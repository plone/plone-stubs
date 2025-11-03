from zope.schema import Choice
from zope.schema.interfaces import IChoice

class IPath(IChoice):
    """A field for selecting the path of an object in the site."""

class Path(Choice): ...
