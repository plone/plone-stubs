from _typeshed import Incomplete

old_traverse: Incomplete

def traverse(self, name, ignored): ...
def manage_FTPlist(self, REQUEST):
    """Returns a directory listing consisting of a tuple of
    (id,stat) tuples, marshaled to a string. Note, the listing it
    should include '..' if there is a Folder above the current
    one.

    In the case of non-foldoid objects it should return a single
    tuple (id,stat) representing itself."""

old_require: Incomplete

def require(self, *args, **kw): ...
