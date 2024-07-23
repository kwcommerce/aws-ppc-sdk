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


class Locale(str, Enum):
    """
    Locale string as described in [BCP 47](https://tools.ietf.org/html/bcp47). For example, `en-US`
    """

    """
    allowed enum values
    """
    EN_MINUS_US = 'en-US'
    ES_MINUS_MX = 'es-MX'
    ZH_MINUS_CN = 'zh-CN'
    ES_MINUS_ES = 'es-ES'
    IT_MINUS_IT = 'it-IT'
    FR_MINUS_FR = 'fr-FR'
    FR_MINUS_CA = 'fr-CA'
    DE_MINUS_DE = 'de-DE'
    JA_MINUS_JP = 'ja-JP'
    KO_MINUS_KR = 'ko-KR'
    EN_MINUS_GB = 'en-GB'
    EN_MINUS_CA = 'en-CA'
    HI_MINUS_IN = 'hi-IN'
    EN_MINUS_IN = 'en-IN'
    EN_MINUS_DE = 'en-DE'
    EN_MINUS_ES = 'en-ES'
    EN_MINUS_FR = 'en-FR'
    EN_MINUS_IT = 'en-IT'
    EN_MINUS_JP = 'en-JP'
    EN_MINUS_AE = 'en-AE'
    AR_MINUS_AE = 'ar-AE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Locale from a JSON string"""
        return cls(json.loads(json_str))


