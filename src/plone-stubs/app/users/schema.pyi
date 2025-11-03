from _typeshed import Incomplete
from plone.formwidget.namedfile.widget import NamedImageWidget
from plone.schema.email import Email
from plone.schemaeditor.fields import FieldFactory
from zope import schema
from zope.interface import Interface

SCHEMA_ANNOTATION: str
SCHEMATA_KEY: str

def checkEmailAddress(value): ...

class ProtectedTextLine(schema.TextLine):
    """TextLine field which cannot be edited via schema editor"""

class ProtectedEmail(Email):
    """Email field which cannot be edited via schema editor"""

class NotEditableFieldFactory(FieldFactory):
    title: Incomplete
    def protected(self, field): ...

FullnameFieldFactory: Incomplete
EmailFieldFactory: Incomplete

class IUserDataSchema(Interface):
    """ """

    fullname: Incomplete
    email: Incomplete

class IRegisterSchema(Interface):
    username: Incomplete
    password: Incomplete
    password_ctl: Incomplete
    mail_me: Incomplete

class ICombinedRegisterSchema(IRegisterSchema, IUserDataSchema):
    """Collect all register fields under the same interface"""

class IAddUserSchema(Interface):
    groups: Incomplete

class PortraitWidget(NamedImageWidget):
    @property
    def download_url(self): ...

def PortraitFieldWidget(field, request): ...

class IRegistrationSettingsSchema(Interface):
    user_registration_fields: Incomplete

class IUserSchemaProvider(Interface): ...
