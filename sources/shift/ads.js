/* Adsterra 装载器 —— shiftatmidnightwiki.site
 * ============================================================
 * 2026-09-29 站主决策:单游戏站全部上 Adsterra,并撤掉之前的
 * sandbox iframe 隔离(原话「之前做过什么阻挡 adsterra 跳转,现在也撤掉,不阻挡」)。
 * 现在是【直投】:invoke.js 直接加载在页面上,不再限制顶层跳转。
 * 旧的 sandbox 版本见 git 历史(2026-08-11 ~ 2026-09-28)。
 * 只保留 Native Banner 单元;Popunder 仍然不接。
 * ============================================================ */

/* ══ 总闸 ══ 改成 true 就一行 Adsterra 代码都不执行。 */
var KILL_ALL = false;  /* 2026-09-29 站主决策:单游戏站 Adsterra 开启、直投 */

/* Native Banner —— 单元 30483620(NativeBanner_1),取自后台 GET CODE。 */
var NATIVE_SRC = "https://pl30584119.effectivecpmnetwork.com/f7bf84b6fd5f9bcf83b18332a482d287/invoke.js";
var NATIVE_ID  = "container-f7bf84b6fd5f9bcf83b18332a482d287";

(function () {
  "use strict";
  if (KILL_ALL) { return; }
  /* 信任页不挂广告 */
  if (/^\/(about|contact|privacy|privacy-policy|terms|terms-of-service|disclaimer|author|editorial-policy)\/?$/i
        .test(location.pathname)) { return; }
  if (!NATIVE_SRC || !NATIVE_ID || !/^https:\/\//.test(NATIVE_SRC)) { return; }

  var host = document.querySelector(".ad-native");
  if (!host) {
    var anchor = document.querySelector(".ad-banner");
    if (!anchor) { return; }
    host = document.createElement("aside");
    host.className = "ad-native";
    host.setAttribute("aria-label", "Advertisement");
    anchor.parentNode.insertBefore(host, anchor);
  }
  if (document.getElementById(NATIVE_ID)) { return; }

  /* 直投:与后台 GET CODE 的 Native Banner 代码等价(async + data-cfasync + 容器 div) */
  var box = document.createElement("div");
  box.id = NATIVE_ID;
  host.appendChild(box);
  var s = document.createElement("script");
  s.async = true;
  s.setAttribute("data-cfasync", "false");
  s.src = NATIVE_SRC;
  host.appendChild(s);
  host.hidden = false;
})();
