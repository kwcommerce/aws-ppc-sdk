# PerformanceMeasureCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | [**PerformanceMetric**](PerformanceMetric.md) |  | 
**comparison_operator** | [**ComparisonOperator**](ComparisonOperator.md) |  | 
**threshold** | **float** | The performance threshold value. | 

## Example

```python
from openapi_client.models.performance_measure_condition import PerformanceMeasureCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceMeasureCondition from a JSON string
performance_measure_condition_instance = PerformanceMeasureCondition.from_json(json)
# print the JSON string representation of the object
print(PerformanceMeasureCondition.to_json())

# convert the object into a dict
performance_measure_condition_dict = performance_measure_condition_instance.to_dict()
# create an instance of PerformanceMeasureCondition from a dict
performance_measure_condition_from_dict = PerformanceMeasureCondition.from_dict(performance_measure_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


