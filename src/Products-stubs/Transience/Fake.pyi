from Persistence.mapping import PersistentMapping

class FakeIOBTree(PersistentMapping):
    def keys(self, min, max): ...
