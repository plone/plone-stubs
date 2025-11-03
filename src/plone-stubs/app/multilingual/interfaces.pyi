from _typeshed import Incomplete
from plone.app.z3cform.interfaces import IPloneFormLayer
from plone.i18n.interfaces import ILanguageSchema
from zope.interface import Interface

SHARED_NAME: str
LANGUAGE_INDEPENDENT: str
ATTRIBUTE_NAME: str
NOTG: str

class ILanguageRootFolder(Interface):
    """Language Root Folder content type interface"""

class ILanguageIndependentFolder(Interface):
    """Language Independent Folder for content shared between languages"""

class ITranslatable(Interface):
    """Marker interface for content types that support translation"""

class ITranslationFactory(Interface):
    """Adapts ITranslated and is capable of returning
    a translation clone to be added.
    """
    def __call__(language) -> None:
        """Create a clone of the context
        for translation to the given language
        """

class ITranslationLocator(Interface):
    """Find a parent folder for a translation.
    Adapts ITranslated.
    """
    def __call__(language) -> None:
        """Return a parent folder into which a new translation can be added"""

class ITranslationIdChooser(Interface):
    """Find a valid id for a translation
    Adapts ITranslated.
    """
    def __call__(parent, language) -> None:
        """Return a valid id for the translation"""

class ITranslationCloner(Interface):
    """Subscription adapters to perform various aspects of cloning an object.
    Allows componentisation of things like workflow history cloning.
    Adapts ITranslated.
    """
    def __call__(object) -> None:
        """Update the translation copy that is being constructed"""

class ITranslationManager(Interface):
    def add_translation(object, intid) -> None:
        """
        create the translated content and register the translation
        """
    def remove_translation(language) -> None:
        """
        remove translation if exists (unregister the translation)
        """
    def get_translation(language) -> None:
        """
        get translation (translated object) if exists
        """
    def get_restricted_translation(language) -> None:
        """
        get translation (translated object) if exists and permitted
        """
    def get_translations() -> None:
        """
        get all the translated objects (including the context)
        """
    def get_restricted_translations() -> None:
        """
        get all the translated objects (including the context) if permitted
        """
    def get_translated_languages() -> None:
        """
        get a list of the translated languages
        (language-code like 'en', 'it' etc. )
        """
    def register_translation(language, content) -> None:
        """
        register an existing content as translation
        for context
        """
    def update() -> None:
        """
        update the item registered in the canonical
        check that there aren't two translations on the same language
        (used for changing the contexts language)
        """
    def query_canonical() -> None:
        """
        query if there is an canonical for the context
        used for migration
        """

class ILanguageIndependentFieldsManager(Interface):
    context: Incomplete
    def copy_fields(translation) -> None:
        """Copy language independent fields to translation."""

class IMutableTG(Interface):
    """Adapt an object to this interface to manage the TG of an object

    Be sure of what you are doing. Translation Group (TG) is supposed to
    be stable and widely used
    """
    def get() -> None:
        """Return the TG of the context"""
    def set(tg) -> None:
        """Set the unique id of the context with the tg value."""

class ITG(Interface):
    """Abstract representation of a Translation Group (TG).

    Adapt an object to this interface to obtain its UUID. Adaptation will
    fail if the object does not have a TG (yet).
    """

class IPloneAppMultilingualInstalled(IPloneFormLayer):
    """layer inherits from PloneFormLayer for better LIF widget overriding"""

selector_policies: Incomplete

class IMultiLanguageExtraOptionsSchema(ILanguageSchema):
    """Interface for language extra options - control panel fieldset"""

    filter_content: Incomplete
    redirect_babel_view: Incomplete
    bypass_languageindependent_field_permission_check: Incomplete
    buttons_babel_view_up_to_nr_translations: Incomplete
    google_translation_key: Incomplete
    selector_lookup_translations_policy: Incomplete
