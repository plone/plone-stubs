from _typeshed import Incomplete
from zope.publisher.browser import TestRequest

class MockRequest(TestRequest): ...

class DXFieldPermissionChecker:
    """ """

    DEFAULT_PERMISSION: str
    context: Incomplete
    def __init__(self, context) -> None: ...
    def validate(self, field_name, vocabulary_name=None): ...

class GenericFormFieldPermissionChecker(DXFieldPermissionChecker):
    """Permission checker for when we just have an add view"""

    DEFAULT_PERMISSION: str
    context: Incomplete
    view: Incomplete
    def __init__(self, view) -> None: ...

DXAddViewFieldPermissionChecker = GenericFormFieldPermissionChecker
