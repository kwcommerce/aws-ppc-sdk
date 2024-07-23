# BrandSafetyRequestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**BrandSafetyDenyListDomainUpdateResultStatus**](BrandSafetyDenyListDomainUpdateResultStatus.md) |  | [optional] [default to BrandSafetyDenyListDomainUpdateResultStatus.SUCCESS]
**details** | **str** | A human-readable description of the response. | [optional] 
**domain_id** | **int** | The identifier of the Brand Safety Deny List Domain. | [optional] 
**name** | **str** | The website or app identifier. | [optional] 

## Example

```python
from openapi_client.models.brand_safety_request_result import BrandSafetyRequestResult

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyRequestResult from a JSON string
brand_safety_request_result_instance = BrandSafetyRequestResult.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyRequestResult.to_json())

# convert the object into a dict
brand_safety_request_result_dict = brand_safety_request_result_instance.to_dict()
# create an instance of BrandSafetyRequestResult from a dict
brand_safety_request_result_from_dict = BrandSafetyRequestResult.from_dict(brand_safety_request_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


