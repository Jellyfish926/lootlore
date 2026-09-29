/* Adsterra 装载器 —— beast。只开 Native Banner(单元 30269429)。
 *
 * 2026-09-29 站主决策:单游戏站全部上 Adsterra,并撤掉之前的 sandbox iframe 隔离
 * (原话「之前做过什么阻挡 adsterra 跳转,现在也撤掉,不阻挡」)。
 * 现在是【直投】:invoke.js 直接加载在页面上,不再限制顶层跳转。
 * 旧的 sandbox 版本见 git 历史(2026-08-11 ~ 2026-09-28)。
 *
 * ══ 总闸 ══
 * KILL_ALL = true 时一行 Adsterra 代码都不执行,也不会发出任何请求 ——
 * 不用改 HTML。
 *
 * ⛔ 不要打开 Popunder:Google 2017 年起的明文红线。
 */
var KILL_ALL = false;  /* 2026-09-29 站主决策:单游戏站 Adsterra 开启、直投 */

var NATIVE_SRC = "https://pl30369928.effectivecpmnetwork.com/613468cefca7944af8ea3bb4f9c4c2bb/invoke.js";
var NATIVE_ID  = "container-613468cefca7944af8ea3bb4f9c4c2bb";

(function () {
  "use strict";
  if (KILL_ALL) { return; }
  if (!NATIVE_SRC || !NATIVE_ID || !/^https:\/\//.test(NATIVE_SRC)) { return; }

  var slot = document.querySelector(".ad-native");
  if (!slot) { return; }
  if (document.getElementById(NATIVE_ID)) { return; }

  /* 直投:与后台 GET CODE 的 Native Banner 代码等价(async + data-cfasync + 容器 div) */
  var box = document.createElement("div");
  box.id = NATIVE_ID;
  slot.appendChild(box);
  var s = document.createElement("script");
  s.async = true;
  s.setAttribute("data-cfasync", "false");
  s.src = NATIVE_SRC;
  slot.appendChild(s);
  slot.hidden = false;
})();
