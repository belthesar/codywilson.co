AUTHOR = "Cody Wilson"
SITENAME = "Cody Wilson"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "assets",
    "better_codeblock_line_numbering",
    "better_figures_and_images",
    "extract_toc",
    "liquid_tags",
    "liquid_tags.youtube",
    "liquid_tags.img",
    "liquid_tags.include_code",
    "liquid_tags.b64img",
    "liquid_tags.audio",
    "liquid_tags.soundcloud",
    "liquid_tags.video",
    "liquid_tags.include_code",
    "liquid_tags.spotify",
    "liquid_tags.notebook",
    "liquid_tags.giphy",
    "neighbors",
    "photos",
    "post_stats",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "sitemap",
    "tipue_search",
    # "yuicompressor"
]

THEME = "themes/elegant"
DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")

APPLAUSE_BUTTON = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
