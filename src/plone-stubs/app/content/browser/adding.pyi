from Acquisition import Implicit
from Products.Five.browser.adding import ContentAdding

class CMFAdding(Implicit, ContentAdding):
    """An adding view with a less silly next-url"""

    id: str
    def add(self, content): ...
    def nextURL(self): ...
