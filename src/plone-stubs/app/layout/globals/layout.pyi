from _typeshed import Incomplete
from plone.memoize.view import memoize
from zope.publisher.browser import BrowserView

TEMPLATE_CLASSES: Incomplete

class LayoutPolicy(BrowserView):
    """A view that gives access to various layout related functions."""
    def mark_view(self, view) -> None:
        """Adds a marker interface to the view if it is "the" view for the
        context May only be called from a template.
        """
    def hide_columns(self, column_left, column_right):
        """Returns a CSS class matching the current column status."""
    def have_portlets(self, manager_name, view=None):
        """Determine whether a column should be shown. The left column is
        called plone.leftcolumn; the right column is called plone.rightcolumn.
        """
    @memoize
    def icons_visible(self):
        """Returns True if icons should be shown or False otherwise."""
    @memoize
    def thumb_visible(self):
        """Returns True if thumbs should be shown or False otherwise."""
    def bodyClass(self, template, view):
        """
        Returns the CSS class to be used on the body tag.

        Included body classes:
        - template-{}: template name
        - portaltype-{}: portal type
        - site-{}: navigation root
        - section-{}: first section name
        - subsection-{}: subsection names until configured depth
        - icons-on: show icons
        - icons-off: hide icons
        - thumbs-on: show thumbnails
        - thumbs-off: hide thumbnails
        - frontend: user without privileges, no admin interfaces shown
        - viewpermission-{}: minimum permission needed to view context
        - userrole-anonymous: anonymous user
        - userrole-{}: user roles for current user
        - plone-toolbar-left: toolbar is shown on left side
        - plone-toolbar-top: toolbar is shown on top
        - plone-toolbar-expanded: toolbar is in expanded state
        - plone-toolbar-left-expanded: left toolbar is expanded
        - plone-toolbar-top-expanded: top toolbar is expanded
        - plone-toolbar-left-default: left toolbar is not expanded
        - plone-toolbar-top-default: top toolbar is not expanded
        - pat-markspeciallinks: mark special links is set
        """

class DefaultBodyClasses:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_classes(self, template, view):
        """Default body classes adapter."""
