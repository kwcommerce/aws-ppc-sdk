# UpdateSDBudgetRulesRequest

Request object for updating budget rule for SD campaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_rules_details** | [**List[SDBudgetRule]**](SDBudgetRule.md) | A list of budget rule details. | [optional] 

## Example

```python
from openapi_client.models.update_sd_budget_rules_request import UpdateSDBudgetRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSDBudgetRulesRequest from a JSON string
update_sd_budget_rules_request_instance = UpdateSDBudgetRulesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSDBudgetRulesRequest.to_json())

# convert the object into a dict
update_sd_budget_rules_request_dict = update_sd_budget_rules_request_instance.to_dict()
# create an instance of UpdateSDBudgetRulesRequest from a dict
update_sd_budget_rules_request_from_dict = UpdateSDBudgetRulesRequest.from_dict(update_sd_budget_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


