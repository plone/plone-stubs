from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterable
from plone.dexterity.content import DexterityContent
from typing import Any
from zope.interface import Interface
from zope.publisher.browser import BrowserView
from ZPublisher.HTTPRequest import HTTPRequest

MAX_UNIQUE_ID_ATTEMPTS: int

def create(
    container: DexterityContent,
    type: str,
    id: str | None = None,
    title: str | None = None,
    safe_id: bool = False,
    **kwargs,
) -> DexterityContent:
    """Create a new content item.

    :param container: [required] Container object in which to create the new object.
    :type container: Folderish content object
    :param type: [required] Type of the object.
    :type type: string
    :param id: Id of the object. At least one of id or title is required.
    :type id: string
    :param title: Title of the object. At least one of id or title is required.
    :type title: string
    :param safe_id: When True, choose a new, non-conflicting id.
    :type safe_id: boolean
    :returns: Content object
    """

def get(
    path: str | None = None,
    UID: str | None = None,
) -> DexterityContent | None:
    """Get an object by path or UID.

    :param path: Path to the object relative to the portal root.
    :type path: string
    :param UID: UID of the object to get.
    :type UID: string
    :returns: Content object or None if not found.
    """

def move(
    source: DexterityContent,
    target: DexterityContent | None = None,
    id: str | None = None,
    safe_id: bool = False,
) -> DexterityContent:
    """Move the object to a target container and/or change its id.

    :param source: [required] Object that we want to move.
    :type source: Content object
    :param target: Target container to which the source object will be moved.
    :type target: Folderish content object
    :param id: New id for the object.
    :type id: string
    :param safe_id: When True, choose a new, non-conflicting id.
    :type safe_id: boolean
    :returns: Content object that was moved.
    """

def rename(
    obj: DexterityContent,
    new_id: str,
    safe_id: bool = False,
) -> DexterityContent:
    """Rename the object.

    :param obj: [required] Object that we want to rename.
    :type obj: Content object
    :param new_id: [required] New id of the object.
    :type new_id: string
    :param safe_id: When True, choose a new, non-conflicting id.
    :type safe_id: boolean
    :returns: Content object that was renamed.
    """

def copy(
    source: DexterityContent,
    target: DexterityContent | None = None,
    id: str | None = None,
    safe_id: bool = False,
) -> DexterityContent:
    """Copy the object to a target container and/or with a new id.

    :param source: [required] Object that we want to copy.
    :type source: Content object
    :param target: Target container to which the source object will be copied.
    :type target: Folderish content object
    :param id: Id of the copied object.
    :type id: string
    :param safe_id: When True, choose a new, non-conflicting id.
    :type safe_id: boolean
    :returns: Content object that was created.
    """

def delete(
    obj: DexterityContent | None = None,
    objects: list[DexterityContent] | None = None,
    check_linkintegrity: bool = True,
) -> None:
    """Delete content object(s).

    :param obj: Object that we want to delete.
    :type obj: Content object
    :param objects: Objects that we want to delete.
    :type objects: List of content objects
    :param check_linkintegrity: Raise exception if there are linkintegrity-breaches.
    :type check_linkintegrity: boolean
    """

def get_state(obj: DexterityContent, default: Any = ...) -> str:
    """Get the current workflow state of the object.

    :param obj: [required] Object that we want to get the state for.
    :type obj: Content object
    :param default: Returned if no workflow is defined for the object.
    :returns: Object's current workflow state, or default.
    :rtype: string
    """

def transition(
    obj: DexterityContent,
    transition: str | None = None,
    to_state: str | None = None,
    **kwargs,
) -> None:
    """Perform a workflow transition for an object.

    :param obj: [required] Object for which we want to perform the workflow transition.
    :type obj: Content object
    :param transition: Name of the workflow transition.
    :type transition: string
    :param to_state: Name of the workflow state.
    :type to_state: string
    """

def disable_roles_acquisition(obj: DexterityContent) -> None:
    """Disable acquisition of local roles on given obj.

    :param obj: [required] Context object to block the acquisition on.
    :type obj: Content object
    """

def enable_roles_acquisition(obj: DexterityContent) -> None:
    """Enable acquisition of local roles on given obj.

    :param obj: [required] Context object to enable the acquisition on.
    :type obj: Content object
    """

def get_view(
    name: str,
    context: DexterityContent,
    request: HTTPRequest | None = None,
) -> BrowserView:
    """Get a BrowserView object.

    :param name: [required] Name of the view.
    :type name: string
    :param context: [required] Context on which to get view.
    :type context: context object
    :param request: Request on which to get view. Defaults to current request.
    :type request: request object
    :returns: BrowserView object.
    """

def get_uuid(obj: DexterityContent) -> str:
    """Get the object's Universally Unique IDentifier (UUID).

    :param obj: [required] Object we want its UUID.
    :type obj: Content object
    :returns: Object's UUID.
    :rtype: string
    """

def get_path(obj: DexterityContent, relative: bool = False) -> str:
    """Get the path of an object.

    :param obj: [required] Object for which to get its path.
    :type obj: Content object
    :param relative: Return a relative path from the portal root.
    :type relative: boolean
    :returns: Path to the object.
    :rtype: string
    """

def find(
    context: DexterityContent | None = None,
    depth: int | None = None,
    unrestricted: bool = False,
    **kwargs,
) -> Iterable[Any]:
    """Find content in the portal.

    :param context: Context for the search.
    :type context: Content object
    :param depth: How far in the content tree we want to search from context.
    :type depth: int
    :param unrestricted: Use unrestrictedSearchResults if True.
    :type unrestricted: boolean
    :returns: Catalog brains.
    :rtype: Iterable
    """

def iter_ancestors(
    obj: DexterityContent,
    function: Callable[[DexterityContent], bool] | None = None,
    interface: Interface | None = None,
    stop_at: DexterityContent | bool | None = ...,
) -> Generator[DexterityContent]:
    """Iterate over the object ancestors.

    :param obj: [required] Object for which we want to iterate over the ancestors.
    :type obj: Content object
    :param function: Optional callable that takes an object and returns a boolean.
    :type function: callable
    :param interface: Optional interface that should be provided by the ancestor.
    :type interface: zope.interface.Interface
    :param stop_at: Optional object at which to stop the iteration. Pass False to
        return all matching objects in the acquisition chain.
    :type stop_at: Content object or False
    :returns: Iterator of ancestor objects, from immediate to site root.
    :rtype: Generator
    """

def get_closest_ancestor(
    obj: DexterityContent,
    function: Callable[[DexterityContent], bool] | None = None,
    interface: Interface | None = None,
    stop_at: DexterityContent | bool | None = ...,
) -> DexterityContent | None:
    """Get the closest ancestor that matches the criteria.

    :param obj: [required] Object for which we want to get the ancestor.
    :type obj: Content object
    :param function: Optional callable that takes an object and returns a boolean.
    :type function: callable
    :param interface: Optional interface that should be provided by the ancestor.
    :type interface: zope.interface.Interface
    :param stop_at: Optional object at which to stop the iteration. Pass False to
        return all matching objects in the acquisition chain.
    :type stop_at: Content object or False
    :returns: Closest matching ancestor or None.
    :rtype: DexterityContent or None
    """
