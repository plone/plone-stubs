from .WorkflowUIMixin import WorkflowUIMixin
from _typeshed import Incomplete
from OFS.Folder import Folder

def checkId(id): ...

class DCWorkflowDefinition(WorkflowUIMixin, Folder):
    """
    This class is the workflow engine and the container for the
    workflow definition.
    UI methods are in WorkflowUIMixin.
    """

    title: str
    description: str
    state_var: str
    initial_state: Incomplete
    states: Incomplete
    transitions: Incomplete
    variables: Incomplete
    worklists: Incomplete
    scripts: Incomplete
    permissions: Incomplete
    groups: Incomplete
    roles: Incomplete
    creation_guard: Incomplete
    manager_bypass: int
    manage_options: Incomplete
    security: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    @security.private
    def getCatalogVariablesFor(self, ob):
        """
        Allows this workflow to make workflow-specific variables
        available to the catalog, making it possible to implement
        worklists in a simple way.
        Returns a mapping containing the catalog variables
        that apply to ob.
        """
    @security.private
    def listObjectActions(self, info):
        """
        Allows this workflow to
        include actions to be displayed in the actions box.
        Called only when this workflow is applicable to
        info.object.
        Returns the actions to be displayed to the user.
        """
    @security.private
    def listGlobalActions(self, info):
        """
        Allows this workflow to
        include actions to be displayed in the actions box.
        Called on every request.
        Returns the actions to be displayed to the user.
        """
    @security.private
    def isActionSupported(self, ob, action, **kw):
        """
        Returns a true value if the given action name
        is possible in the current state.
        """
    @security.private
    def doActionFor(self, ob, action, comment: str = "", **kw) -> None:
        """
        Allows the user to request a workflow action.  This method
        must perform its own security checks.
        """
    @security.private
    def isInfoSupported(self, ob, name):
        """
        Returns a true value if the given info name is supported.
        """
    @security.private
    def getInfoFor(self, ob, name, default):
        """
        Allows the user to request information provided by the
        workflow.  This method must perform its own security checks.
        """
    @security.private
    def allowCreate(self, container, type_name):
        """Returns true if the user is allowed to create a workflow instance.

        The object passed to the guard is the prospective container.
        """
    @security.private
    def notifyCreated(self, ob) -> None:
        """Notifies this workflow after an object has been created and added."""
    @security.private
    def notifyBefore(self, ob, action) -> None:
        """
        Notifies this workflow of an action before it happens,
        allowing veto by exception.  Unless an exception is thrown, either
        a notifySuccess() or notifyException() can be expected later on.
        The action usually corresponds to a method name.
        """
    @security.private
    def notifySuccess(self, ob, action, result) -> None:
        """
        Notifies this workflow that an action has taken place.
        """
    @security.private
    def notifyException(self, ob, action, exc) -> None:
        """
        Notifies this workflow that an action failed.
        """
    @security.private
    def updateRoleMappingsFor(self, ob):
        """Changes the object permissions according to the current state."""
