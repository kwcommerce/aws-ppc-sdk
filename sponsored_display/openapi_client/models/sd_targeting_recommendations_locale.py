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


class SDTargetingRecommendationsLocale(str, Enum):
    """
    List of supported locales.
    """

    """
    allowed enum values
    """
    AR_AE = 'ar_AE'
    DE_DE = 'de_DE'
    EN_AE = 'en_AE'
    EN_AU = 'en_AU'
    EN_CA = 'en_CA'
    EN_GB = 'en_GB'
    EN_IN = 'en_IN'
    EN_SG = 'en_SG'
    EN_US = 'en_US'
    ES_ES = 'es_ES'
    ES_MX = 'es_MX'
    FR_CA = 'fr_CA'
    FR_FR = 'fr_FR'
    HI_IN = 'hi_IN'
    IT_IT = 'it_IT'
    JA_JP = 'ja_JP'
    KO_KR = 'ko_KR'
    NL_NL = 'nl_NL'
    PL_PL = 'pl_PL'
    PT_BR = 'pt_BR'
    SV_SE = 'sv_SE'
    TA_IN = 'ta_IN'
    TH_TH = 'th_TH'
    TR_TR = 'tr_TR'
    VI_VN = 'vi_VN'
    ZH_CN = 'zh_CN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SDTargetingRecommendationsLocale from a JSON string"""
        return cls(json.loads(json_str))


