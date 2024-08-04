# RuleBasedBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_processing** | **bool** |  | [optional] 
**applicable_rule_name** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**applicable_rule_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.rule_based_budget import RuleBasedBudget

# TODO update the JSON string below
json = "{}"
# create an instance of RuleBasedBudget from a JSON string
rule_based_budget_instance = RuleBasedBudget.from_json(json)
# print the JSON string representation of the object
print(RuleBasedBudget.to_json())

# convert the object into a dict
rule_based_budget_dict = rule_based_budget_instance.to_dict()
# create an instance of RuleBasedBudget from a dict
rule_based_budget_from_dict = RuleBasedBudget.from_dict(rule_based_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


