# CreativePreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_html** | **str** |  | 
**preview_htmls** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.creative_preview_response import CreativePreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreativePreviewResponse from a JSON string
creative_preview_response_instance = CreativePreviewResponse.from_json(json)
# print the JSON string representation of the object
print(CreativePreviewResponse.to_json())

# convert the object into a dict
creative_preview_response_dict = creative_preview_response_instance.to_dict()
# create an instance of CreativePreviewResponse from a dict
creative_preview_response_from_dict = CreativePreviewResponse.from_dict(creative_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


