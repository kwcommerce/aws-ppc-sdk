# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CallToActionType(str, Enum):
    """
    The call to action type. |Call to action type|Description| |--------|-----------| |SIGN_UP|Call to action type for customers to sign up.| |INQUIRE|Call to action type for customers to inquire.| |REQUEST_QUOTE|Call to action type for customers to request a quote.|
    """

    """
    allowed enum values
    """
    SIGN_UP = 'SIGN_UP'
    INQUIRE = 'INQUIRE'
    REQUEST_QUOTE = 'REQUEST_QUOTE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CallToActionType from a JSON string"""
        return cls(json.loads(json_str))

