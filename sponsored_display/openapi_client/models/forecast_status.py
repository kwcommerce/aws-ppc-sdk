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


class ForecastStatus(str, Enum):
    """
    It contains the forecast status. The IMPRESSION_TARGETING_TOO_NARROW field means the targeting  clauses are too narrow, and the IMPRESSION_TARGETING_TOO_BROAD field means the targeting clauses are too broad,  so our inventory impression forecast won't provide any useful information. The COMPLETE field means all the forecasts are complete.
    """

    """
    allowed enum values
    """
    IMPRESSION_TARGETING_TOO_NARROW = 'IMPRESSION_TARGETING_TOO_NARROW'
    IMPRESSION_TARGETING_TOO_BROAD = 'IMPRESSION_TARGETING_TOO_BROAD'
    COMPLETE = 'COMPLETE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ForecastStatus from a JSON string"""
        return cls(json.loads(json_str))


