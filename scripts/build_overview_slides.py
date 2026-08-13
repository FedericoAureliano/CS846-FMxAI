"""Render overview-slides.md into docs/overview-slides.html: a self-contained
slide deck.

overview-slides.md uses the same frontmatter convention as index.md,
followed by slides separated by a line of three-or-more dashes (---). Each
slide is tagged with an HTML comment marker that says what kind of slide
it is:

  <!-- slide:title -->    the cover slide
  <!-- slide:content -->  a generic "# Heading" + free-form markdown body
                           (used for Grading, Project, Schedule, Speed
                           Matching, etc. -- markdown tables work here too;
                           an inline <svg class="lightning"> in the heading
                           is sized/colored to match, see .lightning)
  <!-- slide:section -->  a theme divider (one per theme, in schedule order)
  <!-- slide:paper -->    a paper slide (title, citation link, theme tags,
                           then optional free-form body markdown)

Slide order and paper-to-theme grouping both come from the order slides
appear in this file (a section slide starts a theme; every paper slide
until the next section slide belongs to it). A content slide dropped in
between sections -- like Speed Matching -- stays top-level: it never
inherits a theme label in the footer, regardless of where it sits. Edit
overview-slides.md directly to reorder, add, or fill in slide bodies;
rerun this script to rebuild.
"""

import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OVERVIEW_SLIDES_MD = ROOT / "overview-slides.md"
DOCS = ROOT / "docs"
IMAGES = ROOT / "images"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n+", re.DOTALL)
SLIDE_SEP_RE = re.compile(r"(?m)^-{3,}\s*$")
MARKER_RE = re.compile(r"\A<!--\s*slide:(\w+)\s*-->\n*")
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
H2_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)
LINK_LINE_RE = re.compile(r"^\[(.+?)\]\((\S+)\)\s*$", re.MULTILINE)
TAGS_LINE_RE = re.compile(r"^((?:`[A-Za-z0-9]+`[ \t]*)+)$", re.MULTILINE)
TAG_RE = re.compile(r"`([A-Za-z0-9]+)`")
STRIKETHROUGH_RE = re.compile(r"~~(.+?)~~")

TOPIC_COLORS = {
    "SSC": "blue",
    "LSD": "green",
    "ATU": "orange",
    "SAT": "purple",
    "PRA": "vermillion",
    "AUF": "skyblue",
    "NSP": "yellow",
    "SUP": "black",
    "TPR": "teal",
    "MLV": "indigo",
    "TST": "magenta",
}

# Matches a theme code bolded in markdown (e.g. "**SAT**") once rendered to
# <strong>SAT</strong>, so it can be turned into the same pill used
# elsewhere -- lets a copied table (like the schedule) get pills for free.
STRONG_CODE_RE = re.compile(r"<strong>(" + "|".join(TOPIC_COLORS) + r")</strong>")

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="icon" type="image/svg+xml" href="images/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=Noto+Emoji&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<div id="stage">
  <div id="deck">
  {slides}
  </div>
  <div id="progress"><div id="progress-bar"></div></div>
  <div id="chrome">
    <div id="footer-brand">{brand}</div>
    <div id="theme-footer"></div>
    <div id="counter"><span id="counter-current">1</span> / <span id="counter-total">1</span></div>
  </div>
