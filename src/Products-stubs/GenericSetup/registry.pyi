from _typeshed import Incomplete
from Acquisition import Implicit
from xml.sax.handler import ContentHandler

logger: Incomplete

class _HandlerBase(ContentHandler): ...

class _ToolsetParser(_HandlerBase):
    security: Incomplete
    def __init__(self, encoding) -> None: ...
    def startElement(self, name, attrs) -> None: ...

class _ImportStepRegistryParser(_HandlerBase):
    security: Incomplete
    def __init__(self, encoding) -> None: ...
    def startElement(self, name, attrs) -> None: ...
    def characters(self, content) -> None: ...
    def endElement(self, name) -> None: ...

class _ExportStepRegistryParser(_HandlerBase):
    security: Incomplete
    def __init__(self, encoding) -> None: ...
    def startElement(self, name, attrs) -> None: ...
    def characters(self, content) -> None: ...
    def endElement(self, name) -> None: ...

class GlobalRegistryStorage:
    interfaceClass: Incomplete
    def __init__(self, interfaceClass) -> None: ...
    def keys(self): ...
    def values(self): ...
    def get(self, key): ...
    def __setitem__(self, id, info) -> None: ...
    def __delitem__(self, id) -> None: ...
    def clear(self) -> None: ...

class BaseStepRegistry(Implicit):
    security: Incomplete
    def __init__(self, store=None) -> None: ...
    def listSteps(self):
        """Return a list of registered step IDs."""
    def getStepMetadata(self, key, default=None):
        """Return a mapping of metadata for the step identified by 'key'.

        o Return 'default' if no such step is registered.

        o The 'handler' metadata is available via 'getStep'.
        """
    def listStepMetadata(self):
        """Return a sequence of mappings describing registered steps.

        o Mappings will be ordered alphabetically.
        """
    def generateXML(self, encoding: str = "utf-8"):
        """Return a round-trippable XML representation of the registry.

        o 'handler' values are serialized using their dotted names.
        """
    @security.private
    def getStep(self, key, default=None):
        """Return the I(Export|Import)Plugin registered for 'key'.

        o Return 'default' if no such step is registered.
        """
    @security.private
    def unregisterStep(self, id) -> None: ...
    @security.private
    def clear(self) -> None: ...
    @security.private
    def parseXML(self, text, encoding: str = "utf-8"):
        """Parse 'text'."""

class ImportStepRegistry(BaseStepRegistry):
    """Manage knowledge about steps to create / configure site.

    o Steps are composed together to define a site profile.
    """

    security: Incomplete
    RegistryParser: Incomplete
    def sortSteps(self):
        """Return a sequence of registered step IDs

        o Sequence is sorted topologically by dependency, with the dependent
          steps *after* the steps they depend on.
        """
    def checkComplete(self):
        """Return a sequence of ( node, edge ) tuples for unsatisifed deps."""
    @security.private
    def registerStep(
        self,
        id,
        version=None,
        handler=None,
        dependencies=(),
        title=None,
        description=None,
    ) -> None:
        """Register a setup step.

        o 'id' is a unique name for this step,

        o 'version' is a string for comparing versions, it is preferred to
          be a yyyy/mm/dd-ii formatted string (date plus two-digit
          ordinal).  when comparing two version strings, the version with
          the lower sort order is considered the older version.

          - Newer versions of a step supplant older ones.

          - Attempting to register an older one after a newer one results
            in a KeyError.

        o 'handler' is the dottoed name of a handler which should implement
           IImportPlugin.

        o 'dependencies' is a tuple of step ids which have to run before
          this step in order to be able to run at all. Registration of
          steps that have unmet dependencies are deferred until the
          dependencies have been registered.

        o 'title' is a one-line UI description for this step.
          If None, the first line of the documentation string of the handler
          is used, or the id if no docstring can be found.

        o 'description' is a one-line UI description for this step.
          If None, the remaining line of the documentation string of
          the handler is used, or default to ''.
        """

class ExportStepRegistry(BaseStepRegistry):
    """Registry of known site-configuration export steps.

    o Each step is registered with a unique id.

    o When called, with the portal object passed in as an argument,
      the step must return a sequence of three-tuples,
      ( 'data', 'content_type', 'filename' ), one for each file exported
      by the step.

      - 'data' is a string containing the file data;

      - 'content_type' is the MIME type of the data;

      - 'filename' is a suggested filename for use when downloading.

    """

    security: Incomplete
    RegistryParser: Incomplete
    @security.private
    def registerStep(self, id, handler, title=None, description=None) -> None:
        """Register an export step.

        o 'id' is the unique identifier for this step

        o 'handler' is the dottoed name of a handler which should implement
           IImportPlugin.

        o 'title' is a one-line UI description for this step.
          If None, the first line of the documentation string of the step
          is used, or the id if no docstring can be found.

        o 'description' is a one-line UI description for this step.
          If None, the remaining line of the documentation string of
          the step is used, or default to ''.
        """

class ToolsetRegistry(Implicit):
    """Track required / forbidden tools."""

    security: Incomplete
    def __init__(self) -> None: ...
    def listForbiddenTools(self):
        """See IToolsetRegistry."""
    def addForbiddenTool(self, tool_id) -> None:
        """See IToolsetRegistry."""
    def listRequiredTools(self):
        """See IToolsetRegistry."""
    def getRequiredToolInfo(self, tool_id):
        """See IToolsetRegistry."""
    def listRequiredToolInfo(self):
        """See IToolsetRegistry."""
    def addRequiredTool(self, tool_id, dotted_name) -> None:
        """See IToolsetRegistry."""
    def generateXML(self, encoding: str = "utf-8"):
        """Pseudo API."""
    def parseXML(self, text, encoding: str = "utf-8") -> None:
        """Pseudo-API"""
    @security.private
    def clear(self) -> None: ...

class ProfileRegistry(Implicit):
    """Track registered profiles."""

    security: Incomplete
    def __init__(self) -> None: ...
    def getProfileInfo(self, profile_id, for_=None):
        """See IProfileRegistry."""
    def listProfiles(self, for_=None):
        """See IProfileRegistry."""
    def listProfileInfo(self, for_=None):
        """See IProfileRegistry."""
    def registerProfile(
        self,
        name,
        title,
        description,
        path,
        product=None,
        profile_type=...,
        for_=None,
        pre_handler=None,
        post_handler=None,
    ) -> None:
        """See IProfileRegistry."""
    def unregisterProfile(self, name, product=None) -> None: ...
    @security.private
    def clear(self) -> None: ...
