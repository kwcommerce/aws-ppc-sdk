# SDBudgetRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_state** | [**State**](State.md) |  | [optional] 
**last_updated_date** | **float** | Epoch time of budget rule update. Read-only. | [optional] 
**created_date** | **float** | Epoch time of budget rule creation. Read-only. | [optional] 
**rule_details** | [**SDBudgetRuleDetails**](SDBudgetRuleDetails.md) |  | [optional] 
**rule_id** | **str** | The budget rule identifier. | 
**rule_status** | **str** | The budget rule status. Read-only. | [optional] 

## Example

```python
from openapi_client.models.sd_budget_rule import SDBudgetRule

# TODO update the JSON string below
json = "{}"
# create an instance of SDBudgetRule from a JSON string
sd_budget_rule_instance = SDBudgetRule.from_json(json)
# print the JSON string representation of the object
print(SDBudgetRule.to_json())

# convert the object into a dict
sd_budget_rule_dict = sd_budget_rule_instance.to_dict()
# create an instance of SDBudgetRule from a dict
sd_budget_rule_from_dict = SDBudgetRule.from_dict(sd_budget_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


