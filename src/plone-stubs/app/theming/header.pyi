def setHeader(object, event) -> None:
    """Set a header X-Theme-Enabled in the request if theming is enabled.

    This is useful for checking in things like the portal_css/portal_
    javascripts registries.
    """
