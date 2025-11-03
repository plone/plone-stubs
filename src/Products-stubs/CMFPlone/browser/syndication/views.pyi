from _typeshed import Incomplete
from Products.Five import BrowserView
from z3c.form import form
from zope.cachedescriptors.property import Lazy as lazy_property

class FeedView(BrowserView):
    content_type: str
    def feed(self): ...
    def __call__(self): ...

class SearchFeedView(FeedView):
    def feed(self): ...
    def __call__(self): ...

class NewsMLFeedView(FeedView):
    content_type: str
    @lazy_property
    def current_date(self): ...
    def duid(self, item, value): ...
    def get_image(self, item): ...

class SettingsForm(form.EditForm):
    label: Incomplete
    description: Incomplete
    fields: Incomplete
    status: Incomplete
    def handleSave(self, action) -> None: ...

SettingsFormView: Incomplete
