# -*- coding: utf-8 -*-
"""Contains patterns used for identifying properties of elements."""

from ..middleware.text import Text
from ..middleware.checkbox import Checkbox
from ..middleware.radio import Radio
from ..middleware.dropdown import Dropdown
from . import constants

ELEMENT_TYPE_PATTERNS = [
    (
        ({constants.ELEMENT_TYPE_KEY: constants.TEXT_FIELD_IDENTIFIER},),
        Text,
    ),
    (
        ({constants.ELEMENT_TYPE_KEY: constants.SELECTABLE_IDENTIFIER},),
        Checkbox,
    ),
    (
        ({constants.ELEMENT_TYPE_KEY: constants.CHOICE_FIELD_IDENTIFIER},),
        Dropdown,
    ),
    (
        (
            {
                constants.PARENT_KEY: {
                    constants.ELEMENT_TYPE_KEY: constants.TEXT_FIELD_IDENTIFIER
                }
            },
        ),
        Text,
    ),
    (
        (
            {
                constants.PARENT_KEY: {
                    constants.ELEMENT_TYPE_KEY: constants.SELECTABLE_IDENTIFIER
                }
            },
            {
                constants.PARENT_KEY: {
                    constants.SUBTYPE_KEY: constants.WIDGET_SUBTYPE_KEY
                }
            },
        ),
        Checkbox,
    ),
    (
        (
            {
                constants.PARENT_KEY: {
                    constants.ELEMENT_TYPE_KEY: constants.SELECTABLE_IDENTIFIER
                }
            },
        ),
        Radio,
    ),
]

ELEMENT_KEY_PATTERNS = [
    {constants.ANNOTATION_FIELD_KEY: True},
    {constants.PARENT_KEY: {constants.ANNOTATION_FIELD_KEY: True}},
]
