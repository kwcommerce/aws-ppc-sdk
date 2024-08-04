# BudgetRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | An enumerated success or error code for machine use. | [optional] 
**details** | **str** | A human-readable description of the error, if unsuccessful | [optional] 
**rule_id** | **str** | The rule identifier. | [optional] 
**associated_campaign_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.budget_rule_response import BudgetRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetRuleResponse from a JSON string
budget_rule_response_instance = BudgetRuleResponse.from_json(json)
# print the JSON string representation of the object
print(BudgetRuleResponse.to_json())

# convert the object into a dict
budget_rule_response_dict = budget_rule_response_instance.to_dict()
# create an instance of BudgetRuleResponse from a dict
budget_rule_response_from_dict = BudgetRuleResponse.from_dict(budget_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


