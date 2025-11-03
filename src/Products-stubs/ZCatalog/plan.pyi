from _typeshed import Incomplete
from typing import NamedTuple

MAX_DISTINCT_VALUES: int
REFRESH_RATE: int
VALUE_INDEX_KEY: str

class Duration(NamedTuple):
    start: Incomplete
    end: Incomplete

class IndexMeasurement(NamedTuple):
    name: Incomplete
    duration: Incomplete
    limit: Incomplete

class Benchmark(NamedTuple):
    duration: Incomplete
    hits: Incomplete
    limit: Incomplete

class RecentQuery(NamedTuple):
    duration: Incomplete
    details: Incomplete

class Report(NamedTuple):
    hits: Incomplete
    duration: Incomplete
    last: Incomplete

logger: Incomplete

class NestedDict:
    """Holds a structure of two nested dicts."""
    @classmethod
    def get(cls, key): ...
    @classmethod
    def set(cls, key, value) -> None: ...
    @classmethod
    def clear(cls) -> None: ...
    @classmethod
    def get_entry(cls, key, key2): ...
    @classmethod
    def set_entry(cls, key, key2, value) -> None: ...
    @classmethod
    def clear_entry(cls, key) -> None: ...

class PriorityMap(NestedDict):
    """This holds a structure of nested dicts.

    The outer dict is a mapping of catalog id to plans. The inner dict holds
    a query key to Benchmark mapping.
    """

    lock: Incomplete
    value: Incomplete
    @classmethod
    def get_value(cls): ...
    @classmethod
    def load_default(cls) -> None: ...
    @classmethod
    def load_from_path(cls, path) -> None: ...
    @classmethod
    def load_pmap(cls, location, pmap) -> None: ...

class Reports(NestedDict):
    """This holds a structure of nested dicts.

    The outer dict is a mapping of catalog id to reports. The inner dict holds
    a query key to Report mapping.
    """

    lock: Incomplete
    value: Incomplete

class CatalogPlan:
    """Catalog plan class to measure and identify catalog queries and plan
    their execution.
    """

    catalog: Incomplete
    cid: Incomplete
    querykey_to_index: Incomplete
    query: Incomplete
    key: Incomplete
    benchmark: Incomplete
    threshold: Incomplete
    def __init__(self, catalog, query=None, threshold: float = 0.1) -> None: ...
    def get_id(self): ...
    res: Incomplete
    start_time: Incomplete
    interim: Incomplete
    stop_time: Incomplete
    duration: Incomplete
    def init_timer(self) -> None: ...
    def valueindexes(self): ...
    def make_key(self, query): ...
    def plan(self): ...
    def start(self) -> None: ...
    def start_split(self, name) -> None: ...
    def stop_split(self, name, result=None, limit: bool = False) -> None: ...
    end_time: Incomplete
    def stop(self) -> None: ...
    def log(self) -> None: ...
    def reset(self) -> None: ...
    def report(self):
        """Returns a statistic report of catalog queries as list of dicts.
        The duration is provided in millisecond.
        """
