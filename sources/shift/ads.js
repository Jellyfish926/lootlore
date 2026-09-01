/* Adsterra 装载器 —— shiftatmidnightwiki.site
 * ============================================================
 * 本文件【只有 Native Banner】,而且【只在 sandbox iframe 里跑】。
 * Banner / Social Bar / Popunder 的 key 和代码分支已在 2026-08-10
 * 全部删除 —— 不是关掉,是删掉。要恢复必须回后台重新 GET CODE,
 * 这道摩擦是故意的:后台没有任何单元级停用功能(publisher 面板无控件,
 * Publisher API 只支持 GET),代码是唯一能保证「只跑 Native Banner」的地方。
 *
 * ── 为什么套 sandbox iframe(2026-08-11 加)──────────────────
 *
 * ⚠️ 先说最容易搞错的一点:**光套 iframe 挡不住劫持。**
 *    普通 iframe 里的脚本照样能写 top.location。同一天在本站真浏览器里
 *    做过对照,同一段敌意脚本:
 *
 *      普通 iframe(不加 sandbox)          → 顶层 URL 被改掉,劫持成功
 *      加 sandbox(下面这套 token)          → 三种写法全部 SecurityError
 *          top.location.href = ...          → SecurityError
 *          top.location = ...               → SecurityError
 *          top.location.replace(...)        → SecurityError
 *          parent.document                  → SecurityError(不透明源)
 *          location.origin                  → "null"
 *
 *    真正生效的是 sandbox 属性,不是 iframe。只抄「套个 iframe」等于什么都没做。
 *
 * 给了什么,为什么:
 *   allow-scripts                    广告脚本得能跑
 *   allow-popups                     点广告要能打开落地页,不给就没有点击收入
 *   allow-popups-to-escape-sandbox   落地页不继承沙箱,否则打开的页面是坏的
 *
 * 故意不给:
 *   allow-top-navigation*   ← 挡强制跳转的就是这一条,**永远不要加**
 *   allow-same-origin       不给 = 不透明源。里面拿不到 parent.document,
 *                           也就无法反过来把自己的 sandbox 属性摘掉再重载。
 *                           allow-scripts + allow-same-origin 同时给是已知逃逸组合。
 *   allow-modals / allow-forms / allow-downloads
 *
 * 代价(明知且接受):不透明源里读 localStorage 会抛 SecurityError,
 * 广告脚本可能整个挂掉,所以内嵌文档先垫一层内存版;依赖第三方 cookie 的
 * 定向会失效,填充率和单价可能下降。拿收益换「站点可用」,这笔交易划算。
 *
 * ── 实测记录(真机 + 移动网络,不挂代理)──────────────────
 *
 * 2026-07-31
 *   仅 Native Banner(Popunder / Social Bar 连单元都没建;
 *   站点级与单元级 Adult ads 均关闭;全站仅 1 个广告单元)
 *   → 手机打开本站【被强制跳转】,页面无法浏览。
 *   停用 Native Banner,改 Social Bar + Banner 300x250
 *   → 【仍然打开即跳转】。
 *   当时结论:跳转与格式无关,是零流量新站 + 分类 Other 的库存质量问题。
 *
 * 2026-08-10  ← 这次做了对照组,上面的结论被推翻
 *   全部关闭            → 【不跳转】   ← 对照组,证明跳转确实来自 Adsterra
 *   Banner 300x250 单开 → 【强制跳转】
 *   Native Banner 单开  → 【不跳转】
 *   → 十天里 Adsterra 的需求侧填充变了。格式之间确实有差别。
 *
 * 2026-08-11
 *   同行反馈 Native Banner 一样会被劫持。所以不再赌「哪个格式干净」——
 *   改成让广告**没有能力**跳转。就是上面那层 sandbox。
 *
 * ⚠️ 所以:**任何结论都有保质期。** 2026-07-31 那条「Native Banner 永久
 *    置 false,不要再打开」差点让我们错过唯一能用的格式。每次改动之后
 *    都要重新真机实测,不要拿旧记录当依据。
 *
 * ⚠️ 机房 IP 会被广告网络拒投(403),在服务器上 curl 或挂代理浏览器
 *    **测不出真实行为**。必须用真实手机 + 移动网络。
 *
 * ⛔ 永远不接 Popunder:Google 2017 年起的明文红线,接了 AdSense 就别想过。
 * ============================================================ */

/* ══ 总闸 ══
 * 出现强制跳转、或者要提交 AdSense 审核之前,把它改成 true 就够了。
 * 一行 Adsterra 代码都不会执行,也不会发出任何请求。 */
var KILL_ALL = false;  /* 2026-08-12 站主决策:提审 AdSense 不关闭任何广告,保持 Adsterra 在投 */

/* Native Banner —— 单元 30483620(NativeBanner_1)。
 * 整段取自后台 GET CODE,逐字节核对。 */
