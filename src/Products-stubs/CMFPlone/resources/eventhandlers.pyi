def check_registry_update(event) -> None:
    """Check if a profile import may have updated the configuration registry.

    Main concern for now is: the resource registries may have changed.
    This means the resource viewlet caches should be cleared.
    See discussion in https://github.com/plone/Products.CMFPlone/issues/3505
    """
