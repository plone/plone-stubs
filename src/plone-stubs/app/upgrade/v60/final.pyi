from _typeshed import Incomplete

import types

logger: Incomplete
SITE_ADMIN: str
SITE_ADMIN_PERMISSIONS: Incomplete

def rolemap_site_admin(context) -> None:
    """Add Site Administrator role to various permissions.

    Especially for control panels, permissions were defined in Python or zcml
    with both Manager and Site Administrator in the roles.
    On startup, this is set on the Zope level, NOT the Plone level.
    And on the Zope level the Site Administrator role is not defined.
    This works, but can give problems.
    So setting the Site Administrator role was moved to rolemap.xml
    See https://github.com/plone/Products.CMFPlone/pull/3225

    That works for new sites, but migrated sites now had a problem.
    Site Administrators lost all those permissions, and could not even
    see the Site Setup.  How to fix that?  Here we more or less follow this plan:
    https://github.com/plone/Products.CMFPlone/pull/3225#issuecomment-1467095416
    Not entirely though.  What we do for real, is described in inline comments below.
    """

def fix_iterate_profiles(context) -> None:
    """Fix profiles of plone.app.iterate.

    See https://github.com/plone/plone.app.iterate/issues/99
    There used to be only a plone.app.iterate:plone.app.iterate profile.
    This was kept for backwards compatibility, but copied to a
    plone.app.iterate:default profile, as is usual.
    We want to remove the old profile definition, but this might give problems
    when someone still has this installed instead of the default profile.

    Later we may want to do something similar with CMFPlacefulWorkflow:
    https://github.com/plone/Products.CMFPlacefulWorkflow/issues/38
    But this has no default profile yet.
    """

def fix_tinymce_menubar(context) -> None:
    """Fix menubar with 'toolsview' instead of 'tools' and 'view'.

    See https://github.com/plone/Products.CMFPlone/issues/3785
    """

def fix_syndication_settings(context) -> None:
    """Fix Syndication Setting in the registry
    Products.CMFPlone.interfaces.syndication.ISiteSyndicationSettings
    is moved to plone.base.interfaces.syndication.ISiteSyndicationSettings.

    See https://github.com/plone/Products.CMFPlone/issues/3805
    """

def fix_tinymce_format_iconnames(context) -> None:
    """Fix various TinyMCE formats to have the correct icon name.

    See https://github.com/plone/Products.CMFPlone/issues/3905
    """

class BogusPattern:
    pattern: Incomplete
    exception: Incomplete
    def __init__(self, pattern, exception) -> None: ...

class TemporaryReCompile:
    original_compile: Incomplete
    @staticmethod
    def custom_compile(pattern, flags: int = 0):
        """
        Custom compile function to handle problematic patterns while unpickling.
        """
    def __enter__(self) -> None:
        """
        Replace `re.compile` with a custom compile function that
        will return a BogusPattern instance in case the pattern cannot be compiled.
        """
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None:
        """
        Restore the original `re.compile` function.
        """

def cleanup_mimetypes_registry(context) -> None:
    """Sites created with <= Python 2.7 have stored compiled regular expression
    patterns that will not be compatible with Python >= 3.11.
    """
