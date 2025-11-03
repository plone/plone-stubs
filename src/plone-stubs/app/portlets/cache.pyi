def get_language(context, request): ...
def render_cachekey(fun, self):
    """
    Generates a key based on:

    * Portal URL
    * Negotiated language
    * Anonymous user flag
    * Portlet manager
    * Assignment
    * Fingerprint of the data used by the portlet

    """
