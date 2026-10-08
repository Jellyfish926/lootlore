"""urlnorm —— 全站 URL 规范写法:页面 URL 一律「带尾斜杠」。框架层,不含任何游戏专属文字。

为什么要有它(2026-10-08):
  同一页在线上有两个 200 网址(/about 与 /about/、/beast-of-reincarnation/fr 与 …/fr/),
  canonical / hreflang / sitemap / 站内链接各写各的 —— 原生栏目与四个尾斜杠子站写带斜杠,
  总站自有页与 beast 子站(cleanUrls、无斜杠)写不带斜杠。Google 抓到带斜杠那条、
  canonical 却指向不带斜杠那条 → GSC「备用网页(有适当的规范标记)」,4 个网址不收录。
  修法是全站只留一种写法,配合 vercel.json 的 trailingSlash:true(不带斜杠 308 → 带斜杠)。

规则(与 Vercel trailingSlash:true 的判定同口径,见 scripts/url_consistency_audit.py):
  * path 最后一段不含「.」= 页面 URL → 必须以「/」结尾;
  * path 最后一段含「.」= 文件(sitemap.xml / hub.css / og-image.png …)→ 不动;
  * 斜杠加在 path 末尾,「?查询串」「#锚点」原样留在后面;
  * 裸域名 https://host → https://host/;
  * root_map:游戏根目录没有页面、只做跳转的(default_path 不是 "/" 的游戏,如
    /beast-of-reincarnation/ → /beast-of-reincarnation/en/),站内引用直接写真实目标,
    不让任何站内链接 / 结构化数据指向一个会再跳一次的地址。

两处调用,同一个函数,幂等:
  1) build.transform_urls() 末尾 —— 快照页在「解析之前」就规范好,所以 .sn-body 里的链接
     与 .gates/check_snapshot.py 重算出来的逐字节一致;
  2) build.normalize_out_urls() —— 全部页面写完之后再扫一遍 out/**.html,兜住外壳层
     (导航 / 面包屑 / 页脚 / 总站自有页 / 原生栏目)拼出来的链接。
只改 URL 字符串本身:不碰正文文字、不碰 title / description / H1。
"""
import re


def is_page_path(path: str) -> bool:
    return "." not in path.rsplit("/", 1)[-1]


class UrlNorm:
    def __init__(self, base: str, root_map=None):
        self.base = base.rstrip("/")
        # {"/beast-of-reincarnation/": "/beast-of-reincarnation/en/"}
        self.root_map = dict(root_map or {})
        b = re.escape(self.base)
        # 1) 属性:href / action 的站内值(根相对或本站绝对地址);content 只认本站绝对地址(og:url 等)
        self._attr = [re.compile(r'(\b(?:href|action)=)(")([^"]*)(")'),
                      re.compile(r"(\b(?:href|action)=)(')([^']*)(')"),
                      re.compile(r'(\bcontent=)(")(' + b + r'(?:[/?#][^"]*)?)(")')]
        # 2) 任何被引号整个包住的本站绝对地址(JSON-LD 的 url / @id / item / mainEntityOfPage、内联脚本)
        self._quoted = re.compile(r'''(["'])(''' + b + r'''(?:[/?#][^"'\s<>\\]*)?)\1''')
        # 3) JSON 字符串里转义过的 href(FAQ 的 acceptedAnswer.text 里内嵌的 <a href=\"/x\">)
        self._escaped = re.compile(r'''(href=\\")((?:/|''' + b + r''')[^"\\]*)(\\")''')

    # ------------------------------------------------------------ 单个 URL
    def path(self, p: str) -> str:
        """根相对 path(不含 ?#)→ 规范写法。"""
        if p in ("", "/"):
            return "/"
        if is_page_path(p) and not p.endswith("/"):
            p += "/"
        return self.root_map.get(p, p)

    def url(self, u: str) -> str:
        """站内 URL(根相对 / 本站绝对地址,可带 ?# 尾巴)→ 规范写法;不是站内 URL 原样返回。"""
        m = re.search(r"[?#]", u)
        head, tail = (u, "") if not m else (u[:m.start()], u[m.start():])
        if head == self.base or head.startswith(self.base + "/"):
            return self.base + self.path(head[len(self.base):]) + tail
        if head.startswith("/") and not head.startswith("//"):
            return self.path(head) + tail
        return u

    # ------------------------------------------------------------ 整页
    def html(self, html: str) -> str:
        for pat in self._attr:
            html = pat.sub(lambda m: m.group(1) + m.group(2) + self.url(m.group(3)) + m.group(4), html)
        html = self._quoted.sub(lambda m: m.group(1) + self.url(m.group(2)) + m.group(1), html)
        html = self._escaped.sub(lambda m: m.group(1) + self.url(m.group(2)) + m.group(3), html)
        return html
