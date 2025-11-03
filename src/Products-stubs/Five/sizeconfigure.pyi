from Products.Five import fivemethod

@fivemethod
def get_size(self): ...
def classSizable(class_) -> None:
    """Monkey the class to be sizable through Five"""

def sizable(_context, class_) -> None: ...
def killMonkey(class_, name, fallback, attr=None) -> None:
    """Die monkey, die!"""

def unsizable(class_) -> None:
    """Restore class's initial state with respect to being sizable"""

def cleanUp() -> None: ...
