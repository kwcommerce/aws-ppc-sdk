# SDTargetingRecommendationsProductsV31Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | Amazon Standard Identification Number | [optional] 
**landing_page_type** | [**SDLandingPageType**](SDLandingPageType.md) |  | [optional] 
**landing_page_url** | **str** | The URL where customers will land after clicking on its link. Must be provided if landingPageType field is set. This field is not supported when using asin field. ||Specifications| |------------------|------------------| |LandingPageType| Description| |OFF_AMAZON_LINK| The url should be in the format of https://www.****.com.| | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_products_v31_inner import SDTargetingRecommendationsProductsV31Inner

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsProductsV31Inner from a JSON string
sd_targeting_recommendations_products_v31_inner_instance = SDTargetingRecommendationsProductsV31Inner.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsProductsV31Inner.to_json())

# convert the object into a dict
sd_targeting_recommendations_products_v31_inner_dict = sd_targeting_recommendations_products_v31_inner_instance.to_dict()
# create an instance of SDTargetingRecommendationsProductsV31Inner from a dict
sd_targeting_recommendations_products_v31_inner_from_dict = SDTargetingRecommendationsProductsV31Inner.from_dict(sd_targeting_recommendations_products_v31_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


