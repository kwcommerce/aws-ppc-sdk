# Video

This field denotes video which is displayed on the ad. This field is optional and mutable. A video asset must be provided for a VIDEO creative. Specific restrictions based on the video are listed in the following table. ||Specifications| |------------------|------------------| |Maximum file size|500MB| |Aspect ratio|16:9| |Minimum duration|6s| |Maximum duration|45s| |Minimum frame size|1920x1080| |Minimum video bitrate|4mbps| |Video frame rate(fps)|23.976(recommended), 24, 25, or 29.97| |Video frame rate mode|Constant| |Minimum audio bitrate|192kbps| |Audio sample rate|44.1kHz or 48kHz| |Supported Formats|Video: H.264, MPEG-2, or MPEG-4; Audio: PCM or AAC| |Audio Channel|Audio format needs to be stereo or mono.| |Recommended video bitrate|8mbps| |Recommended duration|A duration of exactly 6s, 15s, 20s, or 30s is recommended. Use of videos outside of these durations may negatively impact your campaign performance. Shorter lengths will drive higher VCR (although scale on 6s may be limited).|

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The unique identifier of the video asset. This assetId comes from the Creative Asset Library. | 
**asset_version** | **str** | The identifier of the particular video assetversion. | 

## Example

```python
from openapi_client.models.video import Video

# TODO update the JSON string below
json = "{}"
# create an instance of Video from a JSON string
video_instance = Video.from_json(json)
# print the JSON string representation of the object
print(Video.to_json())

# convert the object into a dict
video_dict = video_instance.to_dict()
# create an instance of Video from a dict
video_from_dict = Video.from_dict(video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


