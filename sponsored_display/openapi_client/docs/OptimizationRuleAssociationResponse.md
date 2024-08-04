# OptimizationRuleAssociationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of the response. | [optional] 
**responses** | [**List[SingleOptimizationRuleAssociationResponse]**](SingleOptimizationRuleAssociationResponse.md) | An array of response objects. Each response object has code, details and optimizationRuleId. | [optional] 

## Example

```python
from openapi_client.models.optimization_rule_association_response import OptimizationRuleAssociationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationRuleAssociationResponse from a JSON string
optimization_rule_association_response_instance = OptimizationRuleAssociationResponse.from_json(json)
# print the JSON string representation of the object
print(OptimizationRuleAssociationResponse.to_json())

# convert the object into a dict
optimization_rule_association_response_dict = optimization_rule_association_response_instance.to_dict()
# create an instance of OptimizationRuleAssociationResponse from a dict
optimization_rule_association_response_from_dict = OptimizationRuleAssociationResponse.from_dict(optimization_rule_association_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


