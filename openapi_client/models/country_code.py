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


class CountryCode(str, Enum):
    """
    The countryCode for a given country |Region|`countryCode`|Country Name| |------|-----|-------| |NA|BR|Brazil| |NA|CA|Canada| |NA|MX|Mexico| |NA|US|United States| |EU|AE|United Arab Emirates| |EU|BE|Belgium|  |EU|DE|Germany| |EU|EG|Egypt| |EU|ES|Spain| |EU|FR|France| |EU|IN|India| |EU|IT|Italy| |EU|NL|The Netherlands| |EU|PL|Poland| |EU|SA|Saudi Arabia|  |EU|SE|Sweden|   |EU|TR|Turkey| |EU|UK|United Kingdom| |EU|ZA| South Africa | |FE|AU|Australia|     |FE|JP|Japan| |FE|SG|Singapore|
    """

    """
    allowed enum values
    """
    BR = 'BR'
    CA = 'CA'
    MX = 'MX'
    US = 'US'
    AE = 'AE'
    BE = 'BE'
    DE = 'DE'
    EG = 'EG'
    ES = 'ES'
    FR = 'FR'
    IN = 'IN'
    IT = 'IT'
    NL = 'NL'
    PL = 'PL'
    SA = 'SA'
    SE = 'SE'
    TR = 'TR'
    UK = 'UK'
    AU = 'AU'
    JP = 'JP'
    SG = 'SG'
    ZA = 'ZA'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CountryCode from a JSON string"""
        return cls(json.loads(json_str))


