from plone.app.robotframework.remote import RemoteLibrary

class QuickInstaller(RemoteLibrary):
    def product_is_activated(self, product_name) -> None:
        """Assert that given product_name is activated (installed) in
        the add-ons control panel.
        """
    product_is_installed = product_is_activated
