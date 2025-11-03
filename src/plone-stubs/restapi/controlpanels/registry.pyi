from _typeshed import Incomplete
from plone.restapi.controlpanels import RegistryConfigletPanel
from Products.CMFPlone.interfaces.controlpanel import IDateAndTimeSchema
from Products.CMFPlone.interfaces.controlpanel import IEditingSchema
from Products.CMFPlone.interfaces.controlpanel import IImagingSchema
from Products.CMFPlone.interfaces.controlpanel import ILanguageSchema
from Products.CMFPlone.interfaces.controlpanel import IMailSchema
from Products.CMFPlone.interfaces.controlpanel import IMarkupSchema
from Products.CMFPlone.interfaces.controlpanel import INavigationSchema
from Products.CMFPlone.interfaces.controlpanel import ISearchSchema
from Products.CMFPlone.interfaces.controlpanel import ISecuritySchema
from Products.CMFPlone.interfaces.controlpanel import ISiteSchema
from Products.CMFPlone.interfaces.controlpanel import ISocialMediaSchema
from Products.CMFPlone.interfaces.controlpanel import IUserGroupsSettingsSchema

PLONE_6: Incomplete

class DateTimeControlpanel(RegistryConfigletPanel):
    schema = IDateAndTimeSchema
    configlet_id: str
    configlet_category_id: str

class LanguageControlpanel(RegistryConfigletPanel):
    schema = ILanguageSchema
    configlet_id: str
    configlet_category_id: str

class MailControlpanel(RegistryConfigletPanel):
    schema = IMailSchema
    configlet_id: str
    configlet_category_id: str

class NavigationControlpanel(RegistryConfigletPanel):
    schema = INavigationSchema
    configlet_id: str
    configlet_category_id: str

class SiteControlpanel(RegistryConfigletPanel):
    schema = ISiteSchema
    configlet_id: str
    configlet_category_id: str

class SearchControlpanel(RegistryConfigletPanel):
    schema = ISearchSchema
    configlet_id: str
    configlet_category_id: str

class SocialMediaControlpanel(RegistryConfigletPanel):
    schema = ISocialMediaSchema
    configlet_id: str
    configlet_category_id: str

class EditingControlpanel(RegistryConfigletPanel):
    schema = IEditingSchema
    configlet_id: str
    configlet_category_id: str

class ImagingControlpanel(RegistryConfigletPanel):
    schema = IImagingSchema
    configlet_id: str
    configlet_category_id: str

class MarkupControlpanel(RegistryConfigletPanel):
    schema = IMarkupSchema
    configlet_id: str
    configlet_category_id: str

class SecurityControlpanel(RegistryConfigletPanel):
    schema = ISecuritySchema
    configlet_id: str
    configlet_category_id: str

class UserGroupControlpanel(RegistryConfigletPanel):
    schema = IUserGroupsSettingsSchema
    configlet_id: str
    configlet_category_id: str
    title: Incomplete
    group: Incomplete
