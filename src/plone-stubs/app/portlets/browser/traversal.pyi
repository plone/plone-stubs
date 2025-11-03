from _typeshed import Incomplete

class ContextPortletNamespace:
    """Used to traverse to a contextual portlet assignable"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...

class DashboardNamespace:
    """Used to traverse to a portlet assignable for the current user for
    the dashboard.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...

class GroupDashboardNamespace:
    """Used to traverse to a portlet assignable for a group for the dashboard"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...

class GroupPortletNamespace:
    """Used to traverse to a group portlet assignable"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...

class ContentTypePortletNamespace:
    """Used to traverse to a content type portlet assignable"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...
