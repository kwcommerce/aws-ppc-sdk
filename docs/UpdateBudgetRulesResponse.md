# UpdateBudgetRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[BudgetRuleResponse]**](BudgetRuleResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_budget_rules_response import UpdateBudgetRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBudgetRulesResponse from a JSON string
update_budget_rules_response_instance = UpdateBudgetRulesResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateBudgetRulesResponse.to_json())

# convert the object into a dict
update_budget_rules_response_dict = update_budget_rules_response_instance.to_dict()
# create an instance of UpdateBudgetRulesResponse from a dict
update_budget_rules_response_from_dict = UpdateBudgetRulesResponse.from_dict(update_budget_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


