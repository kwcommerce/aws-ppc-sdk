# CreativeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of the response. | [optional] 
**description** | **str** | A human-readable description of the response. | [optional] 
**creative_id** | **float** | The identifier of the creative. | [optional] 

## Example

```python
from openapi_client.models.creative_response import CreativeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreativeResponse from a JSON string
creative_response_instance = CreativeResponse.from_json(json)
# print the JSON string representation of the object
print(CreativeResponse.to_json())

# convert the object into a dict
creative_response_dict = creative_response_instance.to_dict()
# create an instance of CreativeResponse from a dict
creative_response_from_dict = CreativeResponse.from_dict(creative_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


