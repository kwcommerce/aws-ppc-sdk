# BrandSafetyRequestStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Request ID | [optional] 
**timestamp** | **str** | Request timestamp | [optional] 
**status** | **str** | The status of the request | [optional] 
**status_details** | **str** | Details related to the request status | [optional] 

## Example

```python
from openapi_client.models.brand_safety_request_status import BrandSafetyRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyRequestStatus from a JSON string
brand_safety_request_status_instance = BrandSafetyRequestStatus.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyRequestStatus.to_json())

# convert the object into a dict
brand_safety_request_status_dict = brand_safety_request_status_instance.to_dict()
# create an instance of BrandSafetyRequestStatus from a dict
brand_safety_request_status_from_dict = BrandSafetyRequestStatus.from_dict(brand_safety_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


