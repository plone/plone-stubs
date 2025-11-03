from _typeshed import Incomplete
from zope.publisher.browser import BrowserView

logger: Incomplete
_: Incomplete

def munge_search_term(query): ...

class ContentListingView(BrowserView):
    """BrowserView for displaying query results"""
    def __call__(self, **kw): ...

class QueryBuilder(BrowserView):
    """This view is used by the javascripts,
    fetching configuration or results"""
    def __init__(self, context, request) -> None: ...
    def __call__(
        self,
        query,
        batch: bool = False,
        b_start: int = 0,
        b_size: int = 30,
        sort_on=None,
        sort_order=None,
        limit: int = 0,
        brains: bool = False,
        custom_query=None,
    ):
        """Create a zope catalog query and return results.

        :param query: The querystring to be parsed into a zope catalog query.
        :type query: dictionary

        :param batch: Return a plone.batching ``Batch`` instead of a zope
                      catalog result.
        :type batch: boolean

        :param b_start: Start item of the batch.
        :type b_start: integer

        :param b_size: Size of the batch.
        :type b_size: integer

        :param sort_on: Name of the sort index for sorting the results.
        :type sort_on: string

        :param sort_order: The order of the result sorting. Either 'ascending'
                           or 'descending'. 'reverse' is an alias equivalent
                           to 'descending'.
        :type sort_order: string

        :param limit: Limit the results.
        :type limit: integer

        :param brains: Return brains or IContentListing objects.
        :type brains: boolean

        :param custom_query: A dictionary of index names and their associated
                             query values. The custom_query updates the parsed
                             query, thus overriding the query string.
                             May be None.
        :type custom_query: dictionary or None

        """
    def html_results(self, query):
        """html results, used for in the edit screen of a collection,
        used in the live update results"""
    def number_of_results(self, query):
        """Get the number of results"""
    def filter_query(self, query): ...
    def munge_search_term(self, q): ...

class RegistryConfiguration(BrowserView):
    def __call__(self): ...
