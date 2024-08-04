# CreativeModeration

System generated Creative moderation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creative_id** | **float** | Unique identifier of the creative. | 
**creative_type** | [**CreativeTypeInCreativeResponse**](CreativeTypeInCreativeResponse.md) |  | 
**moderation_status** | **str** | The moderation status of the creative. |Status|Description| |------|-----------| |APPROVED|Moderation for the creative is complete.| |IN_PROGRESS|Moderation for the creative is in progress. The expected date and time for completion are specfied in the &#x60;etaForModeration&#x60; field.| |REJECTED|The creative has failed moderation. Specific information about the content that violated policy is available in &#x60;policyViolations&#x60;.| | 
**eta_for_moderation** | **datetime** | Expected date and time by which moderation will be complete. | 
**policy_violations** | [**List[CreativeModerationPolicyViolationsInner]**](CreativeModerationPolicyViolationsInner.md) | A list of policy violations for a creative that has failed moderation. | 

## Example

```python
from openapi_client.models.creative_moderation import CreativeModeration

# TODO update the JSON string below
json = "{}"
# create an instance of CreativeModeration from a JSON string
creative_moderation_instance = CreativeModeration.from_json(json)
# print the JSON string representation of the object
print(CreativeModeration.to_json())

# convert the object into a dict
creative_moderation_dict = creative_moderation_instance.to_dict()
# create an instance of CreativeModeration from a dict
creative_moderation_from_dict = CreativeModeration.from_dict(creative_moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


