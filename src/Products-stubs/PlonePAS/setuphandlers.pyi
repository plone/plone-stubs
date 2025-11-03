from _typeshed import Incomplete

logger: Incomplete

def activatePluginInterfaces(portal, plugin, disable=None) -> None: ...
def setupRoles(portal) -> None: ...
def registerPluginType(pas, plugin_type, plugin_info) -> None: ...
def registerPluginTypes(pas) -> None: ...
def setupPlugins(portal) -> None: ...
def setupAuthPlugins(
    portal,
    pas,
    plone_pas,
    deactivate_basic_reset: bool = True,
    deactivate_cookie_challenge: bool = False,
) -> None: ...
def updateProperties(tool, properties) -> None: ...
def updateProp(prop_manager, prop_dict) -> None:
    """Provided a PropertyManager and a property dict of {id, value,
    type}, set or update that property as applicable.

    Doesn't deal with existing properties changing type.
    """

def addPAS(portal) -> None: ...
def migrate_root_uf(self) -> None: ...
def pas_fixup(self) -> None: ...
def challenge_chooser_setup(self) -> None: ...
def setupPasswordPolicyPlugin(portal) -> None: ...
def setLoginFormInCookieAuth(context) -> None:
    """Makes sure the cookie auth redirects to 'require_login' instead
    of 'login_form'."""

def addRolesToPlugIn(p) -> None:
    """
    XXX This is horrible.. need to switch PlonePAS to a GenericSetup
    based install so this doesn't need to happen.

    Have to manually register the roles from the 'rolemap' step
    with the roles plug-in.
    """

def setupGroups(site) -> None:
    """
    Create Plone's default set of groups.
    """

def installPAS(portal) -> None: ...
def setupPlonePAS(context) -> None:
    """
    Setup PlonePAS step.
    """

def set_up_zope_root_cookie_auth(context) -> None:
    """
    Change the Zope root `/acl_users` to use a simple cookie login form.
    """
