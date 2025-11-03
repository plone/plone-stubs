from _typeshed import Incomplete
from plone.memoize import view

logger: Incomplete

class Addons:
    """Performs install/upgrade/uninstall functions on an addon.
    Pulled, mostly intact, from Plone 5.1's products control panel.
    If we reach the point when plone.restapi isn't supporting releases
    prior to 5.1, we might be able to remove this as duplicate code.
    """

    context: Incomplete
    request: Incomplete
    ps: Incomplete
    errors: Incomplete
    def __init__(self, context, request) -> None: ...
    def serializeAddon(self, addon): ...
    def is_profile_installed(self, profile_id): ...
    def is_product_installed(self, product_id): ...
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
        """Return the version of the product (package).

        That implementation used to fall back to getting the version.txt.
        """
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
    def import_profile(self, product_id, profile_id): ...
    @view.memoize
    def marshall_addons(self): ...
    def get_addons(self, apply_filter=None, product_name=None):
        """
        Based on generic setup profiles.

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
