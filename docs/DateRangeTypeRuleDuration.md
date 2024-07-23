# DateRangeTypeRuleDuration

Object representing date range type rule duration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than &#x60;startDate&#x60;. | [optional] 
**start_date** | **str** | The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date. | 

## Example

```python
from openapi_client.models.date_range_type_rule_duration import DateRangeTypeRuleDuration

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeTypeRuleDuration from a JSON string
date_range_type_rule_duration_instance = DateRangeTypeRuleDuration.from_json(json)
# print the JSON string representation of the object
print(DateRangeTypeRuleDuration.to_json())

# convert the object into a dict
date_range_type_rule_duration_dict = date_range_type_rule_duration_instance.to_dict()
# create an instance of DateRangeTypeRuleDuration from a dict
date_range_type_rule_duration_from_dict = DateRangeTypeRuleDuration.from_dict(date_range_type_rule_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


