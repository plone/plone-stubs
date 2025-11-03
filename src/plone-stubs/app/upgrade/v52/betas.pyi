from _typeshed import Incomplete
from zope.interface import Interface

logger: Incomplete

def add_exclude_from_nav_index(context) -> None:
    """Add exclude_from_nav index to the portal_catalog."""

def remove_legacy_resource_registries(context) -> None:
    """Remove portal_css and portal_javascripts."""

def remove_interface_indexes_from_relations_catalog() -> None:
    """remove unused interface indexes from relations catalog"""

class IResourceRegistriesSettings(Interface):
    """fake/mock interface to be able to remove non existing dotted path"""

FAKE_RR_PATH: str

def to52beta1(context) -> None: ...
def to52rc1(context) -> None: ...
