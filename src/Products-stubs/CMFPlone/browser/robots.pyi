from Products.Five.browser import BrowserView

class Robots(BrowserView):
    """Returns a robots.txt.

    It is editable ttw in /@@site-controlpanel or by setting a different
    using a registry.xml with a line such as:
    <record name="plone.robots_txt">
        <value>User-agent: *
    Disallow: /
        </value>
    </record>
    """
    def __call__(self): ...
