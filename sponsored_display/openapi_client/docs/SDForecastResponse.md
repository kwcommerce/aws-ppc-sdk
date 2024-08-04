# SDForecastResponse

Response to a request for SD forecasting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_optimization** | **str** |  | [optional] 
**lifetime_forecasts** | [**List[Forecast]**](Forecast.md) | Forecasts for campaign start date and end date. Default end date is start date plus 7 days. | [optional] 
**weekly_forecasts** | [**List[Forecast]**](Forecast.md) | Weekly average forecasts. | [optional] 
**daily_forecasts** | [**List[Forecast]**](Forecast.md) | Daily average forecasts. | [optional] 
**curves** | [**List[Curve]**](Curve.md) | Forecasting curves. | [optional] 
**forecast_status** | [**ForecastStatus**](ForecastStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_forecast_response import SDForecastResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SDForecastResponse from a JSON string
sd_forecast_response_instance = SDForecastResponse.from_json(json)
# print the JSON string representation of the object
print(SDForecastResponse.to_json())

# convert the object into a dict
sd_forecast_response_dict = sd_forecast_response_instance.to_dict()
# create an instance of SDForecastResponse from a dict
sd_forecast_response_from_dict = SDForecastResponse.from_dict(sd_forecast_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


