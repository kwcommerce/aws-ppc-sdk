# SDTargetingRecommendationsThemes

The themes used to refine the recommendations. Currently only contextual targeting themes are supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**List[SDProductTargetingTheme]**](SDProductTargetingTheme.md) | A list of themes for product targeting recommendations. If this list is empty, the service will return all the current available theme recommendations. Recommendations will be returned for each theme. If specified, each theme should only include unique expressions. | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_themes import SDTargetingRecommendationsThemes

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsThemes from a JSON string
sd_targeting_recommendations_themes_instance = SDTargetingRecommendationsThemes.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsThemes.to_json())

# convert the object into a dict
sd_targeting_recommendations_themes_dict = sd_targeting_recommendations_themes_instance.to_dict()
# create an instance of SDTargetingRecommendationsThemes from a dict
sd_targeting_recommendations_themes_from_dict = SDTargetingRecommendationsThemes.from_dict(sd_targeting_recommendations_themes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


