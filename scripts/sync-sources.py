#!/usr/bin/env python3
"""sync-sources —— 把五个子站仓的构建产物全量刷进 sources/<游戏>/。

内容层规则:sources/<游戏>/ = 子站构建产物的**全量拷贝**,总站不在里面手改任何东西
(需要的变换全部写在 config/hub.json 的 exclude_* / patches,由 build.py 在构建时做)。
因此同步 = 先删干净再拷,不做增量 merge。

每个子站的产物位置:
  beast       Beast-of-Reincarnation   仓根目录即产物(手写静态 html),剔除仓务目录
  shift       shift-at-midnight-wiki   public/(_src 下的 Python 生成器输出)
  sephiria    sephiria-wiki            out/(next build, output:'export')
  dragonsword dragonsword-guide        out/(同上)
  orc         orc-problem-guide        out/(同上)

用法:
  # 五个子站都 checkout 到 <root>/<游戏名> 下,一次同步全部
  python3 scripts/sync-sources.py --src-root subsites
  # 或单独同步一个
  python3 scripts/sync-sources.py --game sephiria --src /path/to/sephiria-wiki

来源 sha 记到 config/sources.json(commit 信息与排障都从这里看)。
"""
import argparse, json, shutil, subprocess, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources"
LEDGER = ROOT / "config" / "sources.json"

# 仓务文件/目录:存在于子站仓但不属于站点产物,拷进来会污染快照
REPO_ONLY = [
    ".git", ".github", ".gates", ".gitignore", "node_modules",
    "planning", "reviews", "scripts", "_src", "_removed", "_ads.zip",
    "README.md", "site-dossier.md", "lessons-inbox.md", "TODO.md",
    "publish-schedule.json",
]

SITES = {
    # sources 目录名 -> 子站仓 / 产物子目录(仓根为 ".")/ 额外剔除
    "beast": {
        "repo": "Jellyfish926/Beast-of-Reincarnation",
        "product": ".",
        "extra_exclude": [],
    },
    "shift": {
        "repo": "Jellyfish926/shift-at-midnight-wiki",
        "product": "public",
        "extra_exclude": [],
        # shift 的 vercel.json 在仓根(不在 public/ 里),但 build.py 要读它的 redirects
        # 生成总站 vercel.json 的 /shift-at-midnight/* 跳转 —— 必须一起拷进快照。
        "extra_from_root": ["vercel.json"],
    },
    "sephiria": {
        "repo": "Jellyfish926/sephiria-wiki",
        "product": "out",
        "extra_exclude": [],
        "normalize_build_id": True,
    },
    "dragonsword": {
        "repo": "Jellyfish926/dragonsword-guide",
        "product": "out",
        "extra_exclude": [],
        "normalize_build_id": True,
    },
    "orc": {
        "repo": "Jellyfish926/orc-problem-guide",
        "product": "out",
        "extra_exclude": [],
        "normalize_build_id": True,
    },
}

# Next 每次 build 都会生成一个随机 buildId,写进 _next/static/<buildId>/ 目录名和每个
# 页面的 RSC payload。不归一化的话,内容一个字没改也会天天产生 300 个文件的假 diff
# (还会连带跑一次 gates + 一次 Vercel 部署)。总站构建时 __next_f 脚本本来就会被
# build.py 剥掉,buildId 在 out/ 里根本不出现,所以换成固定串是安全的。
BUILD_ID_TOKEN = "static-export"

# 总站自己塞进 sources/<游戏>/ 需要保留的文件(相对游戏目录)。目前为空:
# 快照必须与子站产物逐字节一致,任何总站侧的改动都应该写成 hub.json 的 patch。
KEEP = {}


def git_sha(src: Path) -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(src), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return ""


def normalize_build_id(game: str, dst: Path) -> None:
    """把 Next 的随机 buildId 换成固定串,消掉每次构建都产生的假 diff。"""
    static = dst / "_next" / "static"
    if not static.is_dir():
        return
    ids = [d.name for d in static.iterdir()
           if d.is_dir() and (d / "_buildManifest.js").is_file()]
    if len(ids) != 1:
        print(f"[{game}] 跳过 buildId 归一化:找到 {len(ids)} 个候选目录 {ids}")
        return
    bid = ids[0]
    if bid == BUILD_ID_TOKEN:
        return
    (static / bid).rename(static / BUILD_ID_TOKEN)
    n = 0
    for p in dst.rglob("*"):
        if p.is_file() and p.suffix in (".html", ".txt", ".js", ".json"):
            try:
                t = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if bid in t:
                p.write_text(t.replace(bid, BUILD_ID_TOKEN), encoding="utf-8")
                n += 1
    print(f"[{game}] buildId {bid} -> {BUILD_ID_TOKEN}(改写 {n} 个文件)")


def sync_one(game: str, src: Path) -> dict:
    spec = SITES[game]
    product = (src / spec["product"]).resolve() if spec["product"] != "." else src.resolve()
    if not product.is_dir():
        sys.exit(f"[{game}] 产物目录不存在: {product}(Next 站是不是没跑 npm run build?)")

    exclude = set(REPO_ONLY) | set(spec["extra_exclude"])
    dst = SOURCES / game
    keep = {}
    for rel in KEEP.get(game, []):
        p = dst / rel
        if p.is_file():
            keep[rel] = p.read_bytes()

    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)

    n_files = n_html = 0
    for p in sorted(product.rglob("*")):
        rel = p.relative_to(product)
        if rel.parts[0] in exclude:
            continue
        if p.is_dir():
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
        n_files += 1
        if p.suffix == ".html":
            n_html += 1

    for rel in spec.get("extra_from_root", []):
        p = src / rel
        if not p.is_file():
            sys.exit(f"[{game}] 仓根缺少必需文件: {rel}")
        (dst / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst / rel)
        n_files += 1

    for rel, data in keep.items():
        (dst / rel).parent.mkdir(parents=True, exist_ok=True)
        (dst / rel).write_bytes(data)

    if spec.get("normalize_build_id"):
        normalize_build_id(game, dst)

    sha = git_sha(src)
    print(f"[{game}] {product} -> sources/{game}  files={n_files} html={n_html} sha={sha[:7] or '?'}")
    return {
        "repo": spec["repo"],
        "product": spec["product"],
        "sha": sha,
        "files": n_files,
        "html": n_html,
        "synced_at": datetime.datetime.now(datetime.timezone.utc)
                        .strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src-root", help="五个子站 checkout 的父目录(子目录名 = sources 下的游戏名)")
    ap.add_argument("--game", choices=sorted(SITES))
    ap.add_argument("--src", help="单个子站仓 checkout 路径")
    a = ap.parse_args()

    ledger = {}
    if LEDGER.is_file():
        ledger = json.loads(LEDGER.read_text(encoding="utf-8")).get("sources", {})

    if a.game:
        if not a.src:
            sys.exit("--game 需要配 --src")
        ledger[a.game] = sync_one(a.game, Path(a.src))
    elif a.src_root:
        root = Path(a.src_root)
        for game in SITES:
            src = root / game
            if not src.is_dir():
                sys.exit(f"[{game}] checkout 目录不存在: {src}")
            ledger[game] = sync_one(game, src)
    else:
        sys.exit("需要 --src-root 或 (--game + --src)")

    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(
        json.dumps({"sources": {k: ledger[k] for k in sorted(ledger)}}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"来源账本 -> {LEDGER.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
