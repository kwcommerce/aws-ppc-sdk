# CallToActionProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_form_id** | **str** | Unique identifier of the lead form associated with the creative. The lead form will be visible upon clicking the CTA button or link. | [optional] 

## Example

```python
from openapi_client.models.call_to_action_properties import CallToActionProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CallToActionProperties from a JSON string
call_to_action_properties_instance = CallToActionProperties.from_json(json)
# print the JSON string representation of the object
print(CallToActionProperties.to_json())

# convert the object into a dict
call_to_action_properties_dict = call_to_action_properties_instance.to_dict()
# create an instance of CallToActionProperties from a dict
call_to_action_properties_from_dict = CallToActionProperties.from_dict(call_to_action_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


