# CurvePoint

A single point on a curve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_focus** | **bool** | If this point is the point with the focus circle. | [optional] 
**x** | [**List[CurvePointFixedValue]**](CurvePointFixedValue.md) | x-axis value. | [optional] 
**y** | [**List[CurvePointRangedValue]**](CurvePointRangedValue.md) | y-axis value of multiple KPI types. | [optional] 

## Example

```python
from openapi_client.models.curve_point import CurvePoint

# TODO update the JSON string below
json = "{}"
# create an instance of CurvePoint from a JSON string
curve_point_instance = CurvePoint.from_json(json)
# print the JSON string representation of the object
print(CurvePoint.to_json())

# convert the object into a dict
curve_point_dict = curve_point_instance.to_dict()
# create an instance of CurvePoint from a dict
curve_point_from_dict = CurvePoint.from_dict(curve_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


