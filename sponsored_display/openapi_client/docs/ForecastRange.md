# ForecastRange

Forecast range values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.forecast_range import ForecastRange

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastRange from a JSON string
forecast_range_instance = ForecastRange.from_json(json)
# print the JSON string representation of the object
print(ForecastRange.to_json())

# convert the object into a dict
forecast_range_dict = forecast_range_instance.to_dict()
# create an instance of ForecastRange from a dict
forecast_range_from_dict = ForecastRange.from_dict(forecast_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


