# BrandSafetyDenyListDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The website or app identifier. This can be in the form of full domain (eg. &#39;example.com&#39; or &#39;example.net&#39;), or mobile app identifier (eg. &#39;com.example.app&#39; for Android apps or &#39;1234567890&#39; for iOS apps)  | 
**type** | [**BrandSafetyDenyListDomainType**](BrandSafetyDenyListDomainType.md) |  | 

## Example

```python
from openapi_client.models.brand_safety_deny_list_domain import BrandSafetyDenyListDomain

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyDenyListDomain from a JSON string
brand_safety_deny_list_domain_instance = BrandSafetyDenyListDomain.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyDenyListDomain.to_json())

# convert the object into a dict
brand_safety_deny_list_domain_dict = brand_safety_deny_list_domain_instance.to_dict()
# create an instance of BrandSafetyDenyListDomain from a dict
brand_safety_deny_list_domain_from_dict = BrandSafetyDenyListDomain.from_dict(brand_safety_deny_list_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


