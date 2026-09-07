#!/usr/bin/env python3
"""Wrap index.html (authored for the Claude Artifact host) into a standalone page.

index.html is the source of truth. It omits <!doctype>/<html>/<head>/<body> and the
small reset the host injects — including the viewport meta, without which a phone
renders the page at 980px and no mobile media query ever matches. Re-run after editing.
"""
import pathlib
import sys

SRC = pathlib.Path(__file__).with_name("index.html")
OUT = pathlib.Path(__file__).with_name("standalone.html")

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
     display:flex — without !important the UA rule loses on specificity */
  [hidden] { display: none !important; }
</style>
"""


def main() -> None:
    src = SRC.read_text(encoding="utf-8")
    if SPLIT not in src:
        sys.exit(f"marker {SPLIT!r} not found in {SRC.name}; update build.py")
    head, body = src.split(SPLIT, 1)
    OUT.write_text(
        HEAD_OPEN + head.rstrip() + "\n</head>\n<body>\n" + SPLIT + body.rstrip() + "\n</body>\n</html>\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT.name} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
