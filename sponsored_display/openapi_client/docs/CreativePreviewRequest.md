# CreativePreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creative** | [**PreviewCreativeModel**](PreviewCreativeModel.md) |  | 
**preview_configuration** | [**CreativePreviewConfiguration**](CreativePreviewConfiguration.md) |  | 
**preview_configurations** | [**List[CreativePreviewConfiguration]**](CreativePreviewConfiguration.md) |  | [optional] 

## Example

```python
from openapi_client.models.creative_preview_request import CreativePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreativePreviewRequest from a JSON string
creative_preview_request_instance = CreativePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(CreativePreviewRequest.to_json())

# convert the object into a dict
creative_preview_request_dict = creative_preview_request_instance.to_dict()
# create an instance of CreativePreviewRequest from a dict
creative_preview_request_from_dict = CreativePreviewRequest.from_dict(creative_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


