from _typeshed import Incomplete

class JSONSummarySerializerMetadata:
    def default_metadata_fields(self): ...
    def field_accessors(self): ...
    def non_metadata_attributes(self): ...
    def blocklisted_attributes(self): ...

def merge_serializer_metadata_utilities_data():
    """Merge data returned by utilities registered for IJSONSummarySerializerMetadata."""

class DefaultJSONSummarySerializer:
    """Default ISerializeToJsonSummary adapter.

    Requires context to be adaptable to IContentListingObject, which is
    the case for all content objects providing IContentish.
    """

    context: Incomplete
    request: Incomplete
    default_metadata_fields: Incomplete
    field_accessors: Incomplete
    non_metadata_attributes: Incomplete
    blocklisted_attributes: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...
    def metadata_fields(self): ...

class SiteRootJSONSummarySerializer:
    """ISerializeToJsonSummary adapter for the Plone Site root."""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...
