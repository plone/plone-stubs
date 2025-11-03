def register_layer(layer, name, site_manager=None) -> None:
    """Register the given layer (an interface) with the given name. If it is
    already registered, nothing will be done. If site_manager is not given,
    the current site manager will be used.
    """

def unregister_layer(name, site_manager=None) -> None:
    """Unregister the layer with the given name. If it cannot be found, a
    KeyError is raised.
    """

def registered_layers():
    """Return all currently registered layers"""
