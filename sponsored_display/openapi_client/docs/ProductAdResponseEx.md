# ProductAdResponseEx


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_id** | **float** | The identifier of the ad. | [optional] 
**ad_group_id** | **float** | The identifier of the ad group associated with the ad. | [optional] 
**campaign_id** | **float** | The identifier of the campaign associated with the ad. | [optional] 
**landing_page_url** | **str** | The URL where customers will land after clicking on its link. Must be provided if a LandingPageType is set. Please note that if a single product ad sets the landing page url, only one product ad can be added to the ad group. This field is not supported when using ASIN or SKU fields. ||Specifications| |------------------|------------------| |LandingPageType| Description| |STORE| The url should be in the format of https://www.amazon.com/stores/* (using a correct Amazon url based on the marketplace)| |OFF_AMAZON_LINK| The url should be in the format of https://www.****.com. Note that this LandingPageType is not supported when using ASIN or SKU fields. A custom creative of headline, logo, image are require for this LandingPageType. | |MOMENT| Not yet supported. The url should be in the format of https://www.amazon.com/moments/promotion/{campaignId} (using a correct Amazon url based on the marketplace)| | [optional] 
**landing_page_type** | [**LandingPageType**](LandingPageType.md) |  | [optional] 
**ad_name** | **str** | The name of the ad. Note that this field is not supported when using ASIN or SKU fields. | [optional] 
**asin** | **str** | The ASIN of the product being advertised. This parameter is included in the response for sellers and vendors. | [optional] 
**sku** | **str** | The SKU of the product being advertised. This parameter is included in the response for sellers. | [optional] 
**state** | **str** | The state of the product ad. | [optional] 
**serving_status** | **str** | The status of the product ad. | [optional] 
**creation_date** | **int** | Epoch date the product ad was created. | [optional] 
**last_updated_date** | **int** | Epoch date of the last update to any property associated with the product ad. | [optional] 

## Example

```python
from openapi_client.models.product_ad_response_ex import ProductAdResponseEx

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAdResponseEx from a JSON string
product_ad_response_ex_instance = ProductAdResponseEx.from_json(json)
# print the JSON string representation of the object
print(ProductAdResponseEx.to_json())

# convert the object into a dict
product_ad_response_ex_dict = product_ad_response_ex_instance.to_dict()
# create an instance of ProductAdResponseEx from a dict
product_ad_response_ex_from_dict = ProductAdResponseEx.from_dict(product_ad_response_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


