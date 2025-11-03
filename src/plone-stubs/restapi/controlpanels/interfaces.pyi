from _typeshed import Incomplete
from zope.interface import Interface

class IControlpanel(Interface):
    title: Incomplete
    group: Incomplete
    schema: Incomplete
    configlet_id: Incomplete
    configlet_category_id: Incomplete
    def add(names) -> None:
        """Create controlpanel children by names"""
    def get(names) -> None:
        """Read controlpanel children by names"""
    def update(names) -> None:
        """Update controlpanel children by names"""
    def delete(names) -> None:
        """Remove controlpanel children by names"""

class IDexterityTypesControlpanel(IControlpanel):
    """Dexterity Types Control panel"""

class IContentRulesControlpanel(IControlpanel):
    """Content Rules Control panel"""
