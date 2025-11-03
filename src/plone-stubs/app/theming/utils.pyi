from _typeshed import Incomplete
from lxml import etree

LOGGER: Incomplete

class NoRequest:
    """Fallback to enable querying for the policy adapter
    even in the absence of a proper IRequest."""

def theming_policy(request=None):
    """Primary policy accessor, uses pluggable ZCA lookup.
    Resolves into a IThemingPolicy adapter."""

class FailingFileProtocolResolver(etree.Resolver):
    """Resolver that fails for security when file: urls are tried.

    Note: an earlier version only checked for "file://", not "file:",
    and did not catch relative paths.
    """
    def resolve(self, system_url, public_id, context) -> None: ...

class FailingFileSystemResolver(etree.Resolver):
    """Resolver that fails for security when accessing the file system.

    Problem 1: none of the current plone.app.theming resolvers
    resolve file system paths, and yet they get resolved.
    So somewhere in etree there is a fallback.

    Problem 2: the InternalResolver of plone.app.theming can resolve paths
    internal in the Plone Site.  If that happens, then our failing resolver
    should not be called.  But the order in which resolvers are called,
    seems random, so we cannot rely on the InternalResolver being called first.

    So what do we do?

    Situation:
    - The Plone Site has a theme.html in the site root.
    - On the file system there is a file theme.html in the root.

    Possibilities when resolving /theme.html:

    A. The InternalResolver is called first, and resolves it correctly.
    B. Our FailingFileSystemResolver is called first,
       sees that the file exists, and raises an error.

    In this situation, the resolving would randomly work and not work.
    This seems unavoidable, but also seems a corner case
    which will not happen very often.

    In case the file does not exist on the file system,
    our resolver should return nothing.
    Then the InternalResolver or other resolvers can have a go.
    """
    def resolve(self, system_url, public_id, context) -> None: ...

class NetworkResolver(etree.Resolver):
    """Resolver for network urls"""
    def resolve(self, system_url, public_id, context): ...

class PythonResolver(etree.Resolver):
    """Resolver for python:// paths"""
    def resolve(self, system_url, public_id, context): ...

def resolvePythonURL(url):
    """Resolve the python resource url to it's path
    This can resolve python://dotted.package.name/file/path URLs to paths.
    """

class InternalResolver(etree.Resolver):
    """Resolver for internal absolute and relative paths (excluding protocol).
    If the path starts with a /, it will be resolved relative to the Plone
    site navigation root.
    """
    def resolve(self, system_url, public_id, context): ...

def getPortal():
    """Return the portal object"""

def findContext(request):
    """Find the context from the request"""

def findPathContext(path):
    """Find context given by physical path"""

def expandAbsolutePrefix(prefix):
    """Prepend the Plone site URL to the prefix if it starts with /"""

def getOrCreatePersistentResourceDirectory():
    """Obtain the 'theme' persistent resource directory, creating it if
    necessary.
    """

def createExpressionContext(context, request):
    """Create an expression context suitable for evaluating parameter
    expressions.
    """

def compileExpression(text):
    """Compile the given expression. The returned value is suitable for
    caching in a volatile attribute
    """

def isValidThemeDirectory(directory):
    """Determine if the given plone.resource directory is a valid theme
    directory
    """

def extractThemeInfo(zipfile, checkRules: bool = True):
    """Return an ITheme based on the information in the given zipfile.
    Will throw a ValueError if the theme directory does not contain a single
    top level directory or the rules file cannot be found.
    Set checkRules=False to disable the rules check.
    """

def getTheme(name, manifest=None, resources=None): ...
def getAvailableThemes():
    """Get a list of all ITheme's available in resource directories."""

def getThemeResources(format, defaults=None, filter=None, manifestFilename=...): ...
def getThemeFromResourceDirectory(resourceDirectory):
    """Return a Theme object from a resource directory"""

def getZODBThemes():
    """Get a list of ITheme's stored in the ZODB."""

def getCurrentTheme():
    """Get the name of the currently enabled theme"""

def isThemeEnabled(request, settings=None):
    """Determine if a theme is enabled for the given request"""

def applyTheme(theme) -> None:
    """Apply an ITheme"""

def createThemeFromTemplate(title, description, baseOn: str = "template"):
    """Create a new theme from the given title and description based on
    another theme resource directory
    """

def getParser(type, readNetwork):
    """Set up a parser for either rules, theme or compiler"""

def compileThemeTransform(
    rules,
    absolutePrefix=None,
    readNetwork: bool = False,
    parameterExpressions=None,
    runtrace: bool = False,
):
    """Prepare the theme transform by compiling the rules with the given options"""

def prepareThemeParameters(context, request, parameterExpressions, cache=None):
    """Prepare and return a dict of parameter expression values."""
