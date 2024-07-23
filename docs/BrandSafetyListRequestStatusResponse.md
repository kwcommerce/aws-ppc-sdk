# BrandSafetyListRequestStatusResponse

List of all requests' status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_status_list** | [**List[BrandSafetyRequestStatus]**](BrandSafetyRequestStatus.md) | List of all requests&#39; status. | [optional] 

## Example

```python
from openapi_client.models.brand_safety_list_request_status_response import BrandSafetyListRequestStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyListRequestStatusResponse from a JSON string
brand_safety_list_request_status_response_instance = BrandSafetyListRequestStatusResponse.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyListRequestStatusResponse.to_json())

# convert the object into a dict
brand_safety_list_request_status_response_dict = brand_safety_list_request_status_response_instance.to_dict()
# create an instance of BrandSafetyListRequestStatusResponse from a dict
brand_safety_list_request_status_response_from_dict = BrandSafetyListRequestStatusResponse.from_dict(brand_safety_list_request_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


