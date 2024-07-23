# CreateBudgetRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[BudgetRuleResponse]**](BudgetRuleResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_budget_rules_response import CreateBudgetRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBudgetRulesResponse from a JSON string
create_budget_rules_response_instance = CreateBudgetRulesResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBudgetRulesResponse.to_json())

# convert the object into a dict
create_budget_rules_response_dict = create_budget_rules_response_instance.to_dict()
# create an instance of CreateBudgetRulesResponse from a dict
create_budget_rules_response_from_dict = CreateBudgetRulesResponse.from_dict(create_budget_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


