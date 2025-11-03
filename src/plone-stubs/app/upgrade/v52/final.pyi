from _typeshed import Incomplete

logger: Incomplete
HAS_P_A_DISCUSSION: bool

def rebuild_redirections(context) -> None:
    """Rebuild the plone.app.redirector information.

    This initializes the date and manual information.
    """

def move_dotted_to_named_behaviors(context) -> None:
    """named behaviors are better then dotted behaviors > let's move them."""

KEYS_TO_CHANGE: Incomplete
OLD_PREFIX: str
NEW_PREFIX: str

def change_interface_on_lang_registry_records(context) -> None:
    """Interface Products.CMFPlone.interfaces.ILanguageSchema was moved to
    plone.i18n.interfaces."""

def to521(context) -> None:
    """5.2.0 -> 5.2.1"""

def to522(context) -> None:
    """5.2.1 -> 5.2.2"""

def move_markdown_transform_settings_to_registry(context) -> None:
    """Move markdown settings from portal_transforms to Plone registry."""

def migrate_record_from_ascii_to_bytes(field_name, iface, prefix=None) -> None:
    """Migrate a configuration registry record from ASCII to Bytes.

    Note: this is intended as a utility method that third party code can use.

    Sample use:

    from plone.base.interfaces import ISiteSchema
    migrate_record_from_ascii_to_bytes("plone.site_logo", ISiteSchema, prefix="plone")
    or:
    migrate_record_from_ascii_to_bytes("site_logo", ISiteSchema, prefix="plone")

    The interface is reregistered to get the new field definition.
    Note: this only works well if you have only *one* field that needs fixing.

    For the field name, using the full name including prefix is recommended.
    On Python 2 the full name is less needed, but on Python 3 it is.
    If you are not using a prefix when registering your interface,
    then automatically the identifier of your interface is used as prefix.
    In that case, you can use both of these:

    migrate_record_from_ascii_to_bytes("field_name", IMy)
    migrate_record_from_ascii_to_bytes(IMy.__identifier__ + ".field_name", IMy)
    """

def migrate_site_logo_from_ascii_to_bytes(context) -> None:
    """Site logo was ASCII field in 5.1, and Bytes field in 5.2.

    zope.schema.ASCII inherits from NativeString.
    With Python 2 this is the same as Bytes, but with Python 3 not:
    you get a WrongType error when saving the site-controlpanel.
    """

def secure_portal_setup_objects(context) -> None:
    """Make portal_setup objects accessible only to Manager/Owner.

    This matches the GenericSetup code for new logs and snapshots.
    See https://github.com/zopefoundation/Products.GenericSetup/pull/102
    """

def add_the_timezone_property(context) -> None:
    """Ensure that the portal_memberdata tool has the timezone property."""

def add_get_application_json_to_weak_caching(context) -> None:
    """Add GET application/json for content to weak caching.

    See https://github.com/plone/plone.rest/issues/73#issuecomment-1384298492
    We want to get this in the templateRulesetMapping setting of the registry:

        <element key="GET_application_json_">plone.content.folderView</element>
    """
