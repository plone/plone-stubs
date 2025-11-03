from _typeshed import Incomplete

class Theme:
    """A theme, loaded from a resource directory"""

    rules: Incomplete
    title: Incomplete
    description: Incomplete
    absolutePrefix: Incomplete
    parameterExpressions: Incomplete
    doctype: Incomplete
    preview: Incomplete
    enabled_bundles: Incomplete
    disabled_bundles: Incomplete
    tinymce_content_css: Incomplete
    production_js: Incomplete
    production_css: Incomplete
    development_js: Incomplete
    development_css: Incomplete
    tinymce_styles_css: Incomplete
    def __init__(
        self,
        name,
        rules,
        title=None,
        description=None,
        absolutePrefix=None,
        parameterExpressions=None,
        doctype=None,
        preview=None,
        enabled_bundles=[],
        disabled_bundles=[],
        development_css: str = "",
        development_js: str = "",
        production_css: str = "",
        production_js: str = "",
        tinymce_content_css: str = "",
        tinymce_styles_css: str = "",
    ) -> None: ...
