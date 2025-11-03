from _typeshed import Incomplete
from plone.supermodel.model import Schema
from zope.interface import Interface

log: Incomplete

def copySchemaAttrs(sch): ...

class IEmpty(Schema): ...

class IHomePageSchema(Interface):
    """ """

    home_page: Incomplete

class IDescriptionSchema(Interface):
    """ """

    description: Incomplete

class ILocationSchema(Interface):
    """ """

    location: Incomplete

class IPortraitSchema(Interface):
    """ """

    portrait: Incomplete

def upgrade_to_ttw(context) -> None: ...
