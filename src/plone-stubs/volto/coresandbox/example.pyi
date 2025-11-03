from _typeshed import Incomplete
from plone.dexterity.content import Container
from plone.supermodel import model

_: Incomplete
PloneMessageFactory: Incomplete

class IExample(model.Schema):
    """Dexterity-Schema with all field-types."""

    title: Incomplete
    description: Incomplete
    text_field: Incomplete
    textline_field: Incomplete
    bool_field: Incomplete
    choice_field: Incomplete
    choice_field_radio: Incomplete
    choice_field_voc: Incomplete
    choice_field_select: Incomplete
    list_field: Incomplete
    list_field_checkbox: Incomplete
    list_field_select: Incomplete
    list_field_voc_unconstrained: Incomplete
    list_field_voc_huge: Incomplete
    list_field_voc_huge_unconstrained: Incomplete
    tuple_field: Incomplete
    set_field: Incomplete
    set_field_checkbox: Incomplete
    image_field: Incomplete
    file_field: Incomplete
    datetime_field: Incomplete
    date_field: Incomplete
    relationchoice_field: Incomplete
    relationlist_field: Incomplete
    relationchoice_field_constrained: Incomplete
    relationlist_field_constrained: Incomplete
    relationlist_field_search_mode: Incomplete
    relationchoice_field_select: Incomplete
    relationchoice_field_radio: Incomplete
    relationlist_field_select: Incomplete
    relationlist_field_checkbox: Incomplete
    uuid_choice_field: Incomplete
    uuid_list_field: Incomplete
    uuid_choice_field_constrained: Incomplete
    uuid_list_field_constrained: Incomplete
    uuid_list_field_search_mode: Incomplete
    uuid_choice_field_select: Incomplete
    uuid_choice_field_radio: Incomplete
    uuid_list_field_select: Incomplete
    uuid_list_field_checkbox: Incomplete
    int_field: Incomplete
    float_field: Incomplete
    email_field: Incomplete
    uri_field: Incomplete
    richtext_field: Incomplete
    sourcetext_field: Incomplete
    ascii_field: Incomplete
    bytesline_field: Incomplete
    asciiline_field: Incomplete
    pythonidentifier_field: Incomplete
    dottedname_field: Incomplete
    dict_field: Incomplete
    available_languages: Incomplete
    dict_field_with_choice: Incomplete

class Example(Container):
    """Example instance class"""
