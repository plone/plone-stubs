from _typeshed import Incomplete
from zope.interface import Interface

class IService(Interface):
    """ """

    method: Incomplete
    accept: Incomplete
    for_: Incomplete
    factory: Incomplete
    name: Incomplete
    layer: Incomplete
    permission: Incomplete

def serviceDirective(
    _context, method, accept, factory, for_, permission, layer=..., name: str = ""
) -> None: ...

class ICORSPolicyDirective(Interface):
    """Directive for defining CORS policies"""

    for_: Incomplete
    layer: Incomplete
    allow_origin: Incomplete
    allow_methods: Incomplete
    allow_headers: Incomplete
    expose_headers: Incomplete
    allow_credentials: Incomplete
    max_age: Incomplete

def cors_policy_directive(
    _context,
    allow_origin,
    allow_credentials,
    allow_methods=None,
    expose_headers=None,
    allow_headers=None,
    max_age=None,
    for_=...,
    layer=...,
) -> None: ...
