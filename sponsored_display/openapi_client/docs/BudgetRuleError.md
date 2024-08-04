# BudgetRuleError

The Error Response Object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | An enumerated error code for machine use. | [optional] 
**details** | **str** | A human-readable description of the response. | [optional] 

## Example

```python
from openapi_client.models.budget_rule_error import BudgetRuleError

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetRuleError from a JSON string
budget_rule_error_instance = BudgetRuleError.from_json(json)
# print the JSON string representation of the object
print(BudgetRuleError.to_json())

# convert the object into a dict
budget_rule_error_dict = budget_rule_error_instance.to_dict()
# create an instance of BudgetRuleError from a dict
budget_rule_error_from_dict = BudgetRuleError.from_dict(budget_rule_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


