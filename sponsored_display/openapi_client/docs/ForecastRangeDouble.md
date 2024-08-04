# ForecastRangeDouble

A range of value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **object** | Lower bound. | [optional] 
**mean** | **object** | Geometric mean of the upper and lower bounds. | [optional] 
**max** | **object** | Upper bound. | [optional] 

## Example

```python
from openapi_client.models.forecast_range_double import ForecastRangeDouble

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastRangeDouble from a JSON string
forecast_range_double_instance = ForecastRangeDouble.from_json(json)
# print the JSON string representation of the object
print(ForecastRangeDouble.to_json())

# convert the object into a dict
forecast_range_double_dict = forecast_range_double_instance.to_dict()
# create an instance of ForecastRangeDouble from a dict
forecast_range_double_from_dict = ForecastRangeDouble.from_dict(forecast_range_double_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


