from _typeshed import Incomplete
from zope.interface import Interface

class IBatch(Interface):
    """A batch splits up a large number of items over multiple pages"""

    size: Incomplete
    firstpage: Incomplete
    lastpage: Incomplete
    items_not_on_page: Incomplete
    multiple_pages: Incomplete
    has_next: Incomplete
    has_previous: Incomplete
    previouspage: Incomplete
    nextpage: Incomplete
    next_item_count: Incomplete
    navlist: Incomplete
    show_link_to_first: Incomplete
    show_link_to_last: Incomplete
    second_page_not_in_navlist: Incomplete
    before_last_page_not_in_navlist: Incomplete
    islastpage: Incomplete
    previous_pages: Incomplete
    next_pages: Incomplete
