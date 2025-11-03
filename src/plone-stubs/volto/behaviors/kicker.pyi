from _typeshed import Incomplete
from plone.supermodel import model

class IKicker(model.Schema):
    head_title: Incomplete

class IHeadTitle(IKicker):
    """alias for backwards-compatibility"""
