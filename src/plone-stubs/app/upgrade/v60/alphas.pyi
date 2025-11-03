from _typeshed import Incomplete

logger: Incomplete

def remove_temp_folder(context) -> None:
    """Remove temp_folder from Zope root if broken."""

FT_PROPERTIES_TO_KEEP: Incomplete

def change_plone_site_fti(context) -> None: ...
def make_site_dx(context) -> None:
    """Make the Plone Site a dexterity container"""

def add_uuid_to_dxsiteroot(context) -> None:
    """Give the Plone Site an UUID."""

def index_siteroot(context) -> None:
    """Index the Plone Site"""

def remove_broken_modifiers(context) -> None:
    """Remove Archetypes modifiers from portal_modifier.

    For Plone 6 we have removed Archetypes support.
    This includes removing classes for four Archetypes modifiers.
    During normal usage you should not notice this.
    But it is still better to remove them.

    In CMFEditions we have an upgrade step to remove them: removeBrokenModifiers.
    But there are reports of getting a TypeError when loading one of these modifiers
    when running this code, or before this code has had a chance to run.  See
    https://community.plone.org/t/upgrading-migrating-from-5-2-6-to-6-0-5-fails/17577
    So we delete them early on, especially before running fix_unicode_properties below
    which is where it went wrong in this report.

    Note that the objects themselves are not really broken, but they contain an
    attribute '_modifier' that is broken and cannot be loaded.
    """

def fix_unicode_properties(context) -> None:
    """Fix unicode properties.

    This does two things:

    1. Make sure lines contain only strings, instead of bytes,
       or worse: a combination of strings and bytes.
    2. Replace deprecated ulines, utext, utoken, and ustring properties
       with their non-unicode variant, using native strings.

    See https://github.com/plone/Products.CMFPlone/issues/3305

    The main function we use was added in Zope 5.4:
    https://github.com/zopefoundation/Zope/pull/993
    and improved in Zope 5.5:
    https://github.com/zopefoundation/Zope/pull/1009
    """

def cleanup_resources_and_bundles_in_registry(context=None) -> None:
    """Fix registry for es6 resources and new resource registry."""

def add_new_image_scales(context):
    """Add new image scales.

    See PLIP 3279, which adds and updates a few scales, and especially my
    comment on how we should handle upgrades:
    https://github.com/plone/Products.CMFPlone/issues/3279#issuecomment-1064970253

    Summary: we want an upgrade step in plone.app.upgrade that adds the
    completely new scales, without changing existing scales.
    """

def update_catalog_for_image_scales(context) -> None:
    """Update the catalog to add the image_scales column to all brains.

    This may take long.  By default we update, but we check an environment variable
    so you can switch this off:
    UPDATE_CATALOG_FOR_IMAGE_SCALES = 0
    """

def upgrade_plone_module_profiles(context) -> None:
    """Upgrade profiles of core Plone modules to specific versions.

    This means: all packages that are installed when you use the Plone package.
    So this includes optional packages, like multilingual and plone.volto.
    We want to upgrade all of them to a specific version.

    Originally, when you upgrade a Plone 5.2 site to Plone 6.2, this happened:

    * We run all upgrade steps for Products.CMFPlone:plone to Plone 6.2.
    * Then we run all upgrade steps of the other modules.

    The danger is that an upgrade step that works now when Plone 6.0 alpha
    is the latest release, will not work when run on a 6.2 site.
    Or it may undo a plone.app.upgrade fix from 6.1.

    So the new idea is:

    * We run all upgrade steps for Products.CMFPlone:plone to Plone 6.0 alpha or
      beta, wherever we decide to put this function.
    * Then we call this function.  This runs all upgrade steps of the modules that
      were defined around that alpha/beta time.
    * Then we run the rest of the upgrade steps for Products.CMFPlone:plone to 6.2.
    * Then run any remaining upgrade steps for the other modules.

    See https://github.com/plone/Products.CMFPlone/issues/3346

    You can generate an up to date list if you first activate all modules,
    and then with `bin/instance debug` do this:

    >> tool = app.Plone.portal_setup
    >> for profile_id in tool.listProfilesWithUpgrades():
    ...     version = ".".join(tool.getLastVersionForProfile(profile_id))
    ...     print(f\'("{profile_id}", "{version}"),\')

    You must remove Products.CMFPlone:plone from the printed list:
    it would lead to recursion.

    Also, you may need to fix the plone.app.iterate version if it is unknown,
    due to a \'default\' and \'plone.app.iterate\' profile:

    >> tool.getLastVersionForProfile(\'plone.app.iterate:default\')

    See https://github.com/plone/plone.app.iterate/issues/99
    """