var NATIVE_SRC = "https://pl30584119.effectivecpmnetwork.com/f7bf84b6fd5f9bcf83b18332a482d287/invoke.js";
var NATIVE_ID  = "container-f7bf84b6fd5f9bcf83b18332a482d287";

/* 与两个 Next.js 站的 components/Ads.tsx 逐 token 一致。改这里就要同步改那边。 */
var SANDBOX = "allow-scripts allow-popups allow-popups-to-escape-sandbox";

(function () {
  "use strict";

  if (KILL_ALL) { return; }

  /* 信任页不挂广告 —— about / contact / privacy 是审核员必读页,保持干净。
   * 和 beast 的 SKIP 名单同一条规矩(那边是构建期跳过,这里是运行时跳过:
   * shift 的页面模板一直无差别地发 <script src="/ads.js">,改模板不如在这里拦)。
   * 404 页模板本来就不发这个 script,不用在这里判 —— JS 里也判不可靠。 */
  if (/^\/(about|contact|privacy|privacy-policy|terms|terms-of-service|disclaimer)\/?$/i
        .test(location.pathname)) { return; }
  if (!NATIVE_SRC || !NATIVE_ID) { return; }
  if (!/^https:\/\//.test(NATIVE_SRC)) { return; }   // 会被拼进 iframe 文档,先校验

  // 页面模板里只有 .ad-banner 这个占位(历史遗留,构建脚本还在发它),
  // 没有 .ad-native。找不到就地建一个宿主 —— 否则 querySelector 拿到 null
  // 会静默跳过,实测时会得出「不跳转」的【假阴性】。这个坑踩过一次。
  var host = document.querySelector(".ad-native");
  if (!host) {
    var anchor = document.querySelector(".ad-banner");
    if (!anchor) { return; }
    host = document.createElement("aside");
    host.className = "ad-native";
    host.setAttribute("aria-label", "Advertisement");
    anchor.parentNode.insertBefore(host, anchor);
  }

  // 内嵌文档。src / id 用 JSON.stringify 注入成 JS 字面量,不拼进 HTML 属性,
  // 省掉一整类转义事故。
  var doc =
    '<!doctype html><meta charset="utf-8">' +
    '<style>html,body{margin:0;padding:0;background:transparent;overflow:hidden}' +
    'img{max-width:100%;height:auto}</style><div id=' + JSON.stringify(NATIVE_ID) + '></div><script>' +
    // 不透明源里 localStorage 一读就抛 SecurityError,广告脚本会整个挂掉。
    // 先垫一层内存版,必须在广告脚本之前跑。
    'try{window.localStorage.getItem("_")}catch(e){try{var _m={};' +
    'Object.defineProperty(window,"localStorage",{value:{' +
    'getItem:function(k){return k in _m?_m[k]:null},' +
    'setItem:function(k,v){_m[k]=""+v},removeItem:function(k){delete _m[k]},' +
    'clear:function(){_m={}},key:function(){return null},length:0}})}catch(_){}}' +
    'var s=document.createElement("script");s.src=' + JSON.stringify(NATIVE_SRC) + ';s.async=true;' +
    's.setAttribute("data-cfasync","false");document.body.appendChild(s);' +
    // 不透明源下父页读不到 iframe 内容,所以由里面回传高度;12 秒没填充就报空。
    '(function(){var b=document.getElementById(' + JSON.stringify(NATIVE_ID) + '),n=0,f=0,' +
    't=setInterval(function(){n++;' +
    'var h=Math.max(b?b.scrollHeight:0,document.body.scrollHeight||0);' +
    'if(h>24){f=1;parent.postMessage({__adframe:"fill",h:h},"*")}' +
    'if(n>=40){clearInterval(t);if(!f)parent.postMessage({__adframe:"empty"},"*")}},300)})();' +
    '<\/script>';

  var frame = document.createElement("iframe");
  frame.className = "adframe";
  frame.title = "Advertisement";
  frame.setAttribute("sandbox", SANDBOX);
  frame.setAttribute("loading", "lazy");
  frame.setAttribute("referrerpolicy", "no-referrer-when-downgrade");
  frame.style.cssText = "display:block;width:100%;height:180px;border:0;overflow:hidden";
  frame.srcdoc = doc;

  host.appendChild(frame);
  host.hidden = false;

  // 只认这个 iframe 自己发来的消息,不认来路不明的 message。
  window.addEventListener("message", function (e) {
    var d = e.data;
    if (!d || typeof d !== "object" || !d.__adframe) { return; }
    if (e.source !== frame.contentWindow) { return; }
    if (d.__adframe === "fill") {
      frame.style.height = Math.min((+d.h || 0) + 8, 1400) + "px";
    } else {
      host.hidden = true;          // 没填充就整块折叠,不留空的 Advertisement 框
    }
  });
})();
