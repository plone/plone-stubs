from plone.app.contenttypes.browser.folder import FolderView

class CollectionView(FolderView):
    @property
    def collection_behavior(self): ...
    @property
    def b_size(self): ...
    def results(self, **kwargs):
        """Return a content listing based result set with results from the
        collection query.

        :param **kwargs: Any keyword argument, which can be used for catalog
                         queries.
        :type  **kwargs: keyword argument

        :returns: plone.app.contentlisting based result set.
        :rtype: ``plone.app.contentlisting.interfaces.IContentListing`` based
                sequence.
        """
    def batch(self): ...
    @property
    def album_images(self):
        """Get all images within this collection."""
    @property
    def album_folders(self):
        """Get all folders within this collection."""
    def tabular_fields(self):
        """Return a list of all metadata fields from the catalog that were
        selected.
        """
    @property
    def no_items_message(self): ...
