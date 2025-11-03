from _typeshed import Incomplete
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from plone.app.contentrules.browser.formhelper import EditForm
from plone.contentrules.rule.interfaces import IRuleConfiguration

class RuleAddForm(AddForm):
    """An add form for rules."""

    schema = IRuleConfiguration
    ignoreContext: bool
    label: Incomplete
    description: Incomplete
    def nextURL(self): ...
    def create(self, data): ...

class RuleAddFormView(ContentRuleFormWrapper):
    form = RuleAddForm

class RuleEditForm(EditForm):
    """An edit form for rules."""

    schema = IRuleConfiguration
    label: Incomplete
    description: Incomplete
    def nextURL(self): ...

class RuleEditFormView(ContentRuleFormWrapper):
    form = RuleEditForm
