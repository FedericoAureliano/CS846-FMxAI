"""Render index.md into docs/index.html: a static, GitHub Pages-ready site."""

import re
import shutil
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter

ROOT = Path(__file__).resolve().parent.parent
INDEX_MD = ROOT / "index.md"
DOCS = ROOT / "docs"
IMAGES = ROOT / "images"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="icon" type="image/svg+xml" href="images/favicon.svg">
{author_meta}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<main>
{body}
</main>
<script>
{filter_script}
</script>
</body>
</html>
"""

CSS = """
:root {{
  --font-sans: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;

  /* Obsidian light theme: Foundations/Colors */
  --color-base-00: #ffffff;
  --color-base-05: #fcfcfc;
  --color-base-10: #fafafa;
  --color-base-20: #f6f6f6;
  --color-base-25: #efefef;
  --color-base-30: #e4e4e4;
  --color-base-35: #dadada;
  --color-base-40: #bdbdbd;
  --color-base-50: #ababab;
  --color-base-60: #707070;
  --color-base-70: #5c5c5c;
  --color-base-100: #222222;
  --color-accent: hsl(258, 88%, 66%);
  --color-accent-hover: hsl(258, 88%, 58%);

  /* Okabe & Ito colorblind-safe palette, used for topic coding */
  --color-orange: #e69f00;
  --color-skyblue: #56b4e9;
  --color-green: #009e73;
  --color-blue: #0072b2;
  --color-vermillion: #d55e00;
  --color-purple: #cc79a7;
  /* darkened from the OI palette's #f0e442; the original is too light for AA text contrast on white */
  --color-yellow: #7a6a00;
  --color-black: #000000;
  /* not in the 8-color OI palette; added for a 9th topic, chosen for hue distance from the above */
  --color-teal: #106b6b;
  /* not in the 8-color OI palette; added for a 10th topic, chosen for hue distance from the above */
  --color-indigo: #5b3fa0;

  --bg: var(--color-base-00);
  --bg-alt: var(--color-base-20);
  --fg: var(--color-base-100);
  --muted: var(--color-base-60);
  --border: var(--color-base-30);
  --code-bg: var(--color-base-20);

  /* Obsidian: Foundations/Spacing (2px grid, for fine-grained spacing) */
  --size-2-1: 2px;
  --size-2-2: 4px;
  --size-2-3: 6px;

  /* Obsidian: Foundations/Spacing (4px grid) */
  --size-4-1: 4px;
  --size-4-2: 8px;
  --size-4-3: 12px;
  --size-4-4: 16px;
  --size-4-5: 20px;
  --size-4-6: 24px;
  --size-4-8: 32px;
  --size-4-9: 36px;
  --size-4-12: 48px;
  --size-4-16: 64px;

  /* Obsidian: Foundations/Typography (bumped up a step; topics stay smallest) */
  --font-text-size: 15px;
  --font-ui-smaller: 11px;
  --font-ui-small: 15px;
  --font-ui-medium: 18px;
  --font-ui-large: 24px;
  --line-height-normal: 1.5;
  --line-height-tight: 1.3;
}}

* {{ box-sizing: border-box; }}

body {{
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--font-sans);
  font-size: var(--font-text-size);
  line-height: var(--line-height-normal);
  -webkit-text-size-adjust: 100%;
}}

main {{
  max-width: 40rem;
  margin: 0 auto;
  padding: var(--size-4-12) var(--size-4-5) var(--size-4-16);
}}

.header-row {{
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  flex-wrap: nowrap;
  gap: var(--size-2-2);
  margin: 0 0 var(--size-4-6);
}}

.draft-banner {{
  background: color-mix(in srgb, var(--color-vermillion) 18%, white);
  border: 2px solid var(--color-vermillion);
  border-radius: 8px;
  padding: var(--size-4-4) var(--size-4-5);
  margin: 0 0 var(--size-4-12);
  font-size: 16px;
  font-weight: 600;
  text-align: center;
  color: var(--fg);
}}

h1, h2, h3 {{
  font-family: var(--font-sans);
  font-weight: 600;
  line-height: var(--line-height-tight);
  color: var(--fg);
}}

h1 {{
  font-size: 20px;
  margin: 0;
  flex-shrink: 0;
}}

h2 {{
  font-size: 17px;
  margin: var(--size-4-8) 0 var(--size-4-2);
}}

h3 {{
  font-size: 15px;
  font-weight: 600;
  margin: var(--size-4-6) 0 var(--size-4-1);
}}

h2::before {{
  content: "> ";
  color: var(--color-accent);
}}

h3::before {{
  content: ">> ";
  color: var(--color-accent);
}}

.meta {{
  margin: 0;
  min-width: 0;
  color: var(--muted);
  white-space: normal;
  text-align: right;
}}

p, ul, ol {{ margin: var(--size-4-4) 0; }}

main > p {{
  color: var(--fg);
  text-align: justify;
}}

