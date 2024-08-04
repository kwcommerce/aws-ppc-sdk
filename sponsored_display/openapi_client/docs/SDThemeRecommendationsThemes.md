# SDThemeRecommendationsThemes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDThemeRecommendationsThemesProductsInner]**](SDThemeRecommendationsThemesProductsInner.md) | A list of contextual targeting theme recommendations. | [optional] 

## Example

```python
from openapi_client.models.sd_theme_recommendations_themes import SDThemeRecommendationsThemes

# TODO update the JSON string below
json = "{}"
# create an instance of SDThemeRecommendationsThemes from a JSON string
sd_theme_recommendations_themes_instance = SDThemeRecommendationsThemes.from_json(json)
# print the JSON string representation of the object
print(SDThemeRecommendationsThemes.to_json())

# convert the object into a dict
sd_theme_recommendations_themes_dict = sd_theme_recommendations_themes_instance.to_dict()
# create an instance of SDThemeRecommendationsThemes from a dict
sd_theme_recommendations_themes_from_dict = SDThemeRecommendationsThemes.from_dict(sd_theme_recommendations_themes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


