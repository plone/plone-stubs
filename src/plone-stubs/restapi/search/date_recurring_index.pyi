from _typeshed import Incomplete
from DateTime import DateTime
from plone.restapi.search.query import BaseIndexQueryParser

class DateRecurringIndexQueryParser(BaseIndexQueryParser):
    query_value_type = DateTime
    query_options: Incomplete
