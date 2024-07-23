# TimeOfDay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | The start time of intra-day budget rule window in the format &#39;hh:mm:ss&#39; | [optional] 
**end_time** | **str** | The end time of intra-day budget rule window in the format &#39;hh:mm:ss&#39;. Required to be greater than start-time. | [optional] 

## Example

```python
from openapi_client.models.time_of_day import TimeOfDay

# TODO update the JSON string below
json = "{}"
# create an instance of TimeOfDay from a JSON string
time_of_day_instance = TimeOfDay.from_json(json)
# print the JSON string representation of the object
print(TimeOfDay.to_json())

# convert the object into a dict
time_of_day_dict = time_of_day_instance.to_dict()
# create an instance of TimeOfDay from a dict
time_of_day_from_dict = TimeOfDay.from_dict(time_of_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


