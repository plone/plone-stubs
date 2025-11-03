from _typeshed import Incomplete
from DateTime import DateTime

log: Incomplete
ANY_TYPE: Incomplete

class ZCatalogCompatibleQueryAdapter:
    """Converts a Python dictionary representing a catalog query, but with
    possibly wrong value types, to a ZCatalog compatible query dict suitable
    for passing to catalog.searchResults().

    See the IZCatalogCompatibleQuery interface documentation for details.
    """

    global_query_params: Incomplete
    multiple_types_global_query_params: Incomplete
    ignore_query_params: Incomplete
    context: Incomplete
    request: Incomplete
    catalog: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_index(self, name): ...
    def parse_query_param(self, idx_name, idx_query): ...
    def parse_multiple_types_param(self, idx_name, idx_query):
        """these indexes can contain single str values or a list of strings"""
    def __call__(self, query): ...

class BaseIndexQueryParser:
    """Base class for IIndexQueryParser adapters.

    See the IIndexQueryParser interface documentation for details.
    """

    query_value_type = str
    query_options: Incomplete
    index: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, index=None, context=None, request=None) -> None: ...
    def parse(self, idx_query): ...
    def parse_query_value(self, query_value): ...
    def parse_simple_query(self, idx_query): ...
    def parse_complex_query(self, idx_query): ...

class ZCTextIndexQueryParser(BaseIndexQueryParser):
    query_value_type = str
    query_options: Incomplete

class KeywordIndexQueryParser(BaseIndexQueryParser):
    query_value_type = ANY_TYPE
    query_options: Incomplete

class BooleanIndexQueryParser(BaseIndexQueryParser):
    query_value_type = bool
    query_options: Incomplete
    def parse_query_value(self, query_value): ...

class FieldIndexQueryParser(BaseIndexQueryParser):
    query_value_type = ANY_TYPE
    query_options: Incomplete

class ExtendedPathIndexQueryParser(BaseIndexQueryParser):
    query_value_type = str
    query_options: Incomplete

class DateIndexQueryParser(BaseIndexQueryParser):
    query_value_type = DateTime
    query_options: Incomplete

class DateRangeIndexQueryParser(BaseIndexQueryParser):
    query_value_type = DateTime
    query_options: Incomplete

class UUIDIndexQueryParser(BaseIndexQueryParser):
    query_value_type = str
    query_options: Incomplete
