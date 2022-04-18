import os
from sphinx.util.fileutil import copy_asset_file

__version_trait = (1, 0, 0)
__version = ".".join(map(str, __version_trait))
__syntax_higlight_laanguages_rainbow = [
        "c", "coffeescript", "csharp", "css", "d", "generic",
        "go", "haskell", "html", "java", "javascript", "lua",
        "php", "python", "r", "ruby", "scheme", "shell", "smalltalk"
    ]
__syntax_higlight_laanguages_syntaxhighlighterjs = [
        "AS3", "AppleScript", "Bash", "CSharp", "ColdFusion",
        "Cpp", "Css", "Delphi", "Diff", "Erlang", "Groovy", "JScript",
        "Java", "JavaFX", "Perl", "Php", "Plain", "PowerShell", 
        "Python", "Ruby", "Sass", "Scala", "Sql", "Vb", "Xml"
    ]

def get_html_theme_path():
    return os.path.dirname(__file__)

def update_context(app, pagename, templatename, context, doctree):

    def themata_fetch_syntax_highlighter_js(static_dir, highlighter, code_block_editable, highlighter_theme, iframe_embed):
        syntaxInjectableCode = ""
        is_editable_literal = "true" if code_block_editable == True else "false"
        embed_code_block_in_iframe = "true" if iframe_embed == True else "false"
        return """{}<script>
                const themataSyntaxHighlighter = "{}";
                const themataCodeBlockIsEditable = {};
                const themataSyntaxHighlighterTheme = "{}";
                const themataStaticAssetsDir = "{}";
                const themataSyntaxHighlighterIframeEmbed = {};
                $("pre").parent().css("display", "none");
            </script>""".format(syntaxInjectableCode, highlighter, is_editable_literal, highlighter_theme, static_dir, embed_code_block_in_iframe)

    def themata_fetch_syntax_highlighter_css(static_dir, highlighter, highlighter_theme, iframe_embed):
        return ""

    context["clear_version"] = __version
    context["themata_fetch_syntax_highlighter_js"] = themata_fetch_syntax_highlighter_js
    context["themata_fetch_syntax_highlighter_css"] = themata_fetch_syntax_highlighter_css

#TODO only copy the assets that is used not all
def copy_custom_files_impl(app):
    if app.builder.format == 'html':
        staticdir = os.path.join(app.builder.outdir, '_static')
        copy_asset_file(os.path.abspath(os.path.dirname(__file__) + "/_static/js/prism.js"), staticdir)
        copy_asset_file(os.path.abspath(os.path.dirname(__file__) + "/_static/js/themata.js"), staticdir)
        copy_asset_file(os.path.abspath(os.path.dirname(__file__) + "/_static/js/microlight.js"), staticdir)
        copy_asset_file(os.path.abspath(os.path.dirname(__file__) + "/_static/js/syntaxy.min.js"), staticdir)
        copy_asset_file(os.path.abspath(os.path.dirname(__file__) + "/_static/css/syntaxy.dark.min.css"), staticdir)
        copy_asset_file(os.path.abspath(os.path.dirname(__file__) + "/_static/css/syntaxy.light.min.css"), staticdir)
        copy_asset_file(os.path.abspath(os.path.dirname(__file__) + "/_static/css/syntaxy.purple.min.css"), staticdir)

def copy_custom_files(app, exc):
    if not exc:
        copy_custom_files_impl(app)