HAS_EVENT: bool

class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """
        Prevents all profiles but 'plone-content' from showing up in the
        profile list when creating a Plone site.
        """

def addContentToContainer(container, object, checkConstraints: bool = True):
    """Copy of plone.dexterity.util.addContentToContainer.
    Modified to check the existing Id on the object before paving over it.
    """

def create_frontpage(portal, target_language) -> None: ...
def create_news_topic(portal, target_language) -> None: ...
def create_events_topic(portal, target_language) -> None: ...
def configure_members_folder(portal, target_language) -> None: ...
def import_content(context) -> None:
    """Create default content."""

def setup_various(context) -> None: ...
