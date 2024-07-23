# CallToAction

Details of a call-to-action (CTA) button or link displayed on the ad. This is required when \"leads\" optimization type is selected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_to_action_type** | [**CallToActionType**](CallToActionType.md) |  | [optional] 
**properties** | [**CallToActionProperties**](CallToActionProperties.md) |  | [optional] 

## Example

```python
from openapi_client.models.call_to_action import CallToAction

# TODO update the JSON string below
json = "{}"
# create an instance of CallToAction from a JSON string
call_to_action_instance = CallToAction.from_json(json)
# print the JSON string representation of the object
print(CallToAction.to_json())

# convert the object into a dict
call_to_action_dict = call_to_action_instance.to_dict()
# create an instance of CallToAction from a dict
call_to_action_from_dict = CallToAction.from_dict(call_to_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