a {{
  color: var(--fg);
  text-decoration-line: underline;
  text-decoration-color: color-mix(in srgb, var(--color-orange) 38%, transparent);
  text-decoration-thickness: 0.6em;
  text-underline-offset: -0.42em;
  text-decoration-skip-ink: none;
}}
a:hover {{ text-decoration-color: var(--color-orange); }}

code {{
  font-family: var(--font-mono);
  background: var(--code-bg);
  padding: 0.15em 0.4em;
  border-radius: 4px;
}}

pre {{
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: var(--size-4-4);
  overflow-x: auto;
}}

pre code {{
  background: none;
  padding: 0;
  line-height: var(--line-height-normal);
}}

blockquote {{
  margin: var(--size-4-4) 0;
  padding: var(--size-4-1) var(--size-4-4);
  border-left: 3px solid var(--border);
  color: var(--muted);
}}

hr {{
  border: none;
  border-top: 1px solid var(--border);
  margin: var(--size-4-9) 0;
}}

table {{
  width: 100%;
  border-collapse: collapse;
  margin: var(--size-4-6) 0;
  table-layout: fixed;
}}

th, td {{
  text-align: left;
  padding: var(--size-4-2) var(--size-4-4);
  vertical-align: middle;
}}

thead th {{
  font-size: 13px;
  font-weight: 400;
  color: var(--fg);
  border-bottom: 2px solid var(--fg);
  white-space: nowrap;
  text-align: center;
}}

#topic-filter {{
  font: inherit;
  font-weight: inherit;
  text-transform: inherit;
  letter-spacing: inherit;
  color: inherit;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px var(--size-4-2);
  cursor: pointer;
}}

th:first-child, td:first-child {{
  /* Title: fixed so filtering rows doesn't reflow column widths. */
  width: 50%;
}}

th:nth-child(2), td:nth-child(2) {{
  width: 35%;
}}

th:last-child, td:last-child {{
  width: 15%;
  padding-left: var(--size-2-1);
  padding-right: var(--size-2-1);
}}

tbody tr:nth-child(even) {{
  background: var(--bg-alt);
}}

.tag {{
  display: inline-block;
  background: hsla(258, 88%, 66%, 0.14);
  color: var(--color-accent-hover);
  font-size: var(--font-ui-smaller);
  font-weight: 600;
  padding: 1px var(--size-2-2);
  border: 1px solid currentColor;
  border-radius: 999px;
}}
.tag + .tag {{ margin-left: 1px; }}

.tag-group {{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2px;
}}

.c-orange {{ color: var(--color-orange); }}
.c-skyblue {{ color: var(--color-skyblue); }}
.c-green {{ color: var(--color-green); }}
.c-blue {{ color: var(--color-blue); }}
.c-vermillion {{ color: var(--color-vermillion); }}
.c-purple {{ color: var(--color-purple); }}
.c-yellow {{ color: var(--color-yellow); }}
.c-black {{ color: var(--color-black); }}
.c-teal {{ color: var(--color-teal); }}
.c-indigo {{ color: var(--color-indigo); }}

.tag.c-orange {{ background: color-mix(in srgb, var(--color-orange) 16%, white); }}
.tag.c-skyblue {{ background: color-mix(in srgb, var(--color-skyblue) 16%, white); }}
.tag.c-green {{ background: color-mix(in srgb, var(--color-green) 16%, white); }}
.tag.c-blue {{ background: color-mix(in srgb, var(--color-blue) 16%, white); }}
.tag.c-vermillion {{ background: color-mix(in srgb, var(--color-vermillion) 16%, white); }}
.tag.c-purple {{ background: color-mix(in srgb, var(--color-purple) 16%, white); }}
.tag.c-yellow {{ background: color-mix(in srgb, var(--color-yellow) 16%, white); }}
.tag.c-black {{ background: color-mix(in srgb, var(--color-black) 16%, white); }}
.tag.c-teal {{ background: color-mix(in srgb, var(--color-teal) 16%, white); }}
.tag.c-indigo {{ background: color-mix(in srgb, var(--color-indigo) 16%, white); }}

main > p .tag {{ margin: 0 1px; }}

img {{ max-width: 100%; }}

@media (max-width: 480px) {{
  main {{ padding: var(--size-4-8) var(--size-4-4) var(--size-4-12); }}
  h1 {{ font-size: var(--font-ui-medium); }}
  th, td {{ padding: var(--size-4-1) var(--size-4-2); }}
  .header-row {{ flex-wrap: wrap; }}
  .meta {{ text-align: left; }}
}}

