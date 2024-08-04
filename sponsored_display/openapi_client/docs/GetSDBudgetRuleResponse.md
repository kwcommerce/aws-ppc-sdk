# GetSDBudgetRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_rule** | [**SDBudgetRule**](SDBudgetRule.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_sd_budget_rule_response import GetSDBudgetRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSDBudgetRuleResponse from a JSON string
get_sd_budget_rule_response_instance = GetSDBudgetRuleResponse.from_json(json)
# print the JSON string representation of the object
print(GetSDBudgetRuleResponse.to_json())

# convert the object into a dict
get_sd_budget_rule_response_dict = get_sd_budget_rule_response_instance.to_dict()
# create an instance of GetSDBudgetRuleResponse from a dict
get_sd_budget_rule_response_from_dict = GetSDBudgetRuleResponse.from_dict(get_sd_budget_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


