from plone.autoform.interfaces import FORM_NAMESPACE
from plone.autoform.interfaces import FORM_PREFIX
from plone.autoform.interfaces import SECURITY_NAMESPACE
from plone.autoform.interfaces import SECURITY_PREFIX

class FormSchema:
    """Support the form: namespace in model definitions."""

    namespace = FORM_NAMESPACE
    prefix = FORM_PREFIX
    def read(self, fieldNode, schema, field) -> None: ...
    def write(self, fieldNode, schema, field) -> None: ...

class SecuritySchema:
    """Support the security: namespace in model definitions."""

    namespace = SECURITY_NAMESPACE
    prefix = SECURITY_PREFIX
    def read(self, fieldNode, schema, field) -> None: ...
    def write(self, fieldNode, schema, field) -> None: ...
