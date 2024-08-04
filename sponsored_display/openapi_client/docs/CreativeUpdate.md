# CreativeUpdate

Creative update model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creative_id** | **float** | Unique identifier of the creative. | 
**creative_type** | [**CreativeTypeInCreativeRequest**](CreativeTypeInCreativeRequest.md) |  | [optional] 
**properties** | [**CreativeProperties**](CreativeProperties.md) |  | 

## Example

```python
from openapi_client.models.creative_update import CreativeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CreativeUpdate from a JSON string
creative_update_instance = CreativeUpdate.from_json(json)
# print the JSON string representation of the object
print(CreativeUpdate.to_json())

# convert the object into a dict
creative_update_dict = creative_update_instance.to_dict()
# create an instance of CreativeUpdate from a dict
creative_update_from_dict = CreativeUpdate.from_dict(creative_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