</div>
<script>
{js}
</script>
</body>
</html>
"""

CSS = """
:root {
  --font-sans: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --font-emoji: "Noto Emoji";

  --color-base-00: #ffffff;
  --color-base-05: #fcfcfc;
  --color-base-20: #f6f6f6;
  --color-base-30: #e4e4e4;
  --color-base-40: #bdbdbd;
  --color-base-60: #707070;
  --color-base-100: #222222;
  --color-accent: hsl(258, 88%, 66%);
  --color-accent-hover: hsl(258, 88%, 58%);

  --color-orange: #e69f00;
  --color-skyblue: #56b4e9;
  --color-green: #009e73;
  --color-blue: #0072b2;
  --color-vermillion: #d55e00;
  --color-purple: #cc79a7;
  --color-yellow: #7a6a00;
  --color-black: #000000;
  --color-teal: #106b6b;
  --color-indigo: #5b3fa0;
  --color-lime: #218807;
  --color-magenta: #9329a3;

  --bg: var(--color-base-00);
  --bg-alt: var(--color-base-20);
  --fg: var(--color-base-100);
  --muted: var(--color-base-60);
  --border: var(--color-base-30);

  --size-2-2: 4px;
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

  --line-height-normal: 1.5;
  --line-height-tight: 1.15;

  /* Space between the slide frame and the browser edge. */
  --frame-gap: clamp(1.5rem, 4vw, 4rem);
}

* { box-sizing: border-box; }

html, body {
  height: 100%;
  margin: 0;
  overflow: hidden;
}

body {
  background: var(--bg);
  color: var(--fg);
  font-family: var(--font-sans);
  font-size: 16px;
  line-height: var(--line-height-normal);
  -webkit-text-size-adjust: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--frame-gap);
}

/* The 16:9 frame. container-type lets slide typography below be sized in
   cqw/cqh so it scales with the frame itself, not the raw viewport. */
#stage {
  container-type: size;
  position: relative;
  width: min(100%, calc((100vh - 2 * var(--frame-gap)) * 16 / 9));
  max-height: 100%;
  aspect-ratio: 16 / 9;
  border: 1px solid #000;
  background: var(--bg);
  overflow: hidden;
}

#deck {
  position: absolute;
  inset: 0;
}

.slide {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  display: none;
  flex-direction: column;
  justify-content: center;
  padding: 6cqh 7cqw 10cqh;
}

.slide.active { display: flex; }

.slide a {
  color: var(--fg);
  text-decoration-line: underline;
  text-decoration-color: color-mix(in srgb, var(--color-orange) 38%, transparent);
  text-decoration-thickness: 0.6em;
  text-underline-offset: -0.42em;
  text-decoration-skip-ink: none;
}
.slide a:hover { text-decoration-color: var(--color-orange); }

/* Title slide */

.slide-title h1 {
  font-size: clamp(2rem, 6cqw, 3.6rem);
  font-weight: 700;
  margin: 0;
  line-height: var(--line-height-tight);
}

.slide-title h2 {
  font-size: clamp(1rem, 2.4cqw, 1.4rem);
  font-weight: 400;
  color: var(--muted);
  margin: var(--size-4-4) 0 0;
}

.slide-title .meta {
  margin-top: var(--size-4-9);
  color: var(--muted);
  font-size: var(--font-ui-small, 15px);
}

.slide-title .nav-hint {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 8cqh;
  margin: 0;
  text-align: center;
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 13px;
}

.slide-title .nav-hint .nav-key {
  font-family: var(--font-emoji);
  font-variant-emoji: text;
  font-size: 18px;
  letter-spacing: 0.2em;
  vertical-align: -0.15em;
}

/* Content slides (Grading, Project, Paper Discussions, Schedule, ...) */

.slide-content {
  align-items: stretch;
  justify-content: flex-start;
}

.slide-content h1 .lightning {
  display: inline-block;
  width: 1em;
  height: 1em;
  vertical-align: -0.1em;
  margin-left: var(--size-4-2);
  fill: var(--color-accent);
}

.slide-content h1 {
  font-size: clamp(1.6rem, 5cqw, 3rem);
  font-weight: 700;
  margin: 0 0 var(--size-4-6);
  line-height: var(--line-height-tight);
  flex-shrink: 0;
}

.slide-content h1::before {
  content: "> ";
  color: var(--color-accent);
}

.slide-content .body {
  flex: 1 1 auto;
  min-height: 0;
  overflow-y: auto;
  font-size: clamp(0.9rem, 1.6cqw, 1.15rem);
}

