#!/usr/bin/env python3
"""Guide Atlas 本地预览服务器 — 模拟 Vercel cleanUrls + trailingSlash:/a/b/ -> a/b.html 或 a/b/index.html
(线上 /a/b 会先 308 到 /a/b/;本地不做跳转,两种写法都直接给页面)"""
import http.server, os, sys, functools
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
ROOT = os.path.dirname(os.path.abspath(__file__))

class H(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.path.split('?')[0].split('#')[0]
        fs = os.path.join(ROOT, path.lstrip('/'))
        if path.endswith('/') and not os.path.isfile(os.path.join(fs, 'index.html')) \
                and os.path.isfile(fs.rstrip('/') + '.html'):
            # 规范写法带尾斜杠:beast 的 en/bosses.html 由 /…/en/bosses/ 提供(en/ 目录本身没有 index)
            self.path = '/' + os.path.relpath(fs.rstrip('/') + '.html', ROOT).replace(os.sep, '/')
        elif not os.path.exists(fs) and not path.endswith('/'):
            for cand in (fs + '.html', os.path.join(fs, 'index.html')):
                if os.path.isfile(cand):
                    self.path = '/' + os.path.relpath(cand, ROOT).replace(os.sep, '/')
                    break
            else:
                if os.path.isfile(os.path.join(ROOT, '404.html')):
                    self.path = '/404.html'
        elif not os.path.exists(fs):
            if os.path.isfile(os.path.join(ROOT, '404.html')):
                self.path = '/404.html'
        return super().send_head()

Handler = functools.partial(H, directory=ROOT)
print(f"预览: http://localhost:{PORT}   (Ctrl+C 停止)")
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
