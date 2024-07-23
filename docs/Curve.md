# Curve

Forecast curve of a certain type. The type could be budget vs forecast outcome.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meet_threshold** | **bool** | True if the budget utilization is good to show the curve. | [optional] 
**graph** | **str** | Type of Graph. | [optional] 
**points** | [**List[CurvePoint]**](CurvePoint.md) |  | [optional] 

## Example

```python
from openapi_client.models.curve import Curve

# TODO update the JSON string below
json = "{}"
# create an instance of Curve from a JSON string
curve_instance = Curve.from_json(json)
# print the JSON string representation of the object
print(Curve.to_json())

# convert the object into a dict
curve_dict = curve_instance.to_dict()
# create an instance of Curve from a dict
curve_from_dict = Curve.from_dict(curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


