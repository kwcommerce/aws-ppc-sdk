# BrandSafetyUpdateResponse

Response for Brand Safety POST and DELETE requests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The identifier of the request | [optional] 

## Example

```python
from openapi_client.models.brand_safety_update_response import BrandSafetyUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyUpdateResponse from a JSON string
brand_safety_update_response_instance = BrandSafetyUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyUpdateResponse.to_json())

# convert the object into a dict
brand_safety_update_response_dict = brand_safety_update_response_instance.to_dict()
# create an instance of BrandSafetyUpdateResponse from a dict
brand_safety_update_response_from_dict = BrandSafetyUpdateResponse.from_dict(brand_safety_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


