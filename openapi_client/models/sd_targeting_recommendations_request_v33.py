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
from typing_extensions import Annotated
from openapi_client.models.sd_goal_product import SDGoalProduct
from openapi_client.models.sd_recommendation_type_v32 import SDRecommendationTypeV32
from openapi_client.models.sd_tactic_v31 import SDTacticV31
from openapi_client.models.sd_targeting_recommendations_themes import SDTargetingRecommendationsThemes
from typing import Optional, Set
from typing_extensions import Self

class SDTargetingRecommendationsRequestV33(BaseModel):
    """
    Request for targeting recommendations for API version 3.3.
    """ # noqa: E501
    tactic: SDTacticV31
    products: Annotated[List[SDGoalProduct], Field(min_length=1, max_length=10000)] = Field(description="A list of products for which to get targeting recommendations")
    type_filter: Annotated[List[SDRecommendationTypeV32], Field(min_length=1, max_length=2)] = Field(description="A filter to indicate which types of recommendations to request.", alias="typeFilter")
    themes: Optional[SDTargetingRecommendationsThemes] = None
    __properties: ClassVar[List[str]] = ["tactic", "products", "typeFilter", "themes"]

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
        """Create an instance of SDTargetingRecommendationsRequestV33 from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SDTargetingRecommendationsRequestV33 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tactic": obj.get("tactic"),
            "products": [SDGoalProduct.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None,
            "typeFilter": obj.get("typeFilter"),
            "themes": SDTargetingRecommendationsThemes.from_dict(obj["themes"]) if obj.get("themes") is not None else None
        })
        return _obj

