from Products.Five.browser import BrowserView

def get_default_page(context):
    """Given a folderish item, find out if it has a default-page using
    the following lookup rules:

        1. A content object called 'index_html' wins
        2. Else check for IBrowserDefault, either if the container implements
           it or if an adapter exists. In both cases fetch its FTI and either
           take it if it implements IDynamicViewTypeInformation or adapt it to
           IDynamicViewTypeInformation. call getDefaultPage on the implementer
           and take value if given.
        3. Else, look up the attribute default_page on the object, without
           acquisition in place
        3.1 look for a content in the container with the id, no acquisition!
        3.2 look for a content at portal, with acquisition
        4. Else, look up the property plone.default_page in the registry for
           magic ids and test these

    The id of the first matching item is then used to lookup a translation
    and if found, its id is returned. If no default page is set, None is
    returned. If a non-folderish item is passed in, return None always.
    """

def is_default_page(container, obj):
    """Finds out if the given obj is the default page in its parent folder.

    Only considers explicitly contained objects, either set as index_html,
    with the default_page property, or using IBrowserDefault.
    """

class DefaultPageView(BrowserView):
    def isDefaultPage(self, obj): ...
    def getDefaultPage(self): ...

def check_default_page_via_view(obj, request): ...
def get_default_page_via_view(obj, request): ...
