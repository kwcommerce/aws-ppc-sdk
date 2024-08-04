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


class ComparisonOperator(str, Enum):
    """
    The comparison operator.
    """

    """
    allowed enum values
    """
    GREATER_THAN = 'GREATER_THAN'
    LESS_THAN = 'LESS_THAN'
    LESS_THAN_OR_EQUAL_TO = 'LESS_THAN_OR_EQUAL_TO'
    GREATER_THAN_OR_EQUAL_TO = 'GREATER_THAN_OR_EQUAL_TO'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ComparisonOperator from a JSON string"""
        return cls(json.loads(json_str))


