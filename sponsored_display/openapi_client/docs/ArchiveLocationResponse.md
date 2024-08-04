# ArchiveLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Returns \&quot;SUCCESS\&quot; for a successful response, otherwise a HTTP error code | [optional] 
**description** | **str** | A human-readable description of the response if there is an error | [optional] 
**location_expression_id** | **int** | The identifier of the location. | [optional] 

## Example

```python
from openapi_client.models.archive_location_response import ArchiveLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveLocationResponse from a JSON string
archive_location_response_instance = ArchiveLocationResponse.from_json(json)
# print the JSON string representation of the object
print(ArchiveLocationResponse.to_json())

# convert the object into a dict
archive_location_response_dict = archive_location_response_instance.to_dict()
# create an instance of ArchiveLocationResponse from a dict
archive_location_response_from_dict = ArchiveLocationResponse.from_dict(archive_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


