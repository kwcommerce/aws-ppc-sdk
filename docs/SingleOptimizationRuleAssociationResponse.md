# SingleOptimizationRuleAssociationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of the response. | [optional] 
**details** | **str** | A human-readable description of the response. | [optional] 
**optimization_rule_id** | **str** | The identifier of the optimization rule. | [optional] 

## Example

```python
from openapi_client.models.single_optimization_rule_association_response import SingleOptimizationRuleAssociationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleOptimizationRuleAssociationResponse from a JSON string
single_optimization_rule_association_response_instance = SingleOptimizationRuleAssociationResponse.from_json(json)
# print the JSON string representation of the object
print(SingleOptimizationRuleAssociationResponse.to_json())

# convert the object into a dict
single_optimization_rule_association_response_dict = single_optimization_rule_association_response_instance.to_dict()
# create an instance of SingleOptimizationRuleAssociationResponse from a dict
single_optimization_rule_association_response_from_dict = SingleOptimizationRuleAssociationResponse.from_dict(single_optimization_rule_association_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


