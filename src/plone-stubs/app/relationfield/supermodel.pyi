from _typeshed import Incomplete
from plone.supermodel.exportimport import BaseHandler

class RelationChoiceBaseHandler(BaseHandler):
    filteredAttributes: Incomplete
    def __init__(self, klass) -> None: ...
    def write(self, field, name, type, elementName: str = "field"): ...

RelationChoiceHandler: Incomplete
RelationListHandler: Incomplete
