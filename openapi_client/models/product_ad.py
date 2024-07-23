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
from openapi_client.models.landing_page_type import LandingPageType
from typing import Optional, Set
from typing_extensions import Self

class ProductAd(BaseModel):
    """
    ProductAd
    """ # noqa: E501
    state: Optional[StrictStr] = Field(default=None, description="The state of the campaign associated with the product ad.")
    ad_id: Optional[StrictInt] = Field(default=None, description="The identifier of the product ad.", alias="adId")
    ad_group_id: Optional[StrictInt] = Field(default=None, description="The identifier of the ad group.", alias="adGroupId")
    campaign_id: Optional[StrictInt] = Field(default=None, description="The identifier of the campaign.", alias="campaignId")
    landing_page_url: Optional[StrictStr] = Field(default=None, description="The URL where customers will land after clicking on its link. Must be provided if a LandingPageType is set. Please note that if a single product ad sets the landing page url, only one product ad can be added to the ad group. This field is not supported when using ASIN or SKU fields. ||Specifications| |------------------|------------------| |LandingPageType| Description| |STORE| The url should be in the format of https://www.amazon.com/stores/* (using a correct Amazon url based on the marketplace)| |OFF_AMAZON_LINK| The url should be in the format of https://www.****.com. Note that this LandingPageType is not supported when using ASIN or SKU fields. A custom creative of headline, logo, image are require for this LandingPageType. | |MOMENT| Not yet supported. The url should be in the format of https://www.amazon.com/moments/promotion/{campaignId} (using a correct Amazon url based on the marketplace)|", alias="landingPageUrl")
    landing_page_type: Optional[LandingPageType] = Field(default=None, alias="landingPageType")
    ad_name: Optional[StrictStr] = Field(default=None, description="The name of the ad. Note that this field is not supported when using ASIN or SKU fields.", alias="adName")
    asin: Optional[StrictStr] = Field(default=None, description="The Amazon ASIN of the product advertised by the product ad. This parameter is included in the response for sellers and vendors.")
    sku: Optional[StrictStr] = Field(default=None, description="The Amazon SKU of the product advertised by the product ad. This parameter is included in the response for sellers.")
    __properties: ClassVar[List[str]] = ["state", "adId", "adGroupId", "campaignId", "landingPageUrl", "landingPageType", "adName", "asin", "sku"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'paused', 'archived']):
            raise ValueError("must be one of enum values ('enabled', 'paused', 'archived')")
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
        """Create an instance of ProductAd from a JSON string"""
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
        """Create an instance of ProductAd from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "state": obj.get("state"),
            "adId": obj.get("adId"),
            "adGroupId": obj.get("adGroupId"),
            "campaignId": obj.get("campaignId"),
            "landingPageUrl": obj.get("landingPageUrl"),
            "landingPageType": obj.get("landingPageType"),
            "adName": obj.get("adName"),
            "asin": obj.get("asin"),
            "sku": obj.get("sku")
        })
        return _obj

