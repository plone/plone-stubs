from _typeshed import Incomplete
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

class KeepLastNVersionsTool(UniqueObject, SimpleItem, PropertyManager):
    """ """

    id: str
    alternative_id: str
    meta_type: str
    manage_options: Incomplete
    maxNumberOfVersionsToKeep: int
    security: Incomplete
    def beforeSaveHook(self, history_id, obj, metadata={}):
        """Purge all but the n most current versions

        Purges old version so that at maximum ``maxNumberOfVersionsToKeep``
        versions reside in the history.
        """
    def retrieveSubstitute(self, history_id, selector, default=None):
        """Retrieves the next older version

        If there isn't a next older one returns the next newer one.
        """
