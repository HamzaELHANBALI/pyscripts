"""Generate a simple static HTML page listing available scripts."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src" / "pyscripts"
DIST_DIR = ROOT / "dist"
OUTPUT_FILE = DIST_DIR / "index.html"


def discover_scripts() -> list[str]:
    scripts = []
    for path in sorted(SOURCE_DIR.glob("*.py")):
        if path.name == "__init__.py":
            continue
        scripts.append(path.stem)
    return scripts


def render_html(scripts: list[str]) -> str:
    items = "\n".join(f"        <li>{script}</li>" for script in scripts)
    return f"""<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>PyScripts CNAM</title>
    <style>
      body {{
        font-family: Arial, sans-serif;
        max-width: 760px;
        margin: 48px auto;
        padding: 0 20px;
        line-height: 1.6;
      }}
      code {{
        background: #f3f4f6;
        padding: 2px 6px;
        border-radius: 4px;
      }}
    </style>
  </head>
  <body>
    <h1>PyScripts CNAM</h1>
    <p>Scripts disponibles dans le depot :</p>
    <ul>
{items}
    </ul>
    <p>Page generee avec <code>scripts/generate_index.py</code>.</p>
  </body>
</html>
"""


def main() -> None:
    DIST_DIR.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(render_html(discover_scripts()), encoding="utf-8")
    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
