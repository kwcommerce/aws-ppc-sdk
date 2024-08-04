# BudgetUsageError

The Error Response Object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | An enumerated error code for machine use. | [optional] 
**details** | **str** | A human-readable description of the response. | [optional] 

## Example

```python
from openapi_client.models.budget_usage_error import BudgetUsageError

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUsageError from a JSON string
budget_usage_error_instance = BudgetUsageError.from_json(json)
# print the JSON string representation of the object
print(BudgetUsageError.to_json())

# convert the object into a dict
budget_usage_error_dict = budget_usage_error_instance.to_dict()
# create an instance of BudgetUsageError from a dict
budget_usage_error_from_dict = BudgetUsageError.from_dict(budget_usage_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


