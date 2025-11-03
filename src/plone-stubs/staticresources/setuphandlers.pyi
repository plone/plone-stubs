class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide all profiles from site-creation and quickinstaller."""
    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller.

        Our upgrades profiles are defined in the directory 'upgrades'.
        Plone sees this is a separate product.
        So instead of adding each new upgrade profile to the list of
        non installable profiles above, we can mark the upgrades product
        as non installable.
        """
