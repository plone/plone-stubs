from ..utils import NodeAdapterBase
from ..utils import PropertyManagerHelpers
from _typeshed import Incomplete

class PluggableIndexNodeAdapter(NodeAdapterBase):
    """Node im- and exporter for FieldIndex, KeywordIndex."""

    node: Incomplete

class DateIndexNodeAdapter(NodeAdapterBase, PropertyManagerHelpers):
    """Node im- and exporter for DateIndex."""

    node: Incomplete

class DateRangeIndexNodeAdapter(NodeAdapterBase):
    """Node im- and exporter for DateRangeIndex."""

    node: Incomplete

class PathIndexNodeAdapter(NodeAdapterBase):
    """Node im- and exporter for PathIndex."""

    node: Incomplete

class FilteredSetNodeAdapter(NodeAdapterBase):
    """Node im- and exporter for FilteredSet."""

    node: Incomplete

class TopicIndexNodeAdapter(NodeAdapterBase):
    """Node im- and exporter for TopicIndex."""

    node: Incomplete
