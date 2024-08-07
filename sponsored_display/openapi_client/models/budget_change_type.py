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


class BudgetChangeType(str, Enum):
    """
    The value by which to update the budget of the budget rule.
    """

    """
    allowed enum values
    """
    PERCENT = 'PERCENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BudgetChangeType from a JSON string"""
        return cls(json.loads(json_str))


