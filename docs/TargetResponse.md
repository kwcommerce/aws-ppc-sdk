# TargetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of the response. | [optional] 
**description** | **str** | A human-readable description of the response. | [optional] 
**target_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.target_response import TargetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TargetResponse from a JSON string
target_response_instance = TargetResponse.from_json(json)
# print the JSON string representation of the object
print(TargetResponse.to_json())

# convert the object into a dict
target_response_dict = target_response_instance.to_dict()
# create an instance of TargetResponse from a dict
target_response_from_dict = TargetResponse.from_dict(target_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


