from _typeshed import Incomplete
from Acquisition import Acquired
from Acquisition import Explicit
from App.Management import Navigation
from OFS.role import RoleManager
from OFS.SimpleItem import Item
from Persistence import Persistent

manage_addExternalMethodForm: Incomplete

def manage_addExternalMethod(self, id, title, module, function, REQUEST=None):
    """Add an external method to a folder

    In addition to the standard object-creation arguments,
    'id' and title, the following arguments are defined:

        function -- The name of the python function. This can be a
          an ordinary Python function, or a bound method.

        module -- The name of the file containing the function
          definition.

        The module normally resides in the 'Extensions' directory.

        If the zope.conf directive 'extensions' was overriden, then
        it will specify where modules should reside.

        However, the file name may have a prefix of
        'product.', indicating that it should be found in a product
        directory.

        For example, if the module is: 'ACMEWidgets.foo', then an
        attempt will first be made to use the file
        'lib/python/Products/ACMEWidgets/Extensions/foo.py'. If this
        failes, then the file 'Extensions/ACMEWidgets.foo.py' will be
        used.
    """

class ExternalMethod(Item, Persistent, Explicit, RoleManager, Navigation):
    """Web-callable functions that encapsulate external python functions.

    The function is defined in an external file.  This file is treated
    like a module, but is not a module.  It is not imported directly,
    but is rather read and evaluated.  The file must reside in the
    'Extensions' subdirectory of the Zope installation, or in the directory
     specified by the 'extensions' directive in zope.conf, or in an
    'Extensions' subdirectory of a product directory.

    Due to the way ExternalMethods are loaded, it is not *currently*
    possible to use Python modules that reside in the 'Extensions'
    directory.  It is possible to load modules found in the
    'lib/python' directory of the Zope installation, or in
    packages that are in the 'lib/python' directory.

    """

    meta_type: str
    zmi_icon: str
    security: Incomplete
    __defaults__: Incomplete
    __code__: Incomplete
    ZopeTime = Acquired
    ZopeVersion = Acquired
    manage_page_header = Acquired
    getBookmarkableURLs = Acquired
    manage_options: Incomplete
    id: Incomplete
    def __init__(self, id, title, module, function) -> None: ...
    manage_main: Incomplete
    title: Incomplete
    def manage_edit(self, title, module, function, REQUEST=None):
        """Change the external method

        See the description of manage_addExternalMethod for a
        description of the arguments \'module\' and \'function\'.

        Note that calling \'manage_edit\' causes the "module" to be
        effectively reloaded.  This is useful during debugging to see
        the effects of changes, but can lead to problems of functions
        rely on shared global data.
        """
    def getFunction(self, reload: bool = False): ...
    def reloadIfChanged(self) -> None: ...
    def getFuncDefaults(self): ...
    def getFuncCode(self): ...
    def __call__(self, *args, **kw):
        """Call an ExternalMethod

        Calling an External Method is roughly equivalent to calling
        the original actual function from Python.  Positional and
        keyword parameters can be passed as usual.  Note however that
        unlike the case of a normal Python method, the "self" argument
        must be passed explicitly.  An exception to this rule is made
        if:

        - The supplied number of arguments is one less than the
          required number of arguments, and

        - The name of the function\'s first argument is \'self\'.

        In this case, the URL parent of the object is supplied as the
        first argument.
        """
    def function(self): ...
    def module(self): ...
    def filepath(self): ...
