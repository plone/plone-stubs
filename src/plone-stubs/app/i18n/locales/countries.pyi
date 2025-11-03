from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.i18n.locales.countries import CountryAvailability

class Countries(SimpleItem, CountryAvailability):
    """A local utility storing a list of available countries.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ICountries, Countries)
      True
    """

    id: str
    title: str
    meta_type: str
    countries: Incomplete
    def __init__(self) -> None: ...
    def getAvailableCountries(self):
        """Return a sequence of country tags for available countries."""
    def setAvailableCountries(self, countries) -> None:
        """Set a list of available country tags."""
