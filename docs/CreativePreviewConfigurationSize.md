# CreativePreviewConfigurationSize

The slot dimension to render the creative. Sponsored Display creatives are responsive to a limited list of width and height pairs, including 300x250, 650x130, 245x250, 414x125, 600x160, 600x300, 728x90, 980x55, 320x50, 970x250 and 270x150.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.creative_preview_configuration_size import CreativePreviewConfigurationSize

# TODO update the JSON string below
json = "{}"
# create an instance of CreativePreviewConfigurationSize from a JSON string
creative_preview_configuration_size_instance = CreativePreviewConfigurationSize.from_json(json)
# print the JSON string representation of the object
print(CreativePreviewConfigurationSize.to_json())

# convert the object into a dict
creative_preview_configuration_size_dict = creative_preview_configuration_size_instance.to_dict()
# create an instance of CreativePreviewConfigurationSize from a dict
creative_preview_configuration_size_from_dict = CreativePreviewConfigurationSize.from_dict(creative_preview_configuration_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


