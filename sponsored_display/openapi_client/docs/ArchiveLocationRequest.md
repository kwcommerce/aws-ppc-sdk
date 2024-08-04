# ArchiveLocationRequest

Request body for the Archive Locations API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_expression_id_filter** | [**LocationExpressionIdFilter**](LocationExpressionIdFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.archive_location_request import ArchiveLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveLocationRequest from a JSON string
archive_location_request_instance = ArchiveLocationRequest.from_json(json)
# print the JSON string representation of the object
print(ArchiveLocationRequest.to_json())

# convert the object into a dict
archive_location_request_dict = archive_location_request_instance.to_dict()
# create an instance of ArchiveLocationRequest from a dict
archive_location_request_from_dict = ArchiveLocationRequest.from_dict(archive_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


