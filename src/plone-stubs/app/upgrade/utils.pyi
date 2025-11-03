from _typeshed import Incomplete

logger: Incomplete
plone_version: Incomplete

def version_match(target):
    """Does a target version have the same major and minor version as CMFPlone?

    Given, our versioning scheme is always major.minor.ANYTHING, where major
    and minor are single-digit numbers, we can compare versions as follows,
    without worrying about strictly following semantic versioning.
    """

def null_upgrade_step(tool) -> None:
    """This is a null upgrade, use it when nothing happens"""

def safeEditProperty(obj, key, value, data_type: str = "string") -> None:
    """An add or edit function, surprisingly useful :)"""

def addLinesToProperty(obj, key, values) -> None: ...
def saveCloneActions(actionprovider): ...
def testSkinLayer(skinsTool, layer):
    """Make sure a skin layer exists.

    layer can be a sub folder name, like captchas_core/dynamic
    or a/b/c/d/e.
    """

def cleanupSkinPath(portal, skinName, test: int = 1) -> None:
    """Remove invalid skin layers from skins"""

def cleanUpSkinsTool(context) -> None:
    """Cleanup the portal_skins tool.

    Initially this was created for Plone 4.0 alpha, but was factored out later.

    - Remove directory views for directories missing on the filesystem.

    - Remove invalid skin layers from all skin selections.
    """

def cleanUpToolRegistry(context) -> None: ...
def installOrReinstallProduct(
    portal, product_name, out=None, hidden: bool = False
) -> None:
    """Installs a product

    If product is already installed test if it needs to be reinstalled. Also
    fix skins after reinstalling
    """

def loadMigrationProfile(context, profile, steps=...) -> None: ...
def alias_module(name, target) -> None: ...
def unregisterSteps(context, import_steps=None, export_steps=None) -> None: ...
def updateIconsInBrains(context, typesToUpdate=None) -> None:
    """Update getIcon metadata column in given types.

    typesToUpdate must be a dictionary, for example: {
        # portal_type: ('old_icon.gif', 'new_icon.png'),
        'Document': ('document_icon.gif', 'document_icon.png'),
        }

    The portal_types must have an empty icon_expr, because that is the
    main use case.
    """

def update_catalog_metadata(context, column=None) -> None:
    """Update catalog metadata for all brains."""

def get_property(context, property_name, default_value=None): ...
def remove_utility(iface) -> None:
    """Remove an interface from all utility and adapter registrations.

    Code adapted from
    https://github.com/collective/collective.migrationhelpers/blob/master/src/collective/migrationhelpers/persistent.py

    There are several places where an interface like IPropertiesTool can have
    lodged itself.  We need to find them all, otherwise you will continue to
    see lines like this when first accessing a Plone Site after startup:

    WARNING [OFS.Uninstalled:76][waitress-2] Could not import class
    'PropertiesTool' from module 'Products.CMFPlone.PropertiesTool'

    A pack of the ZODB should get rid of that warning, but various component
    registrations will still be there, and may cause problems later on.
    """
