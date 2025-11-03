from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class VersionPolicy(SimpleItem):
    """A simple class for storing version policy information"""

    security: Incomplete
    id: Incomplete
    title: Incomplete
    def __init__(self, obj_id, title, **kw) -> None: ...
    def Title(self): ...

class ATVersionOnEditPolicy(VersionPolicy):
    """A policy that implements version creation on edit.

    The 'AT' is the name points to Archetypes, but it works for Dexterity as well.
    For Archetypes we used to need portal_form_controller overrides,
    which we installed in a setupPolicyHook method and removed in removePolicyHook.
    In Plone 5.2 this is no longer needed, and in Plone 6 we no longer support Archetypes.

    But the policy class still needs to exist, because this is stored persistently.
    And an instance of it with id 'at_edit_autoversion' needs to be registered,
    as is done in our profiles/default/repositorytool.xml.

    The controlpanel (with code in CMFPlone) expects this id.
    So does plone.app.versioningbehavior.
    Most importantly: if a policy with this id is enabled for a portal_type,
    no matter which class is behind it, a new version is stored on edit.
    """
