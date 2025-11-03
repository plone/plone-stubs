from _typeshed import Incomplete

class ContentItemLookup:
    """General lookup for browser views and page templates.

    1. Attempt to look up a ruleset using z3c.caching.registry.lookup()
       and return that if found (this is necessary because this adapter will
       override the default lookup in most cases).

    2. Get the name of the published object (i.e. the name of the view or
       page template).

    3. Otherwise, look up the published name in the page template mapping (as
       PageTemplateLookup does now) and return that if found

    4. Find the parent of the published object, possibly a content object.

       4.1. If the parent is a content object:
       4.1.1. Get the default view of the parent content object
       4.1.2. If the name of the published object is the same as the default
              view of the parent:
       4.1.2.1. Otherwise, look up the parent type in the content type mapping
                and return that if found
       4.1.2.2. Look up a ruleset on the parent object and return if that
                matches

    The template mapping is:

    ``plone.app.caching.interfaces.IPloneCacheSettings.templateRulesetMapping``

    The content type mapping is:

    ``plone.app.caching.interfaces.IPloneCacheSettings.contentTypeRulesetMapping``.

    Note that this lookup is *not* invoked for a view which happens to use a
    page template to render itself.
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...
