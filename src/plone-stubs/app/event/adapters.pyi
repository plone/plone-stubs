from plone.app.contentlisting.realobject import RealContentListingObject

class OccurrenceContentListingObject(RealContentListingObject):
    def __getattr__(self, name):
        """We'll override getattr so that we can defer name lookups to
        the real underlying objects without knowing the names of all
        attributes.
        """
