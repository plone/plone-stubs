from _typeshed import Incomplete
from plone.formwidget.namedfile.interfaces import (
    IScaleGenerateOnSave as IScaleGenerateOnSave,
)
from plone.formwidget.namedfile.utils import get_scale_infos as get_scale_infos
from plone.namedfile.field import INamedImageField as INamedImageField
from z3c.form.datamanager import AttributeField

ANNOTATION_KEY: str
ENVIRONMENT_KEY: str
logger: Incomplete

class NamedImageAttributeField(AttributeField):
    scale_generate_on_save: Incomplete
    def set(self, value) -> None: ...

def schedule_plone_scale_generate_on_save(context, request, fieldname) -> None: ...
def plone_scale_generate_on_save(event) -> None: ...
