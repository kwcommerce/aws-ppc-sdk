# CreateAssociatedOptimizationRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optimization_rule_ids** | **List[str]** | A list of optimization rule identifiers. | [optional] 

## Example

```python
from openapi_client.models.create_associated_optimization_rules_request import CreateAssociatedOptimizationRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssociatedOptimizationRulesRequest from a JSON string
create_associated_optimization_rules_request_instance = CreateAssociatedOptimizationRulesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAssociatedOptimizationRulesRequest.to_json())

# convert the object into a dict
create_associated_optimization_rules_request_dict = create_associated_optimization_rules_request_instance.to_dict()
# create an instance of CreateAssociatedOptimizationRulesRequest from a dict
create_associated_optimization_rules_request_from_dict = CreateAssociatedOptimizationRulesRequest.from_dict(create_associated_optimization_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


