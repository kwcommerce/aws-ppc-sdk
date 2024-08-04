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


class BrandSafetyDenyListDomainUpdateResultStatus(str, Enum):
    """
    The state of the domain.
    """

    """
    allowed enum values
    """
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BrandSafetyDenyListDomainUpdateResultStatus from a JSON string"""
        return cls(json.loads(json_str))

