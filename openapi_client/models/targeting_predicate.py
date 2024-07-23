# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TargetingPredicate(BaseModel):
    """
    A predicate to match against in the targeting expression (only applicable to contextual targeting - T00020).  * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system. * Brand, price, and review predicates are optional and may only be specified if category is also specified. * Review predicates accept numbers between 0 and 5 and are inclusive. * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive.
    """ # noqa: E501
    type: Optional[StrictStr] = None
    value: Optional[StrictStr] = Field(default=None, description="The value to be targeted.")
    __properties: ClassVar[List[str]] = ["type", "value"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['asinSameAs', 'asinCategorySameAs', 'asinBrandSameAs', 'asinPriceBetween', 'asinPriceGreaterThan', 'asinPriceLessThan', 'asinReviewRatingLessThan', 'asinReviewRatingGreaterThan', 'asinReviewRatingBetween', 'asinIsPrimeShippingEligible', 'asinAgeRangeSameAs', 'asinGenreSameAs', 'similarProduct']):
            raise ValueError("must be one of enum values ('asinSameAs', 'asinCategorySameAs', 'asinBrandSameAs', 'asinPriceBetween', 'asinPriceGreaterThan', 'asinPriceLessThan', 'asinReviewRatingLessThan', 'asinReviewRatingGreaterThan', 'asinReviewRatingBetween', 'asinIsPrimeShippingEligible', 'asinAgeRangeSameAs', 'asinGenreSameAs', 'similarProduct')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TargetingPredicate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TargetingPredicate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "value": obj.get("value")
        })
        return _obj

