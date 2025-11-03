class SyndicationTool:
    """
    Backward compatible tool. This just implements
    what some other packages use for now to provide
    backwards compatibility.
    """
    def editProperties(
        self,
        updatePeriod=None,
        updateFrequency=None,
        updateBase=None,
        isAllowed=None,
        max_items=None,
    ) -> None:
        """
        Edit the properties for the SystemWide defaults on the
        SyndicationTool.
        """
    def getSyndicatableContent(self, obj):
        """
        An interface for allowing folderish items to implement an
        equivalent of PortalFolderBase.contentValues()
        """
    def isSiteSyndicationAllowed(self):
        """
        Return sitewide syndication policy
        """
    def isSyndicationAllowed(self, obj=None):
        """
        Check whether syndication is enabled for the site.  This
        provides for extending the method to check for whether a
        particular obj is enabled, allowing for turning on only
        specific folders for syndication.
        """
    def enableSyndication(self, obj) -> None:
        """
        Enable syndication for the obj
        """
    def disableSyndication(self, obj) -> None: ...
