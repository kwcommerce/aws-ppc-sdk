# BrandSafetyDenyListProcessedDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **int** | The identifier of the Brand Safety List domain. | [optional] 
**name** | **str** | The website or app identifier. This can be in the form of full domain (eg. &#39;example.com&#39; or &#39;example.net&#39;), or mobile app identifier (eg. &#39;com.example.app&#39; for Android apps or &#39;1234567890&#39; for iOS apps)  | [optional] 
**type** | [**BrandSafetyDenyListDomainType**](BrandSafetyDenyListDomainType.md) |  | [optional] 
**state** | [**BrandSafetyDenyListDomainState**](BrandSafetyDenyListDomainState.md) |  | [optional] [default to BrandSafetyDenyListDomainState.ENABLED]
**created_at** | **datetime** | The date time the domain was created at. Format YYYY-MM-ddT:HH:mm:ssZ | [optional] 
**last_modified** | **datetime** | The date time the domain was last modified. Format YYYY-MM-ddT:HH:mm:ssZ | [optional] 

## Example

```python
from openapi_client.models.brand_safety_deny_list_processed_domain import BrandSafetyDenyListProcessedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyDenyListProcessedDomain from a JSON string
brand_safety_deny_list_processed_domain_instance = BrandSafetyDenyListProcessedDomain.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyDenyListProcessedDomain.to_json())

# convert the object into a dict
brand_safety_deny_list_processed_domain_dict = brand_safety_deny_list_processed_domain_instance.to_dict()
# create an instance of BrandSafetyDenyListProcessedDomain from a dict
brand_safety_deny_list_processed_domain_from_dict = BrandSafetyDenyListProcessedDomain.from_dict(brand_safety_deny_list_processed_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


