from plone.resource.traversal import ResourceTraverser

class PloneBundlesTraverser(ResourceTraverser):
    name: str
    def traverse(self, name, remaining): ...

def get_zope_page_template_engine(engine):
    """Get Zope-aware page template engine.

    Hopefully a trusted one, but maybe an untrusted one,
    with less possibilities and more security checks.
    We fall back to nothing. This means the original engine will be used.

    Needed since the page template refactoring/cleanup in Zope 4.4.
    See https://github.com/plone/Products.CMFPlone/issues/3141

    This is currently expected to only be called when a zope.pagetemplate
    is being rendered, which can happen with z3c.form related code.
    For Products.PageTemplates, this code should not be needed.
    """
