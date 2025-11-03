referencedRelationship: str

def getIncomingLinks(obj=None, intid=None, from_attribute=...):
    """Return a generator of incoming relations created using
    plone.app.linkintegrity (Links in Richtext-Fields).
    """

def hasIncomingLinks(obj=None, intid=None):
    """Test if an object is linked to by other objects using
    plone.app.linkintegrity (Links in Richtext-Fields).

    Way to give bool without loading generator into list.
    """

def getOutgoingLinks(obj=None, intid=None, from_attribute=...):
    """Return a generator of outgoing relations created using
    plone.app.linkintegrity (Links in Richtext-Fields).
    """

def hasOutgoingLinks(obj=None, intid=None):
    """Test if an object links to other objects using plone.app.linkintegrity
    (Links in Richtext-Fields).
    """

def linkintegrity_enabled(): ...
def ensure_intid(obj, intids=None): ...
