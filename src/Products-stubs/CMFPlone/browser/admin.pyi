from _typeshed import Incomplete
from functools import cached_property as cached_property
from zope.publisher.browser import BrowserView
from ZPublisher.BaseRequest import DefaultPublishTraverse

HAS_VOLTO: bool
HAS_CACHING: bool
HAS_UPGRADE: bool
LOGGER: Incomplete

class AppTraverser(DefaultPublishTraverse):
    def publishTraverse(self, request, name): ...

class Overview(BrowserView):
    def sites(self, root=None): ...
    def outdated(self, obj): ...
    def can_manage(self): ...
    def upgrade_url(self, site, can_manage=None): ...

class RootLoginRedirect(BrowserView):
    """@@plone-root-login

    This view of the Zope root forces authentication via the root
    acl_users and then redirects elsewhere.
    """
    def __call__(self, came_from=None) -> None: ...

class RootLogout(BrowserView):
    """@@plone-root-logout"""

    logout: Incomplete
    def __call__(self) -> None: ...

class FrontPage(BrowserView):
    index: Incomplete

class AddPloneSite(BrowserView):
    @property
    def default_extension_profiles(self): ...
    def browser_language(self): ...
    def grouped_languages(self, default: str = "en"): ...
    def timezones(self): ...
    def __call__(self): ...

class Upgrade(BrowserView):
    has_upgrade = HAS_UPGRADE
    def upgrades(self): ...
    @cached_property
    def missing_packages(self):
        """Get list of missing packages that were installed in GS.

        Main use case:

        * Create a Product.CMFPlone 6.0 site.
        * Upgrade the code to Products.CMFPlone 6.1.
        * Now the plone.app.discussion package is missing.
          This will give problems, because its GS profile was installed
          by default in 6.0.

        Beware of false positives.  For example when upgrading from Plone 5.2,
        CMFFormController will be missing, but we have code in plone.app.upgrade
        to properly clean this up. So we should not bother the admin with this.
        """
    def versions(self): ...
    def __call__(self): ...
    def can_migrate_to_volto(self): ...
