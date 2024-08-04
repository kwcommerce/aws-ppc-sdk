# CreateOptimizationRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the optimization rule. | 
**rule_name** | **str** | The name of the optimization rule. | [optional] 
**rule_conditions** | [**List[RuleCondition]**](RuleCondition.md) | A list of rule conditions that define the advertiser&#39;s intent for the outcome of the rule. The rule uses &#39;AND&#39; logic to combine every condition in this list, and will validate the combination when the rule is created or updated. | 

## Example

```python
from openapi_client.models.create_optimization_rule import CreateOptimizationRule

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOptimizationRule from a JSON string
create_optimization_rule_instance = CreateOptimizationRule.from_json(json)
# print the JSON string representation of the object
print(CreateOptimizationRule.to_json())

# convert the object into a dict
create_optimization_rule_dict = create_optimization_rule_instance.to_dict()
# create an instance of CreateOptimizationRule from a dict
create_optimization_rule_from_dict = CreateOptimizationRule.from_dict(create_optimization_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


