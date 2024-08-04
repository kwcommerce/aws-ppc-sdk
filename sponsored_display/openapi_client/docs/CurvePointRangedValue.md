# CurvePointRangedValue

A ranged value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | KPI label. | [optional] 
**value** | [**ForecastRangeDouble**](ForecastRangeDouble.md) |  | [optional] 

## Example

```python
from openapi_client.models.curve_point_ranged_value import CurvePointRangedValue

# TODO update the JSON string below
json = "{}"
# create an instance of CurvePointRangedValue from a JSON string
curve_point_ranged_value_instance = CurvePointRangedValue.from_json(json)
# print the JSON string representation of the object
print(CurvePointRangedValue.to_json())

# convert the object into a dict
curve_point_ranged_value_dict = curve_point_ranged_value_instance.to_dict()
# create an instance of CurvePointRangedValue from a dict
curve_point_ranged_value_from_dict = CurvePointRangedValue.from_dict(curve_point_ranged_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


