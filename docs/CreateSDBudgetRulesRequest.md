# CreateSDBudgetRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_rules_details** | [**List[SDBudgetRuleDetails]**](SDBudgetRuleDetails.md) | A list of budget rule details. | [optional] 

## Example

```python
from openapi_client.models.create_sd_budget_rules_request import CreateSDBudgetRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSDBudgetRulesRequest from a JSON string
create_sd_budget_rules_request_instance = CreateSDBudgetRulesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSDBudgetRulesRequest.to_json())

# convert the object into a dict
create_sd_budget_rules_request_dict = create_sd_budget_rules_request_instance.to_dict()
# create an instance of CreateSDBudgetRulesRequest from a dict
create_sd_budget_rules_request_from_dict = CreateSDBudgetRulesRequest.from_dict(create_sd_budget_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


