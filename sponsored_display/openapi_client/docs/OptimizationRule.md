# OptimizationRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the optimization rule. | [optional] 
**rule_name** | **str** | The name of the optimization rule. | [optional] 
**rule_conditions** | [**List[RuleCondition]**](RuleCondition.md) | A list of rule conditions that define the advertiser&#39;s intent for the outcome of the rule. The rule uses &#39;AND&#39; logic to combine every condition in this list, and will validate the combination when the rule is created or updated. | [optional] 
**rule_id** | **str** | The identifier of the optimization rule. | [optional] 

## Example

```python
from openapi_client.models.optimization_rule import OptimizationRule

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizationRule from a JSON string
optimization_rule_instance = OptimizationRule.from_json(json)
# print the JSON string representation of the object
print(OptimizationRule.to_json())

# convert the object into a dict
optimization_rule_dict = optimization_rule_instance.to_dict()
# create an instance of OptimizationRule from a dict
optimization_rule_from_dict = OptimizationRule.from_dict(optimization_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


