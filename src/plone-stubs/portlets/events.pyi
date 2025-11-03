def dispatchToComponent(registration, event) -> None:
    """When a utility is registered, dispatch to an event handler registered for
    the particular component registered, the registration and the event.
    """

def registerPortletManagerRenderer(manager, registration, event) -> None:
    """When a portlet manager is registered as a utility, make an appropriate
    adapter registration for its IPortletManagerRenderer so that the
    provider: expression can find it, and ensure the manager's __name__ is
    the same as the name of the utility, which will also be the name of the
    adapter.
    """

def unregisterPortletManagerRenderer(manager, registration, event) -> None:
    """When a portlet manager is unregistered as a utility, unregister its
    IPortletManagerRenderer.
    """
