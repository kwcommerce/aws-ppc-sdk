# SDTargetingRecommendationsV33

For v3.3 the service will continue to return the recommendations returned for v3.2, and return audience recommendations if requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDProductRecommendationV32]**](SDProductRecommendationV32.md) | List of recommended product targets | [optional] 
**categories** | [**List[SDCategoryRecommendationV33]**](SDCategoryRecommendationV33.md) | List of recommended category targets. | [optional] 
**audiences** | [**List[SDAudienceCategoryRecommendations]**](SDAudienceCategoryRecommendations.md) | List of recommended audience targets, broken down by audience category | [optional] 
**themes** | [**SDThemeRecommendationsThemes**](SDThemeRecommendationsThemes.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_v33 import SDTargetingRecommendationsV33

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsV33 from a JSON string
sd_targeting_recommendations_v33_instance = SDTargetingRecommendationsV33.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsV33.to_json())

# convert the object into a dict
sd_targeting_recommendations_v33_dict = sd_targeting_recommendations_v33_instance.to_dict()
# create an instance of SDTargetingRecommendationsV33 from a dict
sd_targeting_recommendations_v33_from_dict = SDTargetingRecommendationsV33.from_dict(sd_targeting_recommendations_v33_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


