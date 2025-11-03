from _typeshed import Incomplete
from OFS.Folder import Folder
from Products.CMFCore.ActionProviderBase import ActionProviderBase
from Products.CMFCore.utils import UniqueObject

class TransformTool(UniqueObject, ActionProviderBase, Folder):
    id: str
    meta_type: Incomplete
    isPrincipiaFolderish: int
    meta_types: Incomplete
    all_meta_types: Incomplete
    manage_addTransformForm: Incomplete
    manage_addTransformsChainForm: Incomplete
    manage_cacheForm: Incomplete
    manage_editTransformationPolicyForm: Incomplete
    manage_reloadAllTransforms: Incomplete
    manage_options: Incomplete
    security: Incomplete
    max_sec_in_cache: Incomplete
    def __init__(self, policies=None, max_sec_in_cache: int = 3600) -> None: ...
    @security.private
    def unregisterTransform(self, name) -> None:
        """unregister a transform
        name is the name of a registered transform
        """
    @security.public
    def convertTo(
        self,
        target_mimetype,
        orig,
        data=None,
        object=None,
        usedby=None,
        context=None,
        **kwargs,
    ):
        """Convert orig to a given mimetype

        * orig is a native string

        * data an optional IDataStream object. If None a new datastream will be
        created and returned

        * optional object argument is the object on which is bound the data.
        If present that object will be used by the engine to bound cached data.

        * additional arguments (kwargs) will be passed to the transformations.
        Some usual arguments are : filename, mimetype, encoding

        return an object implementing IDataStream or None if no path has been
        found.
        """
    @security.public
    def convertToData(
        self,
        target_mimetype,
        orig,
        data=None,
        object=None,
        usedby=None,
        context=None,
        **kwargs,
    ): ...
    @security.public
    def convert(self, name, orig, data=None, context=None, **kwargs): ...
    def __call__(self, name, orig, data=None, context=None, **kwargs): ...
    @security.private
    def manage_afterAdd(self, item, container) -> None:
        """overload manage_afterAdd to finish initialization when the
        transform tool is added
        """
    def manage_addTransform(self, id, module, REQUEST=None) -> None:
        """add a new transform to the tool"""
    def manage_addTransformsChain(self, id, description, REQUEST=None) -> None:
        """add a new transform to the tool"""
    def manage_setCacheValidityTime(self, seconds, REQUEST=None) -> None:
        """set  the lifetime of cached data in seconds"""
    def reloadTransforms(self, ids=()):
        """reload transforms with the given ids
        if no ids, reload all registered transforms

        return a list of (transform_id, transform_module) describing reloaded
        transforms
        """
    def manage_addPolicy(
        self, output_mimetype, required_transforms, REQUEST=None
    ) -> None:
        """add a policy for a given output mime types"""
    def manage_delPolicies(self, outputs, REQUEST=None) -> None:
        """remove policies for given output mime types"""
    def listPolicies(self):
        """return the list of defined policies

        a policy is a 2-uple (output_mime_type, [list of required transforms])
        """
    @security.private
    def registerTransform(self, transform) -> None:
        """register a new transform

        transform isn't a Zope Transform (the wrapper) but the wrapped
        transform the persistence wrapper will be created here
        """
    def ZopeFind(self, *args, **kwargs):
        """Don't break ZopeFind feature when a transform can't be loaded"""
    def objectItems(self, *args, **kwargs):
        """Don't break ZopeFind feature when a transform can't be loaded"""
    def listAvailableTextInputs(self):
        """Returns a list of mimetypes that can be used as input for textfields
        by building a list of the inputs beginning with "text/" of all
        transforms.
        """
