/* Adsterra 装载器 —— beast。只开 Native Banner(单元 30269429),
 * 且只在 sandbox iframe 里跑。
 *
 * ⚠️ 最容易搞错的一点:**光套 iframe 挡不住劫持。**
 *    普通 iframe 里的脚本照样能写 top.location。2026-08-11 在姊妹站
 *    真浏览器里做过对照,同一段敌意脚本:
 *      普通 iframe(无 sandbox) → 顶层 URL 被改掉,劫持成功
 *      加 sandbox(下面这套)     → top.location 三种写法全部 SecurityError,
 *                                 parent.document 也读不到,origin 是 "null"
 *    真正生效的是 sandbox 属性,不是 iframe 本身。
 *
 * 故意不给 allow-top-navigation*(挡跳转的就是这一条)
 * 故意不给 allow-same-origin(不给 = 不透明源,里面摘不掉自己的 sandbox)
 *
 * ══ 总闸 ══
 * KILL_ALL = true 时一行 Adsterra 代码都不执行,也不会发出任何请求。
 * 出现强制跳转、或者要提交 AdSense 审核之前,把它改成 true 就够了 ——
 * 不用改 149 个 HTML。
 *
 * ⛔ 不要打开 Popunder:Google 2017 年起的明文红线。
 * ⚠️ 任何改动之后必须用真实手机 + 移动网络(不挂代理)实测一遍。
 *    机房 IP 会被广告网络拒投,服务器 curl 和代理浏览器测不出真实行为。
 */
var KILL_ALL = false;  /* 2026-08-12 站主决策:提审 AdSense 不关闭任何广告,保持 Adsterra 在投 */

var NATIVE_SRC = "https://pl30369928.effectivecpmnetwork.com/613468cefca7944af8ea3bb4f9c4c2bb/invoke.js";
var NATIVE_ID  = "container-613468cefca7944af8ea3bb4f9c4c2bb";

/* 与 seo-factory 三个站逐 token 一致。改这里就要同步改那边。 */
var SANDBOX = "allow-scripts allow-popups allow-popups-to-escape-sandbox";

(function () {
  "use strict";
  if (KILL_ALL) { return; }
  if (!NATIVE_SRC || !NATIVE_ID) { return; }
  if (!/^https:\/\//.test(NATIVE_SRC)) { return; }

  var slot = document.querySelector(".ad-native");
  if (!slot) { return; }

  var doc =
    '<!doctype html><meta charset="utf-8">' +
    '<style>html,body{margin:0;padding:0;background:transparent;overflow:hidden}' +
    'img{max-width:100%;height:auto}</style><div id=' + JSON.stringify(NATIVE_ID) + '></div><script>' +
    'try{window.localStorage.getItem("_")}catch(e){try{var _m={};' +
    'Object.defineProperty(window,"localStorage",{value:{' +
    'getItem:function(k){return k in _m?_m[k]:null},' +
    'setItem:function(k,v){_m[k]=""+v},removeItem:function(k){delete _m[k]},' +
    'clear:function(){_m={}},key:function(){return null},length:0}})}catch(_){}}' +
    'var s=document.createElement("script");s.src=' + JSON.stringify(NATIVE_SRC) + ';s.async=true;' +
    's.setAttribute("data-cfasync","false");document.body.appendChild(s);' +
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

  slot.appendChild(frame);
  slot.hidden = false;

  window.addEventListener("message", function (e) {
    var d = e.data;
    if (!d || typeof d !== "object" || !d.__adframe) { return; }
    if (e.source !== frame.contentWindow) { return; }
    if (d.__adframe === "fill") {
      frame.style.height = Math.min((+d.h || 0) + 8, 1400) + "px";
    } else {
      slot.hidden = true;
    }
  });
})();
