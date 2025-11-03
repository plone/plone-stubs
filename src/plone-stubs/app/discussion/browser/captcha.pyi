from _typeshed import Incomplete
from persistent import Persistent
from plone.z3cform.fieldsets import extensible

class Captcha(Persistent):
    """Captcha input field."""

    captcha: str

class CaptchaExtender(extensible.FormExtender):
    """Extends the comment form with a Captcha. This Captcha extender is only
    registered when a plugin is installed that provides the
    "plone.app.discussion-captcha" feature.
    """

    fields: Incomplete
    context: Incomplete
    request: Incomplete
    form: Incomplete
    captcha: Incomplete
    isAnon: Incomplete
    def __init__(self, context, request, form) -> None: ...
    def update(self) -> None: ...
