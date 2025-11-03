from _typeshed import Incomplete
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

search_base_uid_source: Incomplete
PLMF: Incomplete

class ICalendarPortlet(IPortletDataProvider):
    """A portlet displaying a calendar"""

    state: Incomplete
    search_base_uid: Incomplete

class Assignment(base.Assignment):
    title: Incomplete
    state: Incomplete
    search_base_uid: Incomplete
    def __init__(self, state=None, search_base_uid=None) -> None: ...

class Renderer(base.Renderer):
    render: Incomplete
    @property
    def search_base(self): ...
    @property
    def search_base_path(self): ...
    calendar_url: Incomplete
    prev_query: Incomplete
    next_query: Incomplete
    cal: Incomplete
    month_name: Incomplete
    weekdays: Incomplete
    def update(self) -> None: ...
    def year_month_display(self):
        """Return the year and month to display in the calendar."""
    def get_previous_month(self, year, month): ...
    def get_next_month(self, year, month): ...
    def date_events_url(self, date): ...
    @property
    def cal_data(self):
        """Calendar iterator over weeks and days of the month to display."""
    def nav_pattern_options(self, year, month): ...
    @property
    def hash(self): ...

class AddForm(base.AddForm):
    schema = ICalendarPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(base.EditForm):
    schema = ICalendarPortlet
    label: Incomplete
    description: Incomplete
