from .. import registry
import markdown as _markdown
import bleach
from django.utils.html import escape


EXTENSIONS = [
    "pymdownx.magiclink",
    "pymdownx.betterem",
    "pymdownx.details",
    "pymdownx.emoji",
    "pymdownx.inlinehilite",
    "pymdownx.superfences",
    "pymdownx.tasklist",
    "markdown.extensions.footnotes",
    "markdown.extensions.attr_list",
    "markdown.extensions.def_list",
    "markdown.extensions.tables",
    "markdown.extensions.admonition",
]

ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS + [
    "img",
    "center",
    "iframe",
    "div",
    "span",
    "table",
    "tr",
    "td",
    "th",
    "tr",
    "pre",
    "code",
    "p",
    "hr",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "thead",
    "tbody",
    "sup",
    "dl",
    "dt",
    "dd",
]

ALLOWED_ATTRS = ["src", "width", "height", "href", "class"]


@registry.filter
def markdown(value, hard_wrap=False):
    extensions = EXTENSIONS
    if hard_wrap:
        extensions = EXTENSIONS + ["nl2br"]
    html = _markdown.markdown(value, extensions=extensions)
    html = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS)
    if not html:
        html = escape(value)
    return '<div class="md-typeset">%s</div>' % html
