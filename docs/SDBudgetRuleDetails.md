# SDBudgetRuleDetails

Object representing details of a budget rule for SD campaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | [**RuleDuration**](RuleDuration.md) |  | [optional] 
**recurrence** | [**Recurrence**](Recurrence.md) |  | [optional] 
**rule_type** | [**SDRuleType**](SDRuleType.md) |  | [optional] 
**budget_increase_by** | [**BudgetIncreaseBy**](BudgetIncreaseBy.md) |  | [optional] 
**name** | **str** | The budget rule name. Required to be unique within a campaign. | [optional] 
**performance_measure_condition** | [**PerformanceMeasureCondition**](PerformanceMeasureCondition.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_budget_rule_details import SDBudgetRuleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SDBudgetRuleDetails from a JSON string
sd_budget_rule_details_instance = SDBudgetRuleDetails.from_json(json)
# print the JSON string representation of the object
print(SDBudgetRuleDetails.to_json())

# convert the object into a dict
sd_budget_rule_details_dict = sd_budget_rule_details_instance.to_dict()
# create an instance of SDBudgetRuleDetails from a dict
sd_budget_rule_details_from_dict = SDBudgetRuleDetails.from_dict(sd_budget_rule_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


