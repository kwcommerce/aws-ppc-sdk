# VideoCreativeProperties

User-customizable properties of a video creative.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video** | [**Video**](Video.md) |  | [optional] 

## Example

```python
from openapi_client.models.video_creative_properties import VideoCreativeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of VideoCreativeProperties from a JSON string
video_creative_properties_instance = VideoCreativeProperties.from_json(json)
# print the JSON string representation of the object
print(VideoCreativeProperties.to_json())

# convert the object into a dict
video_creative_properties_dict = video_creative_properties_instance.to_dict()
# create an instance of VideoCreativeProperties from a dict
video_creative_properties_from_dict = VideoCreativeProperties.from_dict(video_creative_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


