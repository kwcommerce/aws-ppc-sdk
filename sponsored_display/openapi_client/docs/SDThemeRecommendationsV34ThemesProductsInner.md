# SDThemeRecommendationsV34ThemesProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | HTTP status code 200 indicating a successful response for product recommendations. | [optional] 
**name** | **str** | The theme name specified in the request. | [optional] 
**expression** | [**List[SDProductTargetingThemeExpression]**](SDProductTargetingThemeExpression.md) | A list of expressions defining the product targeting theme. The list will define an AND operator on different expressions. For example, asinPriceGreaterThan and asinReviewRatingLessThan can be used to request product recommendations which are both with greater price and less review rating compared to the goal products. Note: currently the service only support one item in the array. | [optional] 
**recommendations** | [**List[SDProductRecommendationV32]**](SDProductRecommendationV32.md) | A list of recommended products. | [optional] 

## Example

```python
from openapi_client.models.sd_theme_recommendations_v34_themes_products_inner import SDThemeRecommendationsV34ThemesProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SDThemeRecommendationsV34ThemesProductsInner from a JSON string
sd_theme_recommendations_v34_themes_products_inner_instance = SDThemeRecommendationsV34ThemesProductsInner.from_json(json)
# print the JSON string representation of the object
print(SDThemeRecommendationsV34ThemesProductsInner.to_json())

# convert the object into a dict
sd_theme_recommendations_v34_themes_products_inner_dict = sd_theme_recommendations_v34_themes_products_inner_instance.to_dict()
# create an instance of SDThemeRecommendationsV34ThemesProductsInner from a dict
sd_theme_recommendations_v34_themes_products_inner_from_dict = SDThemeRecommendationsV34ThemesProductsInner.from_dict(sd_theme_recommendations_v34_themes_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


