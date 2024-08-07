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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.rule_based_budget import RuleBasedBudget
from openapi_client.models.tactic import Tactic
from typing import Optional, Set
from typing_extensions import Self

class Campaign(BaseModel):
    """
    Campaign
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the campaign.")
    budget_type: Optional[StrictStr] = Field(default=None, description="The time period over which the amount specified in the `budget` property is allocated.", alias="budgetType")
    budget: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the budget.")
    start_date: Optional[StrictStr] = Field(default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future.", alias="startDate")
    end_date: Optional[StrictStr] = Field(default=None, description="The YYYYMMDD end date of the campaign.", alias="endDate")
    cost_type: Optional[StrictStr] = Field(default=None, description="Determines how the campaign will bid and charge. |Name|Description| |----|----------| |cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.| |vcpm |The performance of this campaign is measured by the viewed impressions triggered by the ad. |  To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).", alias="costType")
    state: Optional[StrictStr] = Field(default=None, description="The state of the campaign.")
    portfolio_id: Optional[StrictInt] = Field(default=None, description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.", alias="portfolioId")
    campaign_id: Optional[StrictInt] = Field(default=None, description="The identifier of the campaign.", alias="campaignId")
    tactic: Optional[Tactic] = None
    delivery_profile: Optional[StrictStr] = Field(default=None, alias="deliveryProfile")
    rule_based_budget: Optional[RuleBasedBudget] = Field(default=None, alias="ruleBasedBudget")
    __properties: ClassVar[List[str]] = ["name", "budgetType", "budget", "startDate", "endDate", "costType", "state", "portfolioId", "campaignId", "tactic", "deliveryProfile", "ruleBasedBudget"]

    @field_validator('budget_type')
    def budget_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['daily']):
            raise ValueError("must be one of enum values ('daily')")
        return value

    @field_validator('cost_type')
    def cost_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['cpc', 'vcpm']):
            raise ValueError("must be one of enum values ('cpc', 'vcpm')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'paused', 'archived']):
            raise ValueError("must be one of enum values ('enabled', 'paused', 'archived')")
        return value

    @field_validator('delivery_profile')
    def delivery_profile_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['as_soon_as_possible']):
            raise ValueError("must be one of enum values ('as_soon_as_possible')")
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
        """Create an instance of Campaign from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rule_based_budget
        if self.rule_based_budget:
            _dict['ruleBasedBudget'] = self.rule_based_budget.to_dict()
        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['endDate'] = None

        # set to None if portfolio_id (nullable) is None
        # and model_fields_set contains the field
        if self.portfolio_id is None and "portfolio_id" in self.model_fields_set:
            _dict['portfolioId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Campaign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "budgetType": obj.get("budgetType"),
            "budget": obj.get("budget"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "costType": obj.get("costType"),
            "state": obj.get("state"),
            "portfolioId": obj.get("portfolioId"),
            "campaignId": obj.get("campaignId"),
            "tactic": obj.get("tactic"),
            "deliveryProfile": obj.get("deliveryProfile"),
            "ruleBasedBudget": RuleBasedBudget.from_dict(obj["ruleBasedBudget"]) if obj.get("ruleBasedBudget") is not None else None
        })
        return _obj


