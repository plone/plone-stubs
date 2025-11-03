from _typeshed import Incomplete
from collections.abc import Callable
from collections.abc import Generator
from plone.dexterity.content import DexterityContent
from typing import overload
from zope.interface.interface import InterfaceClass
from zope.publisher.browser import BrowserView
from ZPublisher.HTTPRequest import HTTPRequest
from ZTUtils.Lazy import LazyMap

MAX_UNIQUE_ID_ATTEMPTS: int

@overload
def create(
    container: DexterityContent,
    type: str,
    id: str,
    title: str | None,
    safe_id: bool = False,
    **kwargs,
) -> DexterityContent: ...
@overload
def create(
    container: DexterityContent,
    type: str,
    id: str | None,
    title: str,
    safe_id: bool = False,
    **kwargs,
) -> DexterityContent: ...
@overload
def get(path: str, UID: None = None) -> DexterityContent | None:
    """Get an object by path.

    :param path: Path to the object relative to the portal root.
    :type path: string
    :returns: Content object or None if not found
    :rtype: DexterityContent | None
    """

@overload
def get(path: None = None, *, UID: str) -> DexterityContent | None:
    """Get an object by UID.

    :param UID: UID of the object to get.
    :type UID: string
    :returns: Content object or None if not found
    :rtype: DexterityContent | None
    """

def move(
    source: DexterityContent,
    target: DexterityContent,
    id: str | None,
    safe_id: bool = False,
): ...
def rename(obj: DexterityContent, new_id: str, safe_id: bool = False): ...
def copy(
    source: DexterityContent,
    target: DexterityContent,
    id: str | None,
    safe_id: bool = False,
): ...
def delete(
    obj: DexterityContent,
    objects: list[DexterityContent] | None,
    check_linkintegrity: bool = True,
) -> None: ...
def get_state(obj: DexterityContent, default: str = ...) -> None: ...
@overload
def transition(
    obj: DexterityContent, transition: str, to_state=None, **kwargs
) -> None: ...
@overload
def transition(
    obj: DexterityContent, transition: None, to_state=str, **kwargs
) -> None: ...
def disable_roles_acquisition(obj: DexterityContent) -> None: ...
def enable_roles_acquisition(obj: DexterityContent) -> None: ...
def get_view(
    name: str, context: DexterityContent, request: HTTPRequest
) -> BrowserView | None: ...
def get_uuid(obj: DexterityContent) -> str | None: ...
def get_path(obj: DexterityContent, relative: bool = False): ...
def find(
    context: DexterityContent | None,
    depth: int | None,
    unrestricted: bool = False,
    **kwargs,
) -> LazyMap: ...
def iter_ancestors(
    obj: DexterityContent,
    function: Callable | None,
    interface: type[InterfaceClass] | None,
    stop_at: DexterityContent | bool = ...,
) -> Generator[Incomplete, Incomplete, Incomplete]: ...
def get_closest_ancestor(
    obj: DexterityContent,
    function: Callable | None = None,
    interface: type[InterfaceClass] | None = None,
    stop_at: DexterityContent | bool = ...,
): ...
