from z3c.form.converter import BaseDataConverter
from z3c.form.converter import CollectionSequenceDataConverter
from z3c.form.converter import SequenceDataConverter

class DateWidgetConverter(BaseDataConverter):
    """Data converter for date fields."""
    def toWidgetValue(self, value):
        """Converts from field value to widget.

        :param value: Field value.
        :type value: date

        :returns: Date in format `Y-m-d`
        :rtype: string
        """
    def toFieldValue(self, value):
        """Converts from widget value to field.

        :param value: Value inserted by date widget.
        :type value: string

        :returns: `date.date` object.
        :rtype: date
        """

class DatetimeWidgetConverter(BaseDataConverter):
    """Data converter for datetime fields."""
    def toWidgetValue(self, value):
        """Converts from field value to widget.

        :param value: Field value.
        :type value: datetime

        :returns: Datetime in format `Y-m-d H:M`
        :rtype: string
        """
    def toFieldValue(self, value):
        """Converts from widget value to field.

        :param value: Value inserted by datetime widget.
        :type value: string

        :returns: `datetime.datetime` object.
        :rtype: datetime
        """

class DateWidgetToDatetimeConverter(BaseDataConverter):
    """Data converter for date widget on datetime fields."""
    def toWidgetValue(self, value):
        """Converts from field value to widget.

        :param value: Field value.
        :type value: datetime

        :returns: Datetime in format `Y-m-d`
        :rtype: string
        """
    def toFieldValue(self, value):
        """Converts from widget value to field.

        :param value: Value inserted by datetime widget.
        :type value: string

        :returns: `datetime.datetime` object.
        :rtype: datetime
        """

class TimeWidgetConverter(BaseDataConverter):
    """Data converter for datetime fields."""

    type: str
    def toWidgetValue(self, value): ...
    def toFieldValue(self, value): ...

class Select2WidgetConverterBase:
    def toFieldValue(self, value):
        """Converts from widget value to field.

        :param value: Value inserted by Select2 widget or default html
                      select/multi-select
        :type value: string | list

        :returns: List of items
        :rtype: list | tuple | set
        """

class SequenceSelect2WidgetConverter(Select2WidgetConverterBase, SequenceDataConverter):
    """Data converter for IField fields using the Select2Widget."""

class Select2WidgetConverter(
    Select2WidgetConverterBase, CollectionSequenceDataConverter
):
    """Data converter for ICollection fields using the Select2Widget."""

class AjaxSelectWidgetConverter(BaseDataConverter):
    """Data converter for ICollection fields using the AjaxSelectWidget."""
    def toWidgetValue(self, value):
        """Converts from field value to widget tokenized widget value.

        :param value: Field value.
        :type value: list |tuple | set

        :returns: Items separated using separator defined on widget
        :rtype: string
        """
    def toFieldValue(self, value):
        """Converts from widget value to field.

        :param value: Value inserted by AjaxSelect widget.
        :type value: string

        :returns: List of items
        :rtype: list | tuple | set
        """

class RelationChoiceContentBrowserWidgetConverter(BaseDataConverter):
    """Data converter for RelationChoice fields using the ContentBrowserWidget."""
    def toWidgetValue(self, value): ...
    def toFieldValue(self, value): ...

class RelationChoiceRelatedItemsWidgetConverter(
    RelationChoiceContentBrowserWidgetConverter
):
    """backwards compatibility"""

class RelationChoiceSelectWidgetConverter(RelationChoiceContentBrowserWidgetConverter):
    """Data converter for RelationChoice fields using with SequenceWidgets,
    which expect sequence values.
    """
    def toWidgetValue(self, value): ...

class ContentBrowserDataConverter(BaseDataConverter):
    """Data converter for ICollection fields using the ContentBrowserWidget."""
    def toWidgetValue(self, value):
        """Converts from field value to widget.

        :param value: List of catalog brains.
        :type value: list

        :returns: List of of UID separated by separator defined on widget.
        :rtype: string
        """
    def toFieldValue(self, value):
        """Converts from widget value to field.

        :param value: List of UID's separated by separator defined
        :type value: string

        :returns: List of content objects
        :rtype: list | tuple | set
        """

class RelatedItemsDataConverter(ContentBrowserDataConverter):
    """backwards compatibility"""

class RelationListSelectWidgetDataConverter(ContentBrowserDataConverter):
    """Data converter for RelationChoice fields using with SequenceWidgets,
    which expect sequence values.
    """
    def toWidgetValue(self, value):
        """Converts from field value to widget.

        :param value: List of catalog brains.
        :type value: list

        :returns: List of of UID.
        :rtype: list
        """

class QueryStringDataConverter(BaseDataConverter):
    """Data converter for IList."""
    def toWidgetValue(self, value):
        """Converts from field value to widget.

        :param value: Query string.
        :type value: list

        :returns: Query string converted to JSON.
        :rtype: string
        """
    def toFieldValue(self, value):
        """Converts from widget value to field.

        :param value: Query string.
        :type value: string

        :returns: Query string.
        :rtype: list
        """

class LinkWidgetDataConverter(BaseDataConverter):
    """Data converter for the enhanced link widget."""
    def toWidgetValue(self, value): ...
    def toFieldValue(self, value):
        """Converts from widget value to field."""

class BoolSingleCheckboxDataConverter(BaseDataConverter):
    """Special converter between boolean fields and single checkbox widgets."""
    def toWidgetValue(self, value):
        """Convert from Python bool to token sequence representation."""
    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
