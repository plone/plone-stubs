from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from plone.memoize.view import memoize
from plone.supermodel import model
from z3c.form import form

class IMemberSearchSchema(model.Schema):
    """Provide schema for member search."""

    login: Incomplete
    email: Incomplete
    fullname: Incomplete

def extractCriteriaFromRequest(criteria):
    """Takes a dictionary of z3c.form data and sanitizes it to fit
    for a pas member search.
    """

class MemberSearchForm(AutoExtensibleForm, form.Form):
    """This search form enables you to find users by specifying one or more
    search criteria.
    """

    schema = IMemberSearchSchema
    ignoreContext: bool
    label: Incomplete
    description: Incomplete
    template: Incomplete
    enableCSRFProtection: bool
    formErrorsMessage: Incomplete
    submitted: bool
    @property
    @memoize
    def listing_allowed(self):
        """
        Check if the user has the necessary "List Portal Members" permissions
        to view the list of search results.
        """
    @property
    def results(self):
        """
        Retrieve, merge, and sort the list of results based on search criteria.

        This is based on the methods previously defined in the
        Products.PlonePAS.browser.search module.
        """
    status: Incomplete
    def handleApply(self, action) -> None: ...
