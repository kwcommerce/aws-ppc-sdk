# SDErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of the response. | [optional] 
**details** | **str** | A human-readable description of the response. | [optional] 

## Example

```python
from openapi_client.models.sd_error_response import SDErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SDErrorResponse from a JSON string
sd_error_response_instance = SDErrorResponse.from_json(json)
# print the JSON string representation of the object
print(SDErrorResponse.to_json())

# convert the object into a dict
sd_error_response_dict = sd_error_response_instance.to_dict()
# create an instance of SDErrorResponse from a dict
sd_error_response_from_dict = SDErrorResponse.from_dict(sd_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


