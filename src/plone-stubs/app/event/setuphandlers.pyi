from _typeshed import Incomplete

logger: Incomplete

class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Prevents profiles, which should not be user-installable from showing
        up in the profile list when creating a Plone site.

        plone.app.event:testing .. Testing profile, which provides an
        example type.
        """

def setup_catalog(context) -> None:
    """Setup plone.app.event's indices in the catalog.

    Doing it here instead of in profiles/default/catalog.xml means we
    do not need to reindex those indexes after every reinstall.

    See these discussions for more info about index clearing with catalog.xml:
        http://plone.293351.n2.nabble.com/How-to-import-catalog-xml-without-
        emptying-the-indexes-td2302709.html
        https://mail.zope.org/pipermail/zope-cmf/2007-March/025664.html
    """
