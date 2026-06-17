"""Partial stubs for :mod:`zope.schema`.

The public field names are defined in :mod:`zope.schema._field` and re-exported
here, mirroring the runtime package. ``ValidationError`` is re-exported from
:mod:`zope.schema.interfaces`.
"""

from zope.schema._field import ASCII as ASCII
from zope.schema._field import ASCIILine as ASCIILine
from zope.schema._field import Bool as Bool
from zope.schema._field import Bytes as Bytes
from zope.schema._field import BytesLine as BytesLine
from zope.schema._field import Choice as Choice
from zope.schema._field import Collection as Collection
from zope.schema._field import Container as Container
from zope.schema._field import Date as Date
from zope.schema._field import Datetime as Datetime
from zope.schema._field import Decimal as Decimal
from zope.schema._field import Dict as Dict
from zope.schema._field import DottedName as DottedName
from zope.schema._field import Field as Field
from zope.schema._field import Float as Float
from zope.schema._field import FrozenSet as FrozenSet
from zope.schema._field import Id as Id
from zope.schema._field import Int as Int
from zope.schema._field import InterfaceField as InterfaceField
from zope.schema._field import Iterable as Iterable
from zope.schema._field import List as List
from zope.schema._field import MinMaxLen as MinMaxLen
from zope.schema._field import NativeString as NativeString
from zope.schema._field import NativeStringLine as NativeStringLine
from zope.schema._field import Object as Object
from zope.schema._field import Orderable as Orderable
from zope.schema._field import Password as Password
from zope.schema._field import Set as Set
from zope.schema._field import SourceText as SourceText
from zope.schema._field import Text as Text
from zope.schema._field import TextLine as TextLine
from zope.schema._field import Time as Time
from zope.schema._field import Timedelta as Timedelta
from zope.schema._field import Tuple as Tuple
from zope.schema._field import URI as URI
from zope.schema.interfaces import ValidationError as ValidationError
