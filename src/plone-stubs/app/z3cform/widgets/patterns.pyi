from _typeshed import Incomplete

def el_attrib(name):
    """Helper property methods to get/set/delete element property.

    :param name: [required] Name of the element property.
    :type name: string

    :returns: Property with getter/setter/deletter.
    :rtype: property
    """

class BaseWidget:
    """Basic patterns widget."""

    klass: Incomplete
    pattern: Incomplete
    el: Incomplete
    pattern_options: Incomplete
    def __init__(self, el, pattern, pattern_options={}) -> None:
        """
        :param el: [required] element type (eg. input, div, textarea, a, ...).
        :type el: string

        :param pattern: [required] Pattern name.
        :type pattern: string

        :param pattern_options: Patterns options.
        :type pattern_options: dict
        """
    def update(self) -> None:
        """Updating pattern_options in element `data-*` attribute."""
    def render(self):
        """Renders the widget

        :returns: Widget's HTML.
        :rtype: string
        """

class InputWidget(BaseWidget):
    """Widget with `input` element."""

    type: Incomplete
    value: Incomplete
    name: Incomplete
    def __init__(
        self, pattern, pattern_options={}, type: str = "text", name=None, value=None
    ) -> None:
        """
        :param pattern: [required] Pattern name.
        :type pattern: string

        :param pattern_options: Patterns options.
        :type pattern_options: dict

        :param type: `type` attribute of element.
        :type type: string

        :param name: `name` attribute of element.
        :type name: string

        :param value: `value` attribute of element.
        :type value: string
        """

class SelectWidget(BaseWidget):
    """Widget with `select` element."""

    name: Incomplete
    items: Incomplete
    multiple: Incomplete
    value: Incomplete
    def __init__(
        self,
        pattern,
        pattern_options={},
        items=[],
        name=None,
        value=None,
        multiple: bool = False,
    ) -> None:
        """
        :param pattern: [required] Pattern name.
        :type pattern: string

        :param pattern_options: Patterns options.
        :type pattern_options: dict

        :param items: List of value and title pairs which represents possible
                      options to choose from.
        :type items: list

        :param name: `name` attribute of element.
        :type name: string

        :param value: `value` attribute of element.
        :type value: string

        :param multiple: `multiple` attribute of element.
        :type multiple: bool
        """

class TextareaWidget(BaseWidget):
    """Widget with `textarea` element."""

    name: Incomplete
    value: Incomplete
    def __init__(self, pattern, pattern_options={}, name=None, value=None) -> None:
        """
        :param pattern: [required] Pattern name.
        :type pattern: string

        :param pattern_options: Patterns options.
        :type pattern_options: dict

        :param name: `name` attribute of element.
        :type name: string

        :param value: `value` of element.
        :type value: string
        """
