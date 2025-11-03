from Products.Five.browser import BrowserView

class DuplicatedBlocksUUIDFixer(BrowserView):
    """This script refreshes all UUIDs found in blocks with a new UUID to ensure all UUIDs are unique"""
    def __call__(self): ...
