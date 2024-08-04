# RuleDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type_rule_duration** | [**EventTypeRuleDuration**](EventTypeRuleDuration.md) |  | [optional] 
**date_range_type_rule_duration** | [**DateRangeTypeRuleDuration**](DateRangeTypeRuleDuration.md) |  | [optional] 

## Example

```python
from openapi_client.models.rule_duration import RuleDuration

# TODO update the JSON string below
json = "{}"
# create an instance of RuleDuration from a JSON string
rule_duration_instance = RuleDuration.from_json(json)
# print the JSON string representation of the object
print(RuleDuration.to_json())

# convert the object into a dict
rule_duration_dict = rule_duration_instance.to_dict()
# create an instance of RuleDuration from a dict
rule_duration_from_dict = RuleDuration.from_dict(rule_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


