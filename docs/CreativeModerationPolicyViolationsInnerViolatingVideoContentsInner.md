# CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewed_video_url** | **str** | Address of the video reviewed during moderation. | [optional] 
**video_evidences** | [**List[CreativeModerationPolicyViolationsInnerViolatingVideoContentsInnerVideoEvidencesInner]**](CreativeModerationPolicyViolationsInnerViolatingVideoContentsInnerVideoEvidencesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.creative_moderation_policy_violations_inner_violating_video_contents_inner import CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner from a JSON string
creative_moderation_policy_violations_inner_violating_video_contents_inner_instance = CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner.from_json(json)
# print the JSON string representation of the object
print(CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner.to_json())

# convert the object into a dict
creative_moderation_policy_violations_inner_violating_video_contents_inner_dict = creative_moderation_policy_violations_inner_violating_video_contents_inner_instance.to_dict()
# create an instance of CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner from a dict
creative_moderation_policy_violations_inner_violating_video_contents_inner_from_dict = CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner.from_dict(creative_moderation_policy_violations_inner_violating_video_contents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


