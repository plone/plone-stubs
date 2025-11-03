class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Do not show on Plone's list of installable profiles."""
    def getNonInstallableProducts(self):
        """Do not show on Plone's list of installable products.

        This method is only used in Plone 5.1+.
        """

def install_pas_plugin(context) -> None: ...
def post_install_default(context) -> None:
    """Post install of default profile"""
