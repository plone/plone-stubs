from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.testing import Layer

class RemoteLibrary(SimpleItem):
    """Robot Framework remote library base for Plone

    http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#remote-library-interface
    https://github.com/robotframework/PythonRemoteServer/blob/master/src/robotremoteserver.py
    """
    def get_keyword_names(self):
        """Return names of the implemented keywords"""
    def get_keyword_arguments(self, name) -> None:
        """Return keyword arguments"""
    def get_keyword_documentation(self, name):
        """Return keyword documentation"""
    def run_keyword(self, name, args, kwargs={}):
        """Execute the specified keyword with given arguments."""

class RemoteLibraryLayer(Layer):
    defaultBases: Incomplete
    libraryBases: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