.slide-content .body p,
.slide-content .body ul,
.slide-content .body ol { margin: 0 0 var(--size-4-3); }

.slide-content .body li { margin: 0 0 var(--size-2-2); }

.slide-content .body table {
  width: 100%;
  border-collapse: collapse;
  font-size: clamp(0.75rem, 1.3cqw, 0.95rem);
}

.slide-content .body th, .slide-content .body td {
  text-align: left;
  padding: var(--size-4-1) var(--size-4-3);
  vertical-align: top;
}

.slide-content .body thead th {
  border-bottom: 2px solid var(--fg);
  font-weight: 600;
}

.slide-content .body tbody tr:not(:last-child) td {
  border-bottom: 1px solid var(--border);
}

.slide-content .body del { color: var(--muted); text-decoration-thickness: 0.12em; }

.slide-content .body pre {
  background: var(--bg-alt);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: var(--size-4-4);
  margin: 0 0 var(--size-4-3);
  overflow-x: auto;
}

.slide-content .body pre code {
  font-family: var(--font-mono);
  font-size: clamp(0.72rem, 1.2cqw, 0.9rem);
  line-height: var(--line-height-normal);
}

/* Section (theme divider) slides */

.slide-section {
  align-items: flex-start;
  justify-content: center;
}

.slide-section .section-head {
  display: flex;
  align-items: baseline;
  gap: var(--size-4-4);
}

.slide-section h1 {
  font-size: clamp(1.6rem, 5.5cqw, 3.2rem);
  font-weight: 700;
  line-height: var(--line-height-tight);
  margin: 0;
}

.slide-section h1::before {
  content: "> ";
  color: var(--color-accent);
}

.slide-section .section-head .tag {
  font-size: clamp(0.85rem, 1.7cqw, 1.1rem);
  padding: 4px 14px;
  position: relative;
  top: -0.55em;
}

.slide-section .body {
  margin-top: var(--size-4-6);
  font-size: clamp(0.95rem, 1.6cqw, 1.15rem);
  color: var(--muted);
}

.slide-section .body p, .slide-section .body li { margin: 0 0 var(--size-4-2); }

/* Paper slides */

.slide-paper {
  align-items: stretch;
  justify-content: flex-start;
  padding-top: var(--size-4-9);
  padding-bottom: var(--size-4-9);
}

.slide-paper .paper-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: var(--size-4-2) var(--size-4-4);
  margin-bottom: var(--size-4-6);
  flex-shrink: 0;
}

.slide-paper h2 {
  font-family: var(--font-sans);
  font-weight: 600;
  font-size: clamp(1rem, 1.9cqw, 1.5rem);
  line-height: var(--line-height-tight);
  margin: 0;
  text-align: left;
  flex: 1 1 20rem;
  min-width: 0;
  white-space: normal;
  /* Hanging indent: wrapped lines start after the ">> " prefix below,
     not under it. */
  padding-left: 1.4em;
  text-indent: -1.4em;
}

.slide-paper h2::before {
  content: ">> ";
  color: var(--color-accent);
}

.slide-paper .citation {
  font-family: var(--font-mono);
  color: var(--muted);
  font-size: clamp(0.75rem, 1.2cqw, 0.9rem);
  margin: 0;
  white-space: nowrap;
  flex: 0 0 auto;
}

.tag {
  display: inline-block;
  background: hsla(258, 88%, 66%, 0.14);
  color: var(--color-accent-hover);
  font-size: 12px;
  font-family: var(--font-mono);
  font-weight: 600;
  padding: 2px var(--size-4-2);
  border: 1px solid currentColor;
  border-radius: 999px;
}
.tag + .tag { margin-left: 4px; }

.tag-group {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 4px;
  margin: 0;
}

.slide-paper .paper-head .tag-group { flex: 0 0 auto; }

