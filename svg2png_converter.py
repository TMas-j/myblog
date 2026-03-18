import sys
from pathlib import Path

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 630
BG_COLOR = "#0f172a"

SVG_DIR = Path("public/ogp")
PNG_DIR = Path("static/ogp")


def svg_to_png(svg_content: str, output_path: str):
    """PlaywrightでSVGをPNGに変換"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("エラー: playwrightがインストールされていません", file=sys.stderr)
        sys.exit(1)

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ margin: 0; padding: 0; }}
body {{ width: {CANVAS_WIDTH}px; height: {CANVAS_HEIGHT}px; overflow: hidden; background: {BG_COLOR}; }}
</style>
</head>
<body>
{svg_content}
</body>
</html>"""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": CANVAS_WIDTH, "height": CANVAS_HEIGHT})
        page.set_content(html)
        page.wait_for_timeout(300)  # フォント読み込み待機
        page.screenshot(path=output_path, clip={
            "x": 0, "y": 0,
            "width": CANVAS_WIDTH,
            "height": CANVAS_HEIGHT
        })
        browser.close()


def main():
    if not SVG_DIR.exists():
        print(f"エラー: ディレクトリが見つかりません: {SVG_DIR}", file=sys.stderr)
        sys.exit(1)

    svg_files = list(SVG_DIR.glob("*.svg"))
    if not svg_files:
        print(f"SVGファイルが見つかりません: {SVG_DIR}")
        return

    PNG_DIR.mkdir(parents=True, exist_ok=True)

    converted = 0
    skipped = 0
    for svg_path in sorted(svg_files):
        png_path = PNG_DIR / svg_path.with_suffix(".png").name
        if png_path.exists():
            print(f"スキップ: {png_path.name} (既に存在)")
            skipped += 1
            continue

        print(f"変換中: {svg_path.name} → {png_path.name}")
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_content = f.read()
        svg_to_png(svg_content, str(png_path))
        converted += 1

    print(f"\n完了: {converted}件変換, {skipped}件スキップ")


if __name__ == "__main__":
    main()
