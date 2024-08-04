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
from typing import Any, ClassVar, Dict, List, Union
from openapi_client.models.creative_properties import CreativeProperties
from openapi_client.models.creative_type_in_creative_response import CreativeTypeInCreativeResponse
from typing import Optional, Set
from typing_extensions import Self

class Creative(BaseModel):
    """
    Creative model.
    """ # noqa: E501
    creative_id: Union[StrictFloat, StrictInt] = Field(description="Unique identifier of the creative.", alias="creativeId")
    ad_group_id: StrictInt = Field(description="The identifier of the ad group.", alias="adGroupId")
    creative_type: CreativeTypeInCreativeResponse = Field(alias="creativeType")
    properties: CreativeProperties
    moderation_status: StrictStr = Field(description="The moderation status of the creative", alias="moderationStatus")
    __properties: ClassVar[List[str]] = ["creativeId", "adGroupId", "creativeType", "properties", "moderationStatus"]

    @field_validator('moderation_status')
    def moderation_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['APPROVED', 'PENDING_REVIEW', 'REJECTED']):
            raise ValueError("must be one of enum values ('APPROVED', 'PENDING_REVIEW', 'REJECTED')")
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
        """Create an instance of Creative from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Creative from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "creativeId": obj.get("creativeId"),
            "adGroupId": obj.get("adGroupId"),
            "creativeType": obj.get("creativeType"),
            "properties": CreativeProperties.from_dict(obj["properties"]) if obj.get("properties") is not None else None,
            "moderationStatus": obj.get("moderationStatus")
        })
        return _obj


