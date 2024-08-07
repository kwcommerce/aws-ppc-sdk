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


class SDRecommendationTypeV32(str, Enum):
    """
    Signifies a type of recommendation. PRODUCT and CATEGORY are supported by tactic T00020. CATEGORY and AUDIENCE are supported by tactic T00030.
    """

    """
    allowed enum values
    """
    PRODUCT = 'PRODUCT'
    CATEGORY = 'CATEGORY'
    AUDIENCE = 'AUDIENCE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SDRecommendationTypeV32 from a JSON string"""
        return cls(json.loads(json_str))


