# BrandSafetyGetResponsePagination

Response pagination info for Brand Safety Deny List GET requests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of deny list domains created by the advertiser | [optional] 
**limit** | **int** | The maximum number of deny list domains returned from GET request | [optional] 
**offset** | **int** | The number of deny list domains skipped | [optional] 

## Example

```python
from openapi_client.models.brand_safety_get_response_pagination import BrandSafetyGetResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyGetResponsePagination from a JSON string
brand_safety_get_response_pagination_instance = BrandSafetyGetResponsePagination.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyGetResponsePagination.to_json())

# convert the object into a dict
brand_safety_get_response_pagination_dict = brand_safety_get_response_pagination_instance.to_dict()
# create an instance of BrandSafetyGetResponsePagination from a dict
brand_safety_get_response_pagination_from_dict = BrandSafetyGetResponsePagination.from_dict(brand_safety_get_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


