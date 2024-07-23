# BrandSafetyPostRequest

POST Request for Brand Safety

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[BrandSafetyDenyListDomain]**](BrandSafetyDenyListDomain.md) |  | 

## Example

```python
from openapi_client.models.brand_safety_post_request import BrandSafetyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyPostRequest from a JSON string
brand_safety_post_request_instance = BrandSafetyPostRequest.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyPostRequest.to_json())

# convert the object into a dict
brand_safety_post_request_dict = brand_safety_post_request_instance.to_dict()
# create an instance of BrandSafetyPostRequest from a dict
brand_safety_post_request_from_dict = BrandSafetyPostRequest.from_dict(brand_safety_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


