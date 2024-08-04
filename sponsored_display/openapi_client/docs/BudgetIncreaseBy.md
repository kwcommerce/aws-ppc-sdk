# BudgetIncreaseBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BudgetChangeType**](BudgetChangeType.md) |  | 
**value** | **float** | The budget value. | 

## Example

```python
from openapi_client.models.budget_increase_by import BudgetIncreaseBy

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetIncreaseBy from a JSON string
budget_increase_by_instance = BudgetIncreaseBy.from_json(json)
# print the JSON string representation of the object
print(BudgetIncreaseBy.to_json())

# convert the object into a dict
budget_increase_by_dict = budget_increase_by_instance.to_dict()
# create an instance of BudgetIncreaseBy from a dict
budget_increase_by_from_dict = BudgetIncreaseBy.from_dict(budget_increase_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


