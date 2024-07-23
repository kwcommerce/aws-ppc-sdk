# CreativeModerationPolicyViolationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_description** | **str** | A human-readable description of the policy. | [optional] 
**policy_link_url** | **str** | Address of the policy documentation. Follow the link to learn more about the specified policy. | [optional] 
**violating_headline_contents** | [**List[CreativeModerationPolicyViolationsInnerViolatingHeadlineContentsInner]**](CreativeModerationPolicyViolationsInnerViolatingHeadlineContentsInner.md) | Information about the headline text that violates the specified policy. | [optional] 
**violating_brand_logo_contents** | [**List[CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInner]**](CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInner.md) | Information about the brand logo that violates the specified policy. | [optional] 
**violating_custom_image_contents** | [**List[CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInner]**](CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInner.md) | Information about the custom image that violates the specified policy. | [optional] 
**violating_video_contents** | [**List[CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner]**](CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner.md) | Information about the video that violates the specified policy. | [optional] 

## Example

```python
from openapi_client.models.creative_moderation_policy_violations_inner import CreativeModerationPolicyViolationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreativeModerationPolicyViolationsInner from a JSON string
creative_moderation_policy_violations_inner_instance = CreativeModerationPolicyViolationsInner.from_json(json)
# print the JSON string representation of the object
print(CreativeModerationPolicyViolationsInner.to_json())

# convert the object into a dict
creative_moderation_policy_violations_inner_dict = creative_moderation_policy_violations_inner_instance.to_dict()
# create an instance of CreativeModerationPolicyViolationsInner from a dict
creative_moderation_policy_violations_inner_from_dict = CreativeModerationPolicyViolationsInner.from_dict(creative_moderation_policy_violations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


