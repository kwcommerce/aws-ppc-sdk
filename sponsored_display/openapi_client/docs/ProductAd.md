# ProductAd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the campaign associated with the product ad. | [optional] 
**ad_id** | **int** | The identifier of the product ad. | [optional] 
**ad_group_id** | **int** | The identifier of the ad group. | [optional] 
**campaign_id** | **int** | The identifier of the campaign. | [optional] 
**landing_page_url** | **str** | The URL where customers will land after clicking on its link. Must be provided if a LandingPageType is set. Please note that if a single product ad sets the landing page url, only one product ad can be added to the ad group. This field is not supported when using ASIN or SKU fields. ||Specifications| |------------------|------------------| |LandingPageType| Description| |STORE| The url should be in the format of https://www.amazon.com/stores/* (using a correct Amazon url based on the marketplace)| |OFF_AMAZON_LINK| The url should be in the format of https://www.****.com. Note that this LandingPageType is not supported when using ASIN or SKU fields. A custom creative of headline, logo, image are require for this LandingPageType. | |MOMENT| Not yet supported. The url should be in the format of https://www.amazon.com/moments/promotion/{campaignId} (using a correct Amazon url based on the marketplace)| | [optional] 
**landing_page_type** | [**LandingPageType**](LandingPageType.md) |  | [optional] 
**ad_name** | **str** | The name of the ad. Note that this field is not supported when using ASIN or SKU fields. | [optional] 
**asin** | **str** | The Amazon ASIN of the product advertised by the product ad. This parameter is included in the response for sellers and vendors. | [optional] 
**sku** | **str** | The Amazon SKU of the product advertised by the product ad. This parameter is included in the response for sellers. | [optional] 

## Example

```python
from openapi_client.models.product_ad import ProductAd

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAd from a JSON string
product_ad_instance = ProductAd.from_json(json)
# print the JSON string representation of the object
print(ProductAd.to_json())

# convert the object into a dict
product_ad_dict = product_ad_instance.to_dict()
# create an instance of ProductAd from a dict
product_ad_from_dict = ProductAd.from_dict(product_ad_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


