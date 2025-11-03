from _typeshed import Incomplete
from plone.app.content.browser.contents import ContentsBaseAction

class OrderContentsBaseAction(ContentsBaseAction):
    def getOrdering(self): ...

class ItemOrderActionView(OrderContentsBaseAction):
    success_msg: Incomplete
    failure_msg: Incomplete
    errors: Incomplete
    def __call__(self): ...

class RearrangeActionView(OrderContentsBaseAction):
    success_msg: Incomplete
    failure_msg: Incomplete
    errors: Incomplete
    def __call__(self): ...
