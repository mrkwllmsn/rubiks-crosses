#!/usr/bin/env python3
"""Wrap index.html (authored for the Claude Artifact host) into a standalone page.

index.html is the source of truth. It omits <!doctype>/<html>/<head>/<body> and the
small reset the host injects, including the viewport meta, without which a phone
renders the page at 980px and no mobile media query ever matches.

Output goes to docs/index.html, which is what GitHub Pages serves when the repo is
set to deploy from main /docs. Re-run after editing index.html.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
SRC = HERE / "index.html"
OUT = HERE / "docs" / "index.html"

# everything before this marker is head material; it and the rest is the document body
SPLIT = '<div class="wrap">'

HEAD_OPEN = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root { color-scheme: light dark; }
  body { margin: 0; font: 14px system-ui, sans-serif; }
  img { max-width: 100%; }
  /* the page toggles .coach/.note/.fsbar with el.hidden, and those carry
     display:flex, and without !important the UA rule loses on specificity */
  [hidden] { display: none !important; }
</style>
"""


def main() -> None:
    src = SRC.read_text(encoding="utf-8")
    if SPLIT not in src:
        sys.exit(f"marker {SPLIT!r} not found in {SRC.name}; update build.py")
    head, body = src.split(SPLIT, 1)
    OUT.parent.mkdir(exist_ok=True)
    (OUT.parent / ".nojekyll").touch()   # serve the files as-is, no Jekyll pass
    OUT.write_text(
        HEAD_OPEN + head.rstrip() + "\n</head>\n<body>\n" + SPLIT + body.rstrip() + "\n</body>\n</html>\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT.relative_to(HERE)} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
