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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.create_targeting_expression_inner import CreateTargetingExpressionInner
from typing import Optional, Set
from typing_extensions import Self

class CreateTargetingClause(BaseModel):
    """
    CreateTargetingClause
    """ # noqa: E501
    state: Optional[StrictStr] = None
    bid: Optional[Union[Annotated[float, Field(strict=True, ge=0.02)], Annotated[int, Field(strict=True, ge=1)]]] = Field(default=None, description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.")
    ad_group_id: StrictInt = Field(description="The identifier of the ad group.", alias="adGroupId")
    expression_type: StrictStr = Field(description="Tactic T00020 ad groups only allow manual targeting.", alias="expressionType")
    expression: List[CreateTargetingExpressionInner] = Field(description="The targeting expression to match against.  ------- Applicable to contextual targeting (T00020) ------- * A 'TargetingExpression' in a contextual targeting campaign can only contain 'TargetingPredicate' components. * Expressions must specify either a category predicate or an ASIN predicate, but never both. * Only one category may be specified per targeting expression. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.  ------- Applicable to audiences or contextual targeting (T00030) ------- * A 'TargetingExpression' in a audiences or contextual campaign can only contain 'TargetingPredicateNested' components. * Expressions must specify either auto ASIN-grain (exact products), manual ASIN-grain (similar products), or manual category-grain targeting.")
    __properties: ClassVar[List[str]] = ["state", "bid", "adGroupId", "expressionType", "expression"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'paused', 'archived']):
            raise ValueError("must be one of enum values ('enabled', 'paused', 'archived')")
        return value

    @field_validator('expression_type')
    def expression_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['manual', 'auto']):
            raise ValueError("must be one of enum values ('manual', 'auto')")
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
        """Create an instance of CreateTargetingClause from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in expression (list)
        _items = []
        if self.expression:
            for _item in self.expression:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expression'] = _items
        # set to None if bid (nullable) is None
        # and model_fields_set contains the field
        if self.bid is None and "bid" in self.model_fields_set:
            _dict['bid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateTargetingClause from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "state": obj.get("state"),
            "bid": obj.get("bid"),
            "adGroupId": obj.get("adGroupId"),
            "expressionType": obj.get("expressionType"),
            "expression": [CreateTargetingExpressionInner.from_dict(_item) for _item in obj["expression"]] if obj.get("expression") is not None else None
        })
        return _obj


