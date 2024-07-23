# BrandSafetyGetResponse

Response for Brand Safety Deny List GET requests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**BrandSafetyGetResponsePagination**](BrandSafetyGetResponsePagination.md) |  | [optional] 
**domains** | [**List[BrandSafetyDenyListProcessedDomain]**](BrandSafetyDenyListProcessedDomain.md) | List of Brand Safety Deny List Domains | [optional] 

## Example

```python
from openapi_client.models.brand_safety_get_response import BrandSafetyGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyGetResponse from a JSON string
brand_safety_get_response_instance = BrandSafetyGetResponse.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyGetResponse.to_json())

# convert the object into a dict
brand_safety_get_response_dict = brand_safety_get_response_instance.to_dict()
# create an instance of BrandSafetyGetResponse from a dict
brand_safety_get_response_from_dict = BrandSafetyGetResponse.from_dict(brand_safety_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


