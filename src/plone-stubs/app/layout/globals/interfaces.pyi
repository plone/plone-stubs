from zope.interface import Interface

class IInterfaceInformation(Interface):
    """A view that gives information about interfaces provided by its context"""
    def provides(self, dotted_name) -> None:
        """Given an interface dotted name, determine if the context provides
        this interface.
        """
    def class_provides(self, dotted_name) -> None:
        """Given an interface dotted name, determine if the context's class
        provides this interface.
        """
    def names_and_descriptions(self, dotted_name, all) -> None:
        """Returns a list of pairs (name, description) for a given
        interface"""
    def get_interfaces(self) -> None:
        """Returns the list of interfaces which are implemented by the object"""
    def get_base_interface(self) -> None:
        """Returns all base interfaces of an object but no direct interfaces

        Base interfaces are the interfaces which are the super interfaces of
        the direct interfaces
        """
    def get_interface_informations(self, iface) -> None:
        """Gets all useful information from an iface

        * name
        * dotted name
        * trimmed doc string
        * base interfaces
        * methods with signature and trimmed doc string
        * attributes with trimemd doc string
        """

class ILayoutPolicy(Interface):
    """A view that gives access to various layout related functions."""
    def mark_view(self, view) -> None:
        """Adds a marker interface to the view if it is "the" view for the
        context May only be called from a template.
        """
    def hide_columns(self, column_left, column_right) -> None:
        """Returns a CSS class matching the current column status."""
    def have_portlets(self, manager_name, view=None) -> None:
        """Determine whether a column should be shown. The left column is
        called plone.leftcolumn; the right column is called plone.rightcolumn.
        """
    def icons_visible(self) -> None:
        """Returns True if icons should be shown or False otherwise."""
    def bodyClass(self, template, view) -> None:
        """Returns the CSS class to be used on the body tag."""

class ITools(Interface):
    """A view that gives access to common tools"""
    def actions(self) -> None:
        """The portal_actions tool"""
    def catalog(self) -> None:
        """The portal_catalog tool"""
    def membership(self) -> None:
        """The portal_membership tool"""
    def types(self) -> None:
        """The portal_types tool"""
    def url(self) -> None:
        """The portal_url tool"""
    def workflow(self) -> None:
        """The portal_workflow tool"""

class IPortalState(Interface):
    """A view that gives access to the current state of the portal"""
    def portal(self) -> None:
        """The portal object"""
    def portal_title(self) -> None:
        """The title of the portal object"""
    def portal_url(self) -> None:
        """The URL of the portal object"""
    def navigation_root(self) -> None:
        """The navigation root object"""
    def navigation_root_title(self) -> None:
        """The title of the navigation root object"""
    def navigation_root_path(self) -> None:
        """path of the navigation root"""
    def navigation_root_url(self) -> None:
        """The URL of the navigation root"""
    def default_language(self) -> None:
        """The default language in the portal"""
    def language(self) -> None:
        """The current language"""
    def locale(self) -> None:
        """Get the current locale"""
    def is_rtl(self) -> None:
        """Whether or not the portal is being viewed in an RTL language"""
    def member(self) -> None:
        """The current authenticated member"""
    def anonymous(self) -> None:
        """Whether or not the current member is Anonymous"""
    def friendly_types(self) -> None:
        """Get a list of portal types considered "end user" types"""

class IContextState(Interface):
    """A view that gives access to the state of the current context"""
    def current_page_url(self) -> None:
        """The URL to the current page, including template and query string."""
    def current_base_url(self) -> None:
        """The current "actual" URL from the request, excluding the query
        string.
        """
    def canonical_object(self) -> None:
        """The current "canonical" object.

        That is, the current object unless this object is the default page
        in its folder, in which case the folder is returned.
        """
    def canonical_object_url(self) -> None:
        """The URL to the current "canonical" object.

        That is, the current object unless this object is the default page
        in its folder, in which case the folder is returned.
        """
    def view_url(self) -> None:
        """URL to use for viewing

        Files and Images get downloaded when they are directly
        called, instead of with /view appended.  We want to avoid that.
        """
    def view_template_id(self) -> None:
        """The id of the view template of the context"""
    def is_view_template(self) -> None:
        """Return True if the current URL (in the request) refers to the
        standard "view" of the context (i.e. the "view" tab).
        """
    def object_url(self) -> None:
        """The URL of the current object"""
    def object_title(self) -> None:
        """The prettified title of the current object"""
    def workflow_state(self) -> None:
        """The workflow state of the current object"""
    def parent(self) -> None:
        """The direct parent of the current object"""
    def folder(self) -> None:
        """The current canonical folder"""
    def is_folderish(self) -> None:
        """True if this is a folderish object, structural or not"""
    def is_structural_folder(self) -> None:
        """True if this is a structural folder"""
    def is_default_page(self) -> None:
        """True if this is the default page of its folder"""
    def is_portal_root(self) -> None:
        """True if this is the portal or the default page in the portal"""
    def is_editable(self) -> None:
        """Whether or not the current object is editable"""
    def is_locked(self) -> None:
        """Whether or not the current object is locked"""
    def is_toolbar_visible(self) -> None:
        """Whether toolbar is visible or not in the actual context"""
    def actions(self, category) -> None:
        """The filtered actions in the context. You can restrict the actions
        to just one category.
        """
    def portlet_assignable(self) -> None:
        """Whether or not the context is capable of having locally assigned
        portlets.
        """

class IViewView(Interface):
    """Marker interface which specifies that the current view is, in fact,
    a canonical "view" of the object, e.g. what may go on the "view" tab.
    """

class IBodyClassAdapter(Interface):
    """Adapter interface for retrieving extra body classes."""
