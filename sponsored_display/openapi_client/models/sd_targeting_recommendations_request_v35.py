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
from typing_extensions import Annotated
from openapi_client.models.location_expression import LocationExpression
from openapi_client.models.sd_recommendation_type_v33 import SDRecommendationTypeV33
from openapi_client.models.sd_tactic_v31 import SDTacticV31
from openapi_client.models.sd_targeting_recommendations_products_v31_inner import SDTargetingRecommendationsProductsV31Inner
from openapi_client.models.sd_targeting_recommendations_themes import SDTargetingRecommendationsThemes
from typing import Optional, Set
from typing_extensions import Self

class SDTargetingRecommendationsRequestV35(BaseModel):
    """
    Request for targeting recommendations for API version 3.5.
    """ # noqa: E501
    tactic: SDTacticV31
    products: Annotated[List[SDTargetingRecommendationsProductsV31Inner], Field(min_length=1, max_length=10000)] = Field(description="A list of products for which to get targeting recommendations. This array can only contain either asins or landing pages. If landingPageURL is used, there can only be one item in the array for each request.")
    type_filter: Annotated[List[SDRecommendationTypeV33], Field(min_length=1, max_length=3)] = Field(description="A filter to indicate which types of recommendations to request.", alias="typeFilter")
    themes: Optional[SDTargetingRecommendationsThemes] = None
    category_type: Optional[StrictStr] = Field(default=None, description="This field is optional unless the field locationExpression is present in the request. It is used for category audience targeting to specify if the audience is for views (re-marketing) or purchases (re-purchasing). The specified categories will be returned accordingly.", alias="categoryType")
    location_expression: Optional[Annotated[List[LocationExpression], Field(min_length=1, max_length=20)]] = Field(default=None, description="This optional field is used to specify the locations used in SD location targeting for non-Amazon sellers only at the moment. Therefore it's only supported if the product is a landing page url.", alias="locationExpression")
    __properties: ClassVar[List[str]] = ["tactic", "products", "typeFilter", "themes", "categoryType", "locationExpression"]

    @field_validator('category_type')
    def category_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['views', 'purchases']):
            raise ValueError("must be one of enum values ('views', 'purchases')")
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
        """Create an instance of SDTargetingRecommendationsRequestV35 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item in self.products:
                if _item:
                    _items.append(_item.to_dict())
            _dict['products'] = _items
        # override the default output from pydantic by calling `to_dict()` of themes
        if self.themes:
            _dict['themes'] = self.themes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in location_expression (list)
        _items = []
        if self.location_expression:
            for _item in self.location_expression:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locationExpression'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SDTargetingRecommendationsRequestV35 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tactic": obj.get("tactic"),
            "products": [SDTargetingRecommendationsProductsV31Inner.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None,
            "typeFilter": obj.get("typeFilter"),
            "themes": SDTargetingRecommendationsThemes.from_dict(obj["themes"]) if obj.get("themes") is not None else None,
            "categoryType": obj.get("categoryType"),
            "locationExpression": [LocationExpression.from_dict(_item) for _item in obj["locationExpression"]] if obj.get("locationExpression") is not None else None
        })
        return _obj


