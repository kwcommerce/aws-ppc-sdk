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


class SDBidOptimizationV32(str, Enum):
    """
    Determines what the recommended bids will be optimized for.   |Name|CostType|Description| |----|--------|-----------| |reach|vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.| |clicks|cpc|Optimize for page visits| |conversions|cpc|Optimize for conversion|
    """

    """
    allowed enum values
    """
    REACH = 'reach'
    CLICKS = 'clicks'
    CONVERSIONS = 'conversions'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SDBidOptimizationV32 from a JSON string"""
        return cls(json.loads(json_str))


