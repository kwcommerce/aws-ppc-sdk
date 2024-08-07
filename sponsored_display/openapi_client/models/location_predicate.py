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


class LocationPredicate(str, Enum):
    """
    The location category.
    """

    """
    allowed enum values
    """
    LOCATION = 'location'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LocationPredicate from a JSON string"""
        return cls(json.loads(json_str))


