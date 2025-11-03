from z3c.form.datamanager import AttributeField
from z3c.form.datamanager import DictionaryField

class RelationDataManager(AttributeField):
    """A data manager which uses the z3c.relationfield api to set
    relationships using a schema field."""
    def get(self):
        """Gets the target"""
    def set(self, value):
        """Sets the relationship target"""

class RelationDictDataManager(DictionaryField):
    """A data manager which uses the z3c.relationfield api to set
    relationships using a schema field, for dict-like contexts."""
    def get(self):
        """Gets the target"""
    def query(self, default=...):
        """See z3c.form.interfaces.IDataManager"""
    def set(self, value):
        """Sets the relationship target"""

class RelationListDataManager(AttributeField):
    """A data manager which sets a list of relations"""
    def get(self):
        """Gets the target"""
    def set(self, value) -> None:
        """Sets the relationship target"""

class RelationListDictDataManager(DictionaryField):
    """A data manager which sets a list of relations on dictionary"""
    def get(self):
        """Gets the target"""
    def query(self, default=...):
        """See z3c.form.interfaces.IDataManager"""
    def set(self, value) -> None:
        """Sets the relationship target"""