{pygments_css}
"""


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n+", re.DOTALL)
ROW_RE = re.compile(r"<tr>\n(<td>.*?</td>\n<td>.*?</td>\n)<td>([^<]+)</td>\n</tr>", re.DOTALL)
TOPICS_HEADER_RE = re.compile(r"<th>Topics</th>")
LEGEND_ITEM_RE = re.compile(r"<strong>(.+?)</strong>")

FILTER_SCRIPT = """
document.addEventListener('DOMContentLoaded', function () {
  var select = document.getElementById('topic-filter');
  if (!select) return;
  var rows = document.querySelectorAll('tbody tr');
  select.addEventListener('change', function () {
    var value = select.value;
    rows.forEach(function (row) {
      var topics = (row.getAttribute('data-topics') || '').split(' ');
      row.style.display = !value || topics.indexOf(value) !== -1 ? '' : 'none';
    });
  });
});
"""

TOPIC_COLORS = {
    "SSC": "blue",
    "LCD": "green",
    "ATU": "orange",
    "SAT": "purple",
    "PRA": "vermillion",
    "AUF": "skyblue",
    "NSP": "yellow",
    "SUP": "black",
    "TPR": "teal",
    "MLV": "indigo",
}


def wrap_tag_cells(body: str) -> str:
    """Style the last (topic) column of the table as pill buttons, color
    coded to match the legend (see TOPIC_COLORS / colorize_legend), and
    stamp each row with a data-topics attribute so the header dropdown
    (see build_topic_filter) can filter rows client-side.

    Rows are always three plain <td>...</td> cells (Title, Link, Topics)
    followed by </tr>, so a full row can be matched and its topic cell
    (the third) rewritten without touching the other two. A cell may hold
    several comma-separated topics, each becoming its own pill.
    """

    def render(match: re.Match) -> str:
        other_cells = match.group(1)
        tags = [t.strip() for t in match.group(2).split(",") if t.strip()]
        spans = "".join(
            f'<span class="tag c-{TOPIC_COLORS.get(t, "purple")}">{t}</span>'
            for t in tags
        )
        data_topics = " ".join(tags)
        return (
            f'<tr data-topics="{data_topics}">\n{other_cells}'
            f'<td><span class="tag-group">{spans}</span></td>\n</tr>'
        )

    return ROW_RE.sub(render, body)


def build_topic_filter(body: str) -> str:
    """Replace the "Topics" table header with a <select> that filters
    rows by their data-topics attribute (see wrap_tag_cells)."""

    options = ['<option value="">All</option>']
    options.extend(f'<option value="{code}">{code}</option>' for code in TOPIC_COLORS)
    select = (
        '<th><select id="topic-filter" aria-label="Filter by topic">'
        + "".join(options)
        + "</select></th>"
    )
    return TOPICS_HEADER_RE.sub(select, body)


def colorize_legend(body: str) -> str:
    """Replace each legend entry's bolded code with the same pill used in
    the table, on the left of the line, color matched via TOPIC_COLORS."""

    def render(match: re.Match) -> str:
        code = match.group(1)
        color = TOPIC_COLORS.get(code)
        if not color:
            return match.group(0)
        return f'<span class="tag c-{color}">{code}</span>'

    return LEGEND_ITEM_RE.sub(render, body)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        if key.strip():
            meta[key.strip()] = value.strip()
    return meta, text[match.end():]


def main() -> None:
    raw = INDEX_MD.read_text(encoding="utf-8")
    meta, text = parse_frontmatter(raw)

    body = markdown.markdown(
        text,
        extensions=["extra", "sane_lists", "fenced_code", "codehilite"],
        extension_configs={"codehilite": {"guess_lang": False}},
    )

    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "CS846: FMxAI"

    author_meta = ""
    meta_parts = []
    instructor = meta.get("instructor")
    if instructor:
        author_meta = f'<meta name="author" content="{instructor}">'
        instructor_url = meta.get("instructor_url")
        who = f'<a href="{instructor_url}">{instructor}</a>' if instructor_url else instructor
        meta_parts.append(who)

    meta_parts.extend(meta[key] for key in ("term", "schedule", "location") if meta.get(key))

    if meta_parts:
        meta_row = f'<p class="meta">{" · ".join(meta_parts)}</p>'
        body = re.sub(
            r"<h1>(.*?)</h1>",
            lambda m: f'<div class="header-row">\n<h1>{m.group(1)}</h1>\n{meta_row}\n</div>',
            body,
            count=1,
        )

    body = wrap_tag_cells(body)
    body = build_topic_filter(body)
    body = colorize_legend(body)

    pygments_css = HtmlFormatter(style="default").get_style_defs(".codehilite")
    css = CSS.format(pygments_css=pygments_css)
    html = PAGE.format(
        title=title,
        css=css,
        body=body,
        author_meta=author_meta,
        filter_script=FILTER_SCRIPT,
    )

    DOCS.mkdir(exist_ok=True)
    (DOCS / "index.html").write_text(html, encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    (DOCS / "images").mkdir(exist_ok=True)
    shutil.copy(IMAGES / "favicon.svg", DOCS / "images" / "favicon.svg")

    print(f"Wrote {DOCS / 'index.html'}")


if __name__ == "__main__":
    main()
