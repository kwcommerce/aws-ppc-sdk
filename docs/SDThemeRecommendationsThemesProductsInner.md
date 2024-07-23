# SDThemeRecommendationsThemesProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | HTTP status code 200 indicating a successful response for product recomendations. | [optional] 
**name** | **str** | The theme name specified in the request. | [optional] 
**recommendations** | [**List[SDProductRecommendationV32]**](SDProductRecommendationV32.md) | A list of recommended products. | [optional] 

## Example

```python
from openapi_client.models.sd_theme_recommendations_themes_products_inner import SDThemeRecommendationsThemesProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SDThemeRecommendationsThemesProductsInner from a JSON string
sd_theme_recommendations_themes_products_inner_instance = SDThemeRecommendationsThemesProductsInner.from_json(json)
# print the JSON string representation of the object
print(SDThemeRecommendationsThemesProductsInner.to_json())

# convert the object into a dict
sd_theme_recommendations_themes_products_inner_dict = sd_theme_recommendations_themes_products_inner_instance.to_dict()
# create an instance of SDThemeRecommendationsThemesProductsInner from a dict
sd_theme_recommendations_themes_products_inner_from_dict = SDThemeRecommendationsThemesProductsInner.from_dict(sd_theme_recommendations_themes_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


