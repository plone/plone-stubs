from .basetool import IPloneBaseTool
from _typeshed import Incomplete
from zope.interface import Interface
from zope.interface import invariant

def dump_json_to_text(obj):
    """Encode an obj into a text"""

ROBOTS_TXT: str

def validate_json(value): ...

class IControlPanel(IPloneBaseTool):
    """Interface for the ControlPanel"""
    def registerConfiglet(
        id,
        name,
        action,
        condition: str = "",
        permission: str = "",
        category: str = "Plone",
        visible: int = 1,
        appId=None,
        imageUrl=None,
        description: str = "",
        REQUEST=None,
    ) -> None:
        """Registration of a Configlet"""
    def unregisterConfiglet(id) -> None:
        """unregister Configlet"""
    def unregisterApplication(appId) -> None:
        """unregister Application with all configlets"""
    def getGroupIds() -> None:
        """list of the group ids"""
    def getGroups() -> None:
        """list of groups as dicts with id and title"""
    def enumConfiglets(group=None) -> None:
        """lists the Configlets of a group, returns them as dicts by
        calling .getAction() on each of them"""

class IEditingSchema(Interface):
    available_editors: Incomplete
    default_editor: Incomplete
    ext_editor: Incomplete
    enable_link_integrity_checks: Incomplete
    lock_on_ttw_edit: Incomplete
    subjects_of_navigation_root: Incomplete

class ITagAttrPair(Interface):
    tags: Incomplete
    attributes: Incomplete

class TagAttrPair:
    tags: Incomplete
    attributes: Incomplete
    def __init__(self, tags: str = "", attributes: str = "") -> None: ...

class IFilterSchema(Interface):
    """Combined schema for the adapter lookup."""

    disable_filtering: Incomplete
    nasty_tags: Incomplete
    valid_tags: Incomplete
    custom_attributes: Incomplete

class ITinyMCELayoutSchema(Interface):
    """This interface defines the layout properties."""

    resizing: Incomplete
    autoresize: Incomplete
    inline: Incomplete
    editor_width: Incomplete
    editor_height: Incomplete
    content_css: Incomplete
    header_styles: Incomplete
    inline_styles: Incomplete
    block_styles: Incomplete
    alignment_styles: Incomplete
    table_styles: Incomplete
    formats: Incomplete

class ITinyMCEPluginSchema(Interface):
    """This interface defines the toolbar properties."""

    plugins: Incomplete
    menubar: Incomplete
    menu: Incomplete
    templates: Incomplete
    toolbar: Incomplete
    custom_plugins: Incomplete
    custom_buttons: Incomplete

ITinyMCELibrariesSchema = ITinyMCEPluginSchema

class ITinyMCEResourceTypesSchema(Interface):
    """This interface defines the resource types properties."""

    contains_objects: Incomplete
    image_objects: Incomplete
    entity_encoding: Incomplete

class ITinyMCEAdvancedSchema(Interface):
    """This interface defines the resource types properties."""

    other_settings: Incomplete

class ITinyMCESchema(
    ITinyMCELayoutSchema,
    ITinyMCEPluginSchema,
    ITinyMCEResourceTypesSchema,
    ITinyMCEAdvancedSchema,
):
    """TinyMCE Schema"""

class IMaintenanceSchema(Interface):
    days: Incomplete

class INavigationSchema(Interface):
    navigation_depth: Incomplete
    generate_tabs: Incomplete
    nonfolderish_tabs: Incomplete
    sort_tabs_on: Incomplete
    sort_tabs_reversed: Incomplete
    displayed_types: Incomplete
    filter_on_workflow: Incomplete
    workflow_states_to_show: Incomplete
    show_excluded_items: Incomplete
    root: Incomplete
    sitemap_depth: Incomplete
    parent_types_not_to_query: Incomplete

class ISearchSchema(Interface):
    enable_livesearch: Incomplete
    types_not_searched: Incomplete
    search_results_description_length: Incomplete
    sort_on: Incomplete
    search_show_images: Incomplete
    search_image_scale: Incomplete

