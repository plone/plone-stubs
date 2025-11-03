from _typeshed import Incomplete

logger: Incomplete
AUTOINCLUDE_ALLOW_MODULE_NOT_FOUND_ERROR: Incomplete
ALLOW_MODULE_NOT_FOUND_SET: Incomplete
ALLOW_MODULE_NOT_FOUND_ALL: bool

def load_z3c_packages(target: str = ""):
    """Load packages from the z3c.autoinclude.plugin entry points.

    After running the function, the packages have been imported.
    This returns a dictionary of package names and packages.
    """

def load_own_packages(target: str = ""):
    """Load packages from the plone.autoinclude.plugin entry points.

    After running the function, the packages have been imported.
    This returns a dictionary of package names and packages.

    Etnry points are like this:

        [plone.autoinclude]
        target = plone
        module = collective.mypackage

    Both options are optional, but you must have at least one,
    and it must have a value.
    """

def load_packages(target: str = ""):
    """Load packages from the autoinclude entry points.

    After running the function, the packages have been imported.
    This returns a dictionary of package names and packages.
    """

def get_zcml_file(module_name, zcml: str = "configure.zcml"): ...
def load_zcml_file(
    context,
    module_name,
    package=None,
    zcml: str = "configure.zcml",
    override: bool = False,
) -> None: ...
def load_configure(context, filename, dists) -> None: ...
def load_overrides(context, filename, dists) -> None: ...
