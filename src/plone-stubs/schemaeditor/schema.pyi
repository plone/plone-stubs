from _typeshed import Incomplete
from zope.schema import interfaces

class IBool(interfaces.IBool, interfaces.IFromUnicode): ...

class IFloat(interfaces.IFloat, interfaces.IFromUnicode):
    min: Incomplete
    max: Incomplete

class IDatetime(interfaces.IDatetime):
    min: Incomplete
    max: Incomplete

class IDate(interfaces.IDate):
    min: Incomplete
    max: Incomplete

class IChoice(interfaces.IChoice, interfaces.IFromUnicode): ...

class ITextLinesField(interfaces.IList):
    """A marker for fields which should get the textlines widget"""

class ITextLineChoice(interfaces.IField):
    values: Incomplete
    vocabularyName: Incomplete
