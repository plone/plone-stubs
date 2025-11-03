from _typeshed import Incomplete

logger: Incomplete

def remove_portal_properties_tool(context) -> None:
    """Remove the portal_properties tool.

    Core Plone has moved to the configuration registry in Plone 5.0.
    Add-ons may have still used it, but we announced we would remove
    it in Plone 6.1.
    """

def remove_ipropertiestool_components(context) -> None:
    """Remove IPropertiesTool components.

    After running `remove_portal_properties_tool` from above,
    some related components may still linger.
    See https://github.com/plone/plone.app.upgrade/issues/338
    """

def maybe_cleanup_discussion(context) -> None:
    """Cleanup some left-overs from plone.app.discussion.

    But only do this when the package is not available.
    In Plone 6.1, the package was made into a core add-on.
    Meaning: it no longer gets pulled in by Products.CMFPlone,
    but only by the Plone package.
    """

def upgrade_registry_tinymce_menubar(context) -> None:
    """
    the interface definition of plone.base.interfaces.controlpanel.ITinyMCEPluginSchema changed
    the field `menubar` is now a TextField
    the registry record must be converted
    """

def make_external_editor_action_condition_safer(context) -> None:
    """Make the condition for the external editor action safer.

    This condition uses `object/externalEditorEnabled`.
    This uses a script in the `plone_scripts` skin layer,
    which we may remove at some point.
    """

def cleanup_tinymce_plugins(context) -> None:
    """
    update tinymce plugins registry entry to new default
    """
