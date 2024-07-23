# SDTargetingRecommendationsV34

For v3.4 the service will continue to return the recommendations returned for v3.2, return audience recommendations if requested, and return the theme expression used in product targeting if requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDProductRecommendationsV32]**](SDProductRecommendationsV32.md) | List of recommended product targets | [optional] 
**categories** | [**List[SDCategoryRecommendationV33]**](SDCategoryRecommendationV33.md) | List of recommended category targets | [optional] 
**audiences** | [**List[SDAudienceCategoryRecommendations]**](SDAudienceCategoryRecommendations.md) | List of recommended audience targets, broken down by audience category | [optional] 
**themes** | [**SDThemeRecommendationsV34**](SDThemeRecommendationsV34.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_v34 import SDTargetingRecommendationsV34

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsV34 from a JSON string
sd_targeting_recommendations_v34_instance = SDTargetingRecommendationsV34.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsV34.to_json())

# convert the object into a dict
sd_targeting_recommendations_v34_dict = sd_targeting_recommendations_v34_instance.to_dict()
# create an instance of SDTargetingRecommendationsV34 from a dict
sd_targeting_recommendations_v34_from_dict = SDTargetingRecommendationsV34.from_dict(sd_targeting_recommendations_v34_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


