from _typeshed import Incomplete
from plone.memoize import view
from Products.Five.browser import BrowserView

logger: Incomplete

class InstallerView(BrowserView):
    """View on all contexts for installing and uninstalling products."""

    ps: Incomplete
    errors: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def is_profile_installed(self, profile_id): ...
    def is_product_installed(self, product_id): ...
    def get_install_profiles(self, product_id):
        """List all installer profile ids of the given name.

        TODO Might be superfluous.
        """
    def get_install_profile(self, product_id, allow_hidden: bool = False):
        """Return the default install profile.

        :param product_id: id of product/package
        :type product_id: string
        :param allow_hidden: Allow getting otherwise hidden profile.
            In the UI this will be False, but you can set it to True in
            for example a call from plone.app.upgrade where you want to
            install a new core product, even though it is hidden for users.
        :type allow_hidden: boolean
        :returns: True on success, False otherwise.
        :rtype: boolean
        """
    def get_uninstall_profile(self, product_id):
        """Return the uninstall profile.

        Note: not used yet.
        """
    def is_product_installable(self, product_id, allow_hidden: bool = False):
        """Does a product have an installation profile?

        :param allow_hidden: Allow installing otherwise hidden products.
            In the UI this will be False, but you can set it to True in
            for example a call from plone.app.upgrade where you want to
            install a new core product, even though it is hidden for users.
        :type allow_hidden: boolean
        :returns: True when product is installable, False otherwise.
        :rtype: boolean
        """
    def get_product_version(self, product_id):
        """Return the version of the product (package)."""
    def get_latest_upgrade_step(self, profile_id):
        """Get highest ordered upgrade step for profile.

        If anything errors out then go back to "old way" by returning
        \'unknown\'.
        """
    def upgrade_info(self, product_id):
        """Returns upgrade info for a product.

        This is a dict with among others two booleans values, stating if
        an upgrade is required and available.

        :param product_id: id of product/package
        :type product_id: string
        :returns: dictionary with info about product
        :rtype: dict
        """
    def upgrade_product(self, product_id):
        """Run the upgrade steps for a product.

        Returns True on success, False otherwise.
        """
    def install_product(self, product_id, allow_hidden: bool = False):
        """Install a product by name.

        :param product_id: id of product/package
        :type product_id: string
        :param allow_hidden: Allow installing otherwise hidden products.
            In the UI this will be False, but you can set it to True in
            for example a call from plone.app.upgrade where you want to
            install a new core product, even though it is hidden for users.
        :type allow_hidden: boolean
        :returns: True on success, False otherwise.
        :rtype: boolean
        """
    def uninstall_product(self, product_id):
        """Uninstall a product by name.

        Returns True on success, False otherwise.
        """

class ManageProductsView(InstallerView):
    """
    Activate and deactivate products in mass, and without weird
    permissions issues
    """
    def __call__(self): ...
    @view.memoize
    def marshall_addons(self): ...
    def get_addons(self, apply_filter=None, product_name=None):
        """
        100% based on generic setup profiles now.

        @filter:= 'installed': only products that are installed and not hidden
                  'upgrades': only products with upgrades
                  'available': products that are not installed bit
                               could be
                  'broken': uninstallable products with broken
                            dependencies

        @product_name:= a specific product id that you want info on. Do
                   not pass in the profile type, just the name

        XXX: I am pretty sure we don't want base profiles ...
        """
    def get_sorted_addon_values(self, apply_filter=None, product_name=None): ...
    def get_upgrades(self):
        """
        Return a list of products that have upgrades on tap
        """
    def get_installed(self): ...
    def get_available(self): ...
    def get_broken(self): ...

class UpgradeProductsView(InstallerView):
    """
    Upgrade a product... or twenty
    """
    def __call__(self) -> None: ...

class InstallProductsView(InstallerView):
    def __call__(self) -> None: ...

class UninstallProductsView(InstallerView):
    def __call__(self) -> None: ...
