# UpdateProductAd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the campaign associated with the product ad. | [optional] 
**ad_id** | **int** | The identifier of the product ad. | 

## Example

```python
from openapi_client.models.update_product_ad import UpdateProductAd

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductAd from a JSON string
update_product_ad_instance = UpdateProductAd.from_json(json)
# print the JSON string representation of the object
print(UpdateProductAd.to_json())

# convert the object into a dict
update_product_ad_dict = update_product_ad_instance.to_dict()
# create an instance of UpdateProductAd from a dict
update_product_ad_from_dict = UpdateProductAd.from_dict(update_product_ad_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


