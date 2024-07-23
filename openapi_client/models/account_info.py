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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.account_type import AccountType
from typing import Optional, Set
from typing_extensions import Self

class AccountInfo(BaseModel):
    """
    AccountInfo
    """ # noqa: E501
    marketplace_string_id: Optional[StrictStr] = Field(default=None, description="The identifier of the marketplace to which the account is associated.", alias="marketplaceStringId")
    id: Optional[StrictStr] = Field(default=None, description="Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace.")
    type: Optional[AccountType] = None
    name: Optional[StrictStr] = Field(default=None, description="Account name.")
    sub_type: Optional[StrictStr] = Field(default=None, description="The account subtype.", alias="subType")
    valid_payment_method: Optional[StrictBool] = Field(default=None, description="Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not.", alias="validPaymentMethod")
    __properties: ClassVar[List[str]] = ["marketplaceStringId", "id", "type", "name", "subType", "validPaymentMethod"]

    @field_validator('sub_type')
    def sub_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['KDP_AUTHOR', 'AMAZON_ATTRIBUTION']):
            raise ValueError("must be one of enum values ('KDP_AUTHOR', 'AMAZON_ATTRIBUTION')")
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
        """Create an instance of AccountInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "marketplace_string_id",
            "id",
            "name",
            "sub_type",
            "valid_payment_method",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "marketplaceStringId": obj.get("marketplaceStringId"),
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "subType": obj.get("subType"),
            "validPaymentMethod": obj.get("validPaymentMethod")
        })
        return _obj


