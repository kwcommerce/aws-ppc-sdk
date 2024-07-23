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


class CreativeType(str, Enum):
    """
    The type of the associated creative. If the field is empty or null, a default value of IMAGE will be used. One ad group only supports one type (VIDEO or IMAGE) of creativeType at a time. |Name|Description| |----|-----------| |IMAGE |The creative will display static assets (e.g. headline, brandLogo or custom image).| |VIDEO |The creative will display video assets. This type of creative must have a video asset provided. Only supported when using productAds with ASIN or SKU.|
    """

    """
    allowed enum values
    """
    IMAGE = 'IMAGE'
    VIDEO = 'VIDEO'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CreativeType from a JSON string"""
        return cls(json.loads(json_str))

