# AccountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketplace_string_id** | **str** | The identifier of the marketplace to which the account is associated. | [optional] [readonly] 
**id** | **str** | Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace. | [optional] [readonly] 
**type** | [**AccountType**](AccountType.md) |  | [optional] 
**name** | **str** | Account name. | [optional] [readonly] 
**sub_type** | **str** | The account subtype. | [optional] [readonly] 
**valid_payment_method** | **bool** | Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not. | [optional] [readonly] 

## Example

```python
from openapi_client.models.account_info import AccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfo from a JSON string
account_info_instance = AccountInfo.from_json(json)
# print the JSON string representation of the object
print(AccountInfo.to_json())

# convert the object into a dict
account_info_dict = account_info_instance.to_dict()
# create an instance of AccountInfo from a dict
account_info_from_dict = AccountInfo.from_dict(account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


