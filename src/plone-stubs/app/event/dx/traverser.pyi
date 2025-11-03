from plone.app.event.recurrence import OccurrenceTraverser as DefaultTraverser

class OccurrenceTraverser(DefaultTraverser):
    """Occurrence Traverser for Dexterity based contexts.

    Please note: here is not ImageTraverser support included, since accessing
    images is done by calling the @@images view.
    """
    def fallbackTraverse(self, request, name): ...
