# Creative

Creative model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creative_id** | **float** | Unique identifier of the creative. | 
**ad_group_id** | **int** | The identifier of the ad group. | 
**creative_type** | [**CreativeTypeInCreativeResponse**](CreativeTypeInCreativeResponse.md) |  | 
**properties** | [**CreativeProperties**](CreativeProperties.md) |  | 
**moderation_status** | **str** | The moderation status of the creative | 

## Example

```python
from openapi_client.models.creative import Creative

# TODO update the JSON string below
json = "{}"
# create an instance of Creative from a JSON string
creative_instance = Creative.from_json(json)
# print the JSON string representation of the object
print(Creative.to_json())

# convert the object into a dict
creative_dict = creative_instance.to_dict()
# create an instance of Creative from a dict
creative_from_dict = Creative.from_dict(creative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


