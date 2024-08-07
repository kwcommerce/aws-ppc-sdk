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
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ReportResponse(BaseModel):
    """
    ReportResponse
    """ # noqa: E501
    report_id: Optional[StrictStr] = Field(default=None, description="The identifier of the report.", alias="reportId")
    record_type: Optional[StrictStr] = Field(default=None, description="The type of report requested.", alias="recordType")
    status: Optional[StrictStr] = Field(default=None, description="The build status of the report.")
    status_details: Optional[StrictStr] = Field(default=None, description="A human-readable description of the current status.", alias="statusDetails")
    location: Optional[StrictStr] = Field(default=None, description="The URI location of the report.")
    file_size: Optional[StrictInt] = Field(default=None, description="The size of the report file, in bytes.", alias="fileSize")
    expiration: Optional[StrictInt] = Field(default=None, description="Epoch date of the expiration of the URI in the `location` property.")
    __properties: ClassVar[List[str]] = ["reportId", "recordType", "status", "statusDetails", "location", "fileSize", "expiration"]

    @field_validator('record_type')
    def record_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CAMPAIGN', 'AD_GROUP', 'PRODUCT_AD']):
            raise ValueError("must be one of enum values ('CAMPAIGN', 'AD_GROUP', 'PRODUCT_AD')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['IN_PROGRESS', 'SUCCESS', 'FAILURE']):
            raise ValueError("must be one of enum values ('IN_PROGRESS', 'SUCCESS', 'FAILURE')")
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
        """Create an instance of ReportResponse from a JSON string"""
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
        """Create an instance of ReportResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reportId": obj.get("reportId"),
            "recordType": obj.get("recordType"),
            "status": obj.get("status"),
            "statusDetails": obj.get("statusDetails"),
            "location": obj.get("location"),
            "fileSize": obj.get("fileSize"),
            "expiration": obj.get("expiration")
        })
        return _obj