class ISecuritySchema(Interface):
    enable_self_reg: Incomplete
    enable_user_pwd_choice: Incomplete
    enable_user_folders: Incomplete
    allow_anon_views_about: Incomplete
    use_email_as_login: Incomplete
    use_uuid_as_userid: Incomplete
    autologin_after_password_reset: Incomplete

class ISiteSchema(Interface):
    site_title: Incomplete
    site_logo: Incomplete
    site_favicon_mimetype: Incomplete
    site_favicon: Incomplete
    exposeDCMetaTags: Incomplete
    enable_sitemap: Incomplete
    webstats_head_js: Incomplete
    webstats_js: Incomplete
    display_publication_date_in_byline: Incomplete
    icon_visibility: Incomplete
    thumb_visibility: Incomplete
    no_thumbs_portlet: Incomplete
    no_thumbs_lists: Incomplete
    no_thumbs_summary: Incomplete
    no_thumbs_tables: Incomplete
    thumb_scale_portlet: Incomplete
    thumb_scale_listing: Incomplete
    thumb_scale_table: Incomplete
    thumb_scale_summary: Incomplete
    toolbar_position: Incomplete
    toolbar_logo: Incomplete
    robots_txt: Incomplete
    default_page: Incomplete
    roles_allowed_to_add_keywords: Incomplete

class IDateAndTimeSchema(Interface):
    """Controlpanel settings for date and time related settings."""

    portal_timezone: Incomplete
    available_timezones: Incomplete
    first_weekday: Incomplete

class ITypesSchema(Interface):
    """Controlpanel settings for the types settings."""

    types_use_view_action_in_listings: Incomplete
    redirect_links: Incomplete
    default_page_types: Incomplete

class IMailSchema(Interface):
    smtp_host: Incomplete
    smtp_port: Incomplete
    smtp_userid: Incomplete
    smtp_pass: Incomplete
    email_from_name: Incomplete
    email_from_address: Incomplete
    email_charset: Incomplete

class IMarkupSchema(Interface):
    default_type: Incomplete
    allowed_types: Incomplete
    markdown_extensions: Incomplete

class IUserGroupsSettingsSchema(Interface):
    many_groups: Incomplete
    many_users: Incomplete

def validate_twitter_username(value): ...

class ISocialMediaSchema(Interface):
    share_social_data: Incomplete
    twitter_username: Incomplete
    facebook_app_id: Incomplete
    facebook_username: Incomplete

class IImagingSchema(Interface):
    allowed_sizes: Incomplete
    quality: Incomplete
    highpixeldensity_scales: Incomplete
    quality_2x: Incomplete
    quality_3x: Incomplete
    picture_variants: Incomplete
    image_captioning: Incomplete

class ILoginSchema(Interface):
    auth_cookie_length: Incomplete
    verify_login_name: Incomplete
    allow_external_login_sites: Incomplete
    external_login_url: Incomplete
    external_logout_url: Incomplete
    external_login_iframe: Incomplete

class ILinkSchema(Interface):
    external_links_open_new_window: Incomplete
    mark_special_links: Incomplete

class IActionSchema(Interface):
    category: Incomplete
    title: Incomplete
    description: Incomplete
    i18n_domain: Incomplete
    url_expr: Incomplete
    available_expr: Incomplete
    permissions: Incomplete
    visible: Incomplete
    position: Incomplete
    modal: Incomplete

class INewActionSchema(Interface):
    category: Incomplete
    id: Incomplete
    @invariant
    def validate_category_id(data) -> None: ...

class IPloneControlPanelView(Interface):
    """A marker interface for views showing a controlpanel."""

class IPloneControlPanelForm(IPloneControlPanelView):
    """Forms using plone.app.controlpanel"""

class IConfigurationChangedEvent(Interface):
    """An event which is fired after a configuration setting has been changed."""

    context: Incomplete
    data: Incomplete
