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


class SDTacticV31(str, Enum):
    """
    The advertising tactic associated with the campaign. The following table lists available tactic names: |Tactic Name|Type|Description|         |-----------|-----|-----------|         |T00020 &nbsp;    |Products&nbsp;| Products: Choose individual products to show your ads in placements related to those products.<br>Categories: Choose individual categories to show your ads in placements related to those categories.|         |T00030&nbsp;|Audiences &nbsp;|Select individual audiences to show your ads.|
    """

    """
    allowed enum values
    """
    T00020 = 'T00020'
    T00030 = 'T00030'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SDTacticV31 from a JSON string"""
        return cls(json.loads(json_str))

