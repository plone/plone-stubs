from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

def import_from_name(module_name):
    """import and return a module by its name"""

def make_config_persistent(kwargs) -> None:
    """iterates on the given dictionary and replace list by persistent list,
    dictionary by persistent mapping.
    """

def make_config_nonpersistent(kwargs) -> None:
    """iterates on the given dictionary and replace ListClass by python List,
    and DictClass by python Dict
    """

VALIDATORS: Incomplete

class Transform(SimpleItem):
    """A transform is an external method with
    additional configuration information
    """

    meta_type: str
    meta_types: Incomplete
    all_meta_types: Incomplete
    manage_options: Incomplete
    manage_main: Incomplete
    manage_reloadTransform: Incomplete
    tr_widgets: Incomplete
    security: Incomplete
    __allow_access_to_unprotected_subobjects__: int
    id: Incomplete
    module: Incomplete
    def __init__(self, id, module, transform=None) -> None: ...
    @security.private
    def manage_beforeDelete(self, item, container) -> None: ...
    @security.public
    def get_documentation(self):
        """return transform documentation"""
    @security.public
    def convert(self, *args, **kwargs): ...
    @security.public
    def name(self):
        """return the name of the transform instance"""
    def get_parameters(self):
        """get transform's parameters names"""
    def get_parameter_value(self, key):
        """get value of a transform's parameter"""
    def get_parameter_infos(self, key):
        """get information about a parameter

        return a tuple (type, label, description [, type specific data])
        where type in (string, int, list, dict)
              label and description are two string describing the field
        there may be some additional elements specific to the type :
             (key label, value label) for the dict type
        """
    inputs: Incomplete
    output: Incomplete
    output_encoding: Incomplete
    def set_parameters(self, REQUEST=None, **kwargs) -> None:
        """set transform's parameters"""
    def reload(self) -> None:
        """reload the module where the transformation class is defined"""
    def preprocess_param(self, kwargs) -> None:
        """preprocess param fetched from an http post to handle
        optional dictionary
        """
