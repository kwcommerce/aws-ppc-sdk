# Recurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RecurrenceType**](RecurrenceType.md) |  | [optional] 
**days_of_week** | [**List[DayOfWeek]**](DayOfWeek.md) | Object representing days of the week for weekly type rule. It is not required for daily recurrence type | [optional] 
**intra_day_schedule** | [**List[TimeOfDay]**](TimeOfDay.md) | List of objects representing start and end time of desired intra-day budget rule window | [optional] 

## Example

```python
from openapi_client.models.recurrence import Recurrence

# TODO update the JSON string below
json = "{}"
# create an instance of Recurrence from a JSON string
recurrence_instance = Recurrence.from_json(json)
# print the JSON string representation of the object
print(Recurrence.to_json())

# convert the object into a dict
recurrence_dict = recurrence_instance.to_dict()
# create an instance of Recurrence from a dict
recurrence_from_dict = Recurrence.from_dict(recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


