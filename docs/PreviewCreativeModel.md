# PreviewCreativeModel

Creative model for preview.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creative_type** | [**CreativeTypeInCreativeRequest**](CreativeTypeInCreativeRequest.md) |  | [optional] 
**properties** | [**CreativeProperties**](CreativeProperties.md) |  | [optional] 

## Example

```python
from openapi_client.models.preview_creative_model import PreviewCreativeModel

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewCreativeModel from a JSON string
preview_creative_model_instance = PreviewCreativeModel.from_json(json)
# print the JSON string representation of the object
print(PreviewCreativeModel.to_json())

# convert the object into a dict
preview_creative_model_dict = preview_creative_model_instance.to_dict()
# create an instance of PreviewCreativeModel from a dict
preview_creative_model_from_dict = PreviewCreativeModel.from_dict(preview_creative_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


