# OptimizationRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of the response. | [optional] 
**description** | **str** | A human-readable description of the response. | [optional] 
**rule_id** | **str** | The identifier of the optimization rule. | [optional] 

## Example

```python
from openapi_client.models.optimization_rule_response import OptimizationRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationRuleResponse from a JSON string
optimization_rule_response_instance = OptimizationRuleResponse.from_json(json)
# print the JSON string representation of the object
print(OptimizationRuleResponse.to_json())

# convert the object into a dict
optimization_rule_response_dict = optimization_rule_response_instance.to_dict()
# create an instance of OptimizationRuleResponse from a dict
optimization_rule_response_from_dict = OptimizationRuleResponse.from_dict(optimization_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


