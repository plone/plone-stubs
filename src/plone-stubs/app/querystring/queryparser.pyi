from _typeshed import Incomplete
from typing import NamedTuple

class Row(NamedTuple):
    index: Incomplete
    operator: Incomplete
    values: Incomplete

PATH_INDICES: Incomplete

def parseFormquery(context, formquery, sort_on=None, sort_order=None): ...
def parseAndModifyFormquery(context, query, sort_on=None, sort_order=None): ...
def getPathByUID(context, uid):
    """Returns the path of an object specified by UID"""
