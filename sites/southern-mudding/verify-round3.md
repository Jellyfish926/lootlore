# Southern Mudding 终验（第 3 轮）

取证 2026-10-02 12:37 UTC。结论：通过。

1. 5 处改动到位：raw/round3_edits.json 中 G1、G2（community 表格、community scope、index）、G3 的"改后句"在现文件各出现 1 次，"改前句"各 0 次。旧句全目录（12 页正文 + 4 个 JSON）无残留："needs an account"、"Login required"（首字母大写形式）、"keeps no archive"、"so the roster is wider"、"three event listings"、"once per account"、"black hood stripe" 均为 0。
2. 无其他改动：mtime 显示只有 community、index、updates、vehicles 在第 2 轮之后被改（12:36:50）；其余 8 页在第 2 轮读 diff 之前已定稿。对这 4 页的 diff 行数与第 2 轮所见一致（community 比第 2 轮多一行，即 Discord 表格行；index 8、vehicles 4 行，均与此前一致），badges/limiteds/spawning 重新 diff，行集与第 2 轮所验相同。除这五句外无别的改动。
3. frontmatter 合规，12 页：title 53–59，description 156–160，首段 45–60 词（badges 恰为 60、updates/community/nitrous/how-to-play/guides 的 description 恰为 160，在边界内），站内链接 ≥3 且目标存在，date/updated/reviewed 均 2026-10-02，署名 Jellyfi。_images.json、entities.json、config-snippet.json 均可解析。
4. 红线：全目录无真实车厂/车型品牌名，无兑换码字符串。

仍有问题的条目：无。

## 最终逐页结论

| 页 | 结论 |
| --- | --- |
| index、guides、how-to-play、vehicles、gamepasses、limiteds、spawning、nitrous、badges、community、updates、author | 全部可发布 |

发布时点提示：今天约 17:00 UTC 新版本落地。17:00 UTC 之前发布，各页的时点限定句仍然成立；之后发布需先重取描述、updated 时间戳、活动列表和各项计数，并改掉 "25 September 为最新" 的叙述。
