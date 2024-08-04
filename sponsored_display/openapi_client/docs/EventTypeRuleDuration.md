# EventTypeRuleDuration

Object representing event type rule duration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The event identifier. This value is available from the budget rules recommendation API. | 
**end_date** | **str** | The event end date in YYYYMMDD format. Read-only. | [optional] 
**event_name** | **str** | The event name. Read-only. | [optional] 
**start_date** | **str** | The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events. | [optional] 

## Example

```python
from openapi_client.models.event_type_rule_duration import EventTypeRuleDuration

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypeRuleDuration from a JSON string
event_type_rule_duration_instance = EventTypeRuleDuration.from_json(json)
# print the JSON string representation of the object
print(EventTypeRuleDuration.to_json())

# convert the object into a dict
event_type_rule_duration_dict = event_type_rule_duration_instance.to_dict()
# create an instance of EventTypeRuleDuration from a dict
event_type_rule_duration_from_dict = EventTypeRuleDuration.from_dict(event_type_rule_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


