from _typeshed import Incomplete
from plone.app.robotframework.remote import RemoteLibrary

HAS_RELOAD: bool
HAS_DEBUG_MODE: bool
HAS_VERBOSE_CONSOLE: bool
ZSERVER_HOST: Incomplete
LISTENER_HOST: Incomplete
LISTENER_PORT: Incomplete

def TIME(): ...
def WAIT(msg): ...
def ERROR(msg): ...
def READY(msg): ...
def start(zope_layer_dotted_name) -> None: ...
def print_urls(zope_layer, xmlrpc_server) -> None:
    """Prints the urls with the chosen ports.

    When using a port 0, the operating system chooses an open port.
    When doing that it is helpful that the URLs with the chosen ports are printed to stdout.
    """

def start_reload(
    zope_layer_dotted_name,
    reload_paths=("src",),
    preload_layer_dotted_name: str = "plone.app.testing.PLONE_FIXTURE",
    extensions=None,
): ...
def server() -> None: ...

class RobotListener:
    ROBOT_LISTENER_API_VERSION: int
    server: Incomplete
    def __init__(self) -> None: ...
    def start_test(self, name, attrs) -> None: ...
    def end_test(self, name, attrs) -> None: ...

ZODB = RobotListener

class Zope2Server:
    stop_zope_server_lazy: bool
    stop_zope_server_layer: Incomplete
    zope_layer: Incomplete
    extra_layers: Incomplete
    def __init__(self) -> None: ...
    def start_zope_server(self, layer_dotted_name) -> None: ...
    def set_zope_layer(self, layer_dotted_name) -> None:
        """Explicitly set the current Zope layer, when you know what you are
        doing
        """
    def amend_zope_server(self, layer_dotted_name) -> None:
        """Set up extra layers up to given layer_dotted_name"""
    def prune_zope_server(self) -> None:
        """Tear down the last set of layers set up with amend_zope_server"""
    def stop_zope_server(self, force: bool = False) -> None: ...
    def zodb_setup(self, layer_dotted_name=None) -> None: ...
    def zodb_teardown(self, layer_dotted_name=None) -> None: ...

setup_layers: Incomplete

def setup_layer(layer, setup_layers=...) -> None: ...
def tear_down(setup_layers=...) -> None: ...

class Zope2ServerRemote(RemoteLibrary):
    """Provides ``remote_zodb_setup`` and ``remote_zodb_teardown`` -keywords to
    allow explicit test isolation via remote library calls when server is set
    up with robot-server and tests are run by a separate pybot process.

    *WARNING* These keywords does not with zope.testrunner (yet).
    """
    def remote_zodb_setup(self, layer_dotted_name) -> None: ...
    def remote_zodb_teardown(self, layer_dotted_name) -> None: ...

class LazyStop:
    """Robot Framework listener for enabling lazy Zope2Server shutdown with
    normal Robot Framework test runner. Can be used to keep Zope2Server
    running between otherwise independent test suites with matching layer.

    Usage: pybot --listener plone.app.robotframework.LazyStop

    """

    ROBOT_LISTENER_API_VERSION: int
    def __init__(self) -> None: ...
    def close(self) -> None: ...

def setup(app):
    """Sphinx extension hook for enabling lazy Zope2Server shutdown with with
    ``sphinxcontrib-robotframework`` embedded test suites. Can be used to keep
    Zope2Server running between otherwise independent test suites with matching
    layer.

    Usage: extensions = ['plone.app.robotframework.server']

    """
