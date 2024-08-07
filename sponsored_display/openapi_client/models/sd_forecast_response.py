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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.curve import Curve
from openapi_client.models.forecast import Forecast
from openapi_client.models.forecast_status import ForecastStatus
from typing import Optional, Set
from typing_extensions import Self

class SDForecastResponse(BaseModel):
    """
    Response to a request for SD forecasting.
    """ # noqa: E501
    bid_optimization: Optional[StrictStr] = Field(default=None, alias="bidOptimization")
    lifetime_forecasts: Optional[Annotated[List[Forecast], Field(min_length=1, max_length=4)]] = Field(default=None, description="Forecasts for campaign start date and end date. Default end date is start date plus 7 days.", alias="lifetimeForecasts")
    weekly_forecasts: Optional[Annotated[List[Forecast], Field(min_length=1, max_length=4)]] = Field(default=None, description="Weekly average forecasts.", alias="weeklyForecasts")
    daily_forecasts: Optional[Annotated[List[Forecast], Field(min_length=1, max_length=4)]] = Field(default=None, description="Daily average forecasts.", alias="dailyForecasts")
    curves: Optional[Annotated[List[Curve], Field(min_length=0, max_length=10)]] = Field(default=None, description="Forecasting curves.")
    forecast_status: Optional[ForecastStatus] = Field(default=None, alias="forecastStatus")
    __properties: ClassVar[List[str]] = ["bidOptimization", "lifetimeForecasts", "weeklyForecasts", "dailyForecasts", "curves", "forecastStatus"]

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
        """Create an instance of SDForecastResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lifetime_forecasts (list)
        _items = []
        if self.lifetime_forecasts:
            for _item in self.lifetime_forecasts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lifetimeForecasts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in weekly_forecasts (list)
        _items = []
        if self.weekly_forecasts:
            for _item in self.weekly_forecasts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['weeklyForecasts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in daily_forecasts (list)
        _items = []
        if self.daily_forecasts:
            for _item in self.daily_forecasts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dailyForecasts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in curves (list)
        _items = []
        if self.curves:
            for _item in self.curves:
                if _item:
                    _items.append(_item.to_dict())
            _dict['curves'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SDForecastResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bidOptimization": obj.get("bidOptimization"),
            "lifetimeForecasts": [Forecast.from_dict(_item) for _item in obj["lifetimeForecasts"]] if obj.get("lifetimeForecasts") is not None else None,
            "weeklyForecasts": [Forecast.from_dict(_item) for _item in obj["weeklyForecasts"]] if obj.get("weeklyForecasts") is not None else None,
            "dailyForecasts": [Forecast.from_dict(_item) for _item in obj["dailyForecasts"]] if obj.get("dailyForecasts") is not None else None,
            "curves": [Curve.from_dict(_item) for _item in obj["curves"]] if obj.get("curves") is not None else None,
            "forecastStatus": obj.get("forecastStatus")
        })
        return _obj


