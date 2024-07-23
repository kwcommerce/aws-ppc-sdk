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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.creative_moderation_policy_violations_inner_violating_brand_logo_contents_inner_image_evidences_inner_violating_image_crop import CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInnerViolatingImageCrop
from typing import Optional, Set
from typing_extensions import Self

class CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInner(BaseModel):
    """
    CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInner
    """ # noqa: E501
    violating_image_crop: Optional[CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInnerViolatingImageCrop] = Field(default=None, alias="violatingImageCrop")
    __properties: ClassVar[List[str]] = ["violatingImageCrop"]

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
        """Create an instance of CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of violating_image_crop
        if self.violating_image_crop:
            _dict['violatingImageCrop'] = self.violating_image_crop.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "violatingImageCrop": CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInnerViolatingImageCrop.from_dict(obj["violatingImageCrop"]) if obj.get("violatingImageCrop") is not None else None
        })
        return _obj