.c-orange { color: var(--color-orange); }
.c-skyblue { color: var(--color-skyblue); }
.c-green { color: var(--color-green); }
.c-blue { color: var(--color-blue); }
.c-vermillion { color: var(--color-vermillion); }
.c-purple { color: var(--color-purple); }
.c-yellow { color: var(--color-yellow); }
.c-black { color: var(--color-black); }
.c-teal { color: var(--color-teal); }
.c-indigo { color: var(--color-indigo); }
.c-lime { color: var(--color-lime); }
.c-magenta { color: var(--color-magenta); }

.tag.c-orange { background: color-mix(in srgb, var(--color-orange) 16%, white); }
.tag.c-skyblue { background: color-mix(in srgb, var(--color-skyblue) 16%, white); }
.tag.c-green { background: color-mix(in srgb, var(--color-green) 16%, white); }
.tag.c-blue { background: color-mix(in srgb, var(--color-blue) 16%, white); }
.tag.c-vermillion { background: color-mix(in srgb, var(--color-vermillion) 16%, white); }
.tag.c-purple { background: color-mix(in srgb, var(--color-purple) 16%, white); }
.tag.c-yellow { background: color-mix(in srgb, var(--color-yellow) 16%, white); }
.tag.c-black { background: color-mix(in srgb, var(--color-black) 16%, white); }
.tag.c-teal { background: color-mix(in srgb, var(--color-teal) 16%, white); }
.tag.c-indigo { background: color-mix(in srgb, var(--color-indigo) 16%, white); }
.tag.c-lime { background: color-mix(in srgb, var(--color-lime) 16%, white); }
.tag.c-magenta { background: color-mix(in srgb, var(--color-magenta) 16%, white); }

.slide-paper .body {
  flex: 1 1 auto;
  min-height: 0;
  max-width: 56rem;
  margin: 0 auto;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.slide-paper .body p, .slide-paper .body li { font-size: 1.05rem; }

.slide-paper .body figure {
  margin: 0 0 var(--size-4-3);
  text-align: center;
}

.slide-paper .body figure img {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  max-height: 38cqh;
  height: auto;
}

.slide-paper .body figcaption {
  margin-top: var(--size-4-2);
  font-size: 0.78rem;
  line-height: var(--line-height-normal);
  color: var(--muted);
  text-align: left;
}

/* Chrome: progress bar and a 3-column footer (brand / theme / count),
   both pinned inside the frame so they read as part of the slide. */

#progress {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 6px;
  background: var(--bg-alt);
  z-index: 10;
}

#progress-bar {
  height: 100%;
  width: 0%;
  background: var(--color-accent);
  transition: width 0.15s ease;
}

#chrome {
  position: absolute;
  inset: auto 0 0 0;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: var(--size-4-4);
  padding: var(--size-4-2) var(--size-4-5);
  background: linear-gradient(to top, var(--bg) 55%, transparent);
  z-index: 10;
}

#chrome.hidden { display: none; }

#footer-brand, #theme-footer, #counter {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

#footer-brand { justify-self: start; }
#theme-footer { justify-self: center; }
#counter { justify-self: end; }

@media (max-width: 640px) {
  .slide { padding: 5cqh 6cqw 12cqh; }
  #footer-brand { display: none; }
  .slide-paper h2 { flex-basis: 100%; }
  .slide-section .section-head { flex-wrap: wrap; }
}
"""

JS = """
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var total = slides.length;
  var current = 0;

  var counterCurrent = document.getElementById('counter-current');
  var counterTotal = document.getElementById('counter-total');
  var progressBar = document.getElementById('progress-bar');
  var themeFooter = document.getElementById('theme-footer');
  var chrome = document.getElementById('chrome');
  var sectionSlides = slides.filter(function (s) { return s.classList.contains('slide-section'); });
  // Top-level slides: everything except individual paper slides, which
  // nest under the section that precedes them.
  var landmarks = [];
  slides.forEach(function (s, i) { if (!s.classList.contains('slide-paper')) landmarks.push(i); });

  counterTotal.textContent = String(total);

  // Only section/paper slides belong to a theme; content slides (Grading,
  // Speed Matching, etc.) are top-level regardless of where they sit in
  // the deck, so they never inherit a theme label from a slide before them.
  function nearestThemeLabel(i) {
    var cur = slides[i];
    if (!cur.classList.contains('slide-section') && !cur.classList.contains('slide-paper')) {
      return '';
    }
    for (var j = i; j >= 0; j--) {
      if (slides[j].classList.contains('slide-section')) {
        var number = sectionSlides.indexOf(slides[j]) + 1;
        var name = slides[j].getAttribute('data-theme-name') || '';
        return 'Theme ' + number + ': ' + name;
      }
    }
    return '';
  }

  function showSlide(i) {
    slides[current].classList.remove('active');
    current = i;
    slides[current].classList.add('active');

    counterCurrent.textContent = String(current + 1);
    progressBar.style.width = ((current + 1) / total * 100) + '%';
    themeFooter.textContent = nearestThemeLabel(current);
    chrome.classList.toggle('hidden', slides[current].classList.contains('slide-title'));
    history.replaceState(null, '', '#' + (current + 1));
  }

  function next() { if (current + 1 < total) showSlide(current + 1); }
  function prev() { if (current - 1 >= 0) showSlide(current - 1); }

  function nextLandmark() {
    for (var i = 0; i < landmarks.length; i++) {
      if (landmarks[i] > current) { showSlide(landmarks[i]); return; }
    }
  }

  function prevLandmark() {
    for (var i = landmarks.length - 1; i >= 0; i--) {
      if (landmarks[i] < current) { showSlide(landmarks[i]); return; }
    }
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight') {
      e.preventDefault();
      next();
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      prev();
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      nextLandmark();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      prevLandmark();
    }
  });

  var hash = parseInt(location.hash.replace('#', ''), 10);
  var start = Number.isInteger(hash) && hash >= 1 && hash <= total ? hash - 1 : 0;
  showSlide(start);
})();
"""


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


def render_tags(codes: list[str]) -> str:
    spans = "".join(
        f'<span class="tag c-{TOPIC_COLORS.get(c, "purple")}">{c}</span>' for c in codes
    )
    return f'<div class="tag-group">{spans}</div>'


def render_meta_row(meta: dict[str, str]) -> str:
    parts = []
    instructor = meta.get("instructor")
    if instructor:
        instructor_url = meta.get("instructor_url")
        parts.append(f'<a href="{instructor_url}">{instructor}</a>' if instructor_url else instructor)
    parts.extend(
        meta[key] for key in ("course", "university", "term", "schedule", "location") if meta.get(key)
    )
    return f'<p class="meta">{" &middot; ".join(parts)}</p>' if parts else ""


# Emoji sequences (base codepoint + VS16 U+FE0F for emoji presentation):
# left/right arrow, up/down arrow.
NAV_HINT = (
    '<p class="nav-hint">'
    '<span class="nav-key">&#11013;&#65039; &#10145;&#65039;</span> move between slides'
    " &middot; "
    '<span class="nav-key">&#11014;&#65039; &#11015;&#65039;</span> jump between sections'
    "</p>"
)


def render_title_slide(body: str, meta: dict[str, str]) -> str:
    h1 = H1_RE.search(body)
    sub_match = re.search(r"^##\s+(.+)$", body, re.MULTILINE)
    title = h1.group(1) if h1 else ""
    subtitle = f"<h2>{sub_match.group(1)}</h2>" if sub_match else ""
    meta_row = render_meta_row(meta)
    return f'<div><h1>{title}</h1>{subtitle}{meta_row}</div>{NAV_HINT}'


def render_markdown_body(rest: str) -> str:
    if not rest:
        return ""
    rest = STRIKETHROUGH_RE.sub(r"<del>\1</del>", rest)
    html = markdown.markdown(rest, extensions=["extra", "sane_lists"])
    html = STRONG_CODE_RE.sub(
        lambda m: f'<span class="tag c-{TOPIC_COLORS[m.group(1)]}">{m.group(1)}</span>', html
    )
    return f'<div class="body">{html}</div>'


def render_content_slide(body: str) -> str:
    h1 = H1_RE.search(body)
    title = h1.group(1) if h1 else ""
    rest = body[h1.end():].strip() if h1 else body.strip()
    return f'<h1>{title}</h1>{render_markdown_body(rest)}'


def render_section_slide(body: str) -> tuple[str, str, str]:
    h1 = H1_RE.search(body)
    tags_match = TAGS_LINE_RE.search(body)
    name = h1.group(1) if h1 else ""
    codes = TAG_RE.findall(tags_match.group(1)) if tags_match else []
    code = codes[0] if codes else ""

    rest_start = tags_match.end() if tags_match else (h1.end() if h1 else 0)
    rest = body[rest_start:].strip()

    head = f'<div class="section-head"><h1>{name}</h1>{render_tags(codes)}</div>'
    return f'{head}{render_markdown_body(rest)}', name, code


def render_paper_slide(body: str) -> str:
    h2 = H2_RE.search(body)
    title = h2.group(1) if h2 else ""

    link = LINK_LINE_RE.search(body)
    citation = f'<p class="citation"><a href="{link.group(2)}">{link.group(1)}</a></p>' if link else ""

    tags_match = TAGS_LINE_RE.search(body)
    codes = TAG_RE.findall(tags_match.group(1)) if tags_match else []

    rest_start = tags_match.end() if tags_match else (link.end() if link else (h2.end() if h2 else 0))
    rest = body[rest_start:].strip()

    head = f'<div class="paper-head"><h2>{title}</h2>{citation}{render_tags(codes)}</div>'
    return f'{head}{render_markdown_body(rest)}'


def build_slides(text: str, meta: dict[str, str]) -> str:
    chunks = [c.strip() for c in SLIDE_SEP_RE.split(text) if c.strip()]
    html_slides = []

    for chunk in chunks:
        marker_match = MARKER_RE.match(chunk)
        if not marker_match:
            continue
        kind = marker_match.group(1)
        body = chunk[marker_match.end():]

        if kind == "title":
            inner = render_title_slide(body, meta)
            html_slides.append(f'<section class="slide slide-title active">{inner}</section>')
        elif kind == "content":
            inner = render_content_slide(body)
            html_slides.append(f'<section class="slide slide-content">{inner}</section>')
        elif kind == "section":
            inner, name, code = render_section_slide(body)
            html_slides.append(
                f'<section class="slide slide-section" '
                f'data-theme="{code}" data-theme-name="{name}">{inner}</section>'
            )
        elif kind == "paper":
            inner = render_paper_slide(body)
            html_slides.append(f'<section class="slide slide-paper">{inner}</section>')

    return "\n".join(html_slides)


def main() -> None:
    raw = OVERVIEW_SLIDES_MD.read_text(encoding="utf-8")
    meta, text = parse_frontmatter(raw)
    slides_html = build_slides(text, meta)

    title = meta.get("title", "Overview Slides")
    brand = " &middot; ".join(
        meta[key] for key in ("instructor", "course", "university") if meta.get(key)
    )
    html = PAGE.format(title=title, css=CSS, slides=slides_html, js=JS, brand=brand)

    DOCS.mkdir(exist_ok=True)
    (DOCS / "overview-slides.html").write_text(html, encoding="utf-8")

    (DOCS / "images").mkdir(exist_ok=True)
    import shutil
    shutil.copy(IMAGES / "favicon.svg", DOCS / "images" / "favicon.svg")

    print(f"Wrote {DOCS / 'overview-slides.html'}")


if __name__ == "__main__":
    main()
