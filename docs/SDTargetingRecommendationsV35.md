# SDTargetingRecommendationsV35

For v3.5 the service will continue to return the recommendations returned for v3.4, return Entertainment targeting recommendations if requested and return asin-less recommendations if a landing page URL was passed in the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDProductRecommendationsV32]**](SDProductRecommendationsV32.md) | List of recommended product targets | [optional] 
**categories** | [**List[SDCategoryRecommendationV33]**](SDCategoryRecommendationV33.md) | List of recommended category targets | [optional] 
**audiences** | [**List[SDAudienceCategoryRecommendations]**](SDAudienceCategoryRecommendations.md) | List of recommended audience targets, broken down by audience category | [optional] 
**content_categories** | [**List[SDContentCategoryRecommendations]**](SDContentCategoryRecommendations.md) | List of recommended entertainment targets | [optional] 
**themes** | [**SDThemeRecommendationsV34**](SDThemeRecommendationsV34.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_v35 import SDTargetingRecommendationsV35

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsV35 from a JSON string
sd_targeting_recommendations_v35_instance = SDTargetingRecommendationsV35.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsV35.to_json())

# convert the object into a dict
sd_targeting_recommendations_v35_dict = sd_targeting_recommendations_v35_instance.to_dict()
# create an instance of SDTargetingRecommendationsV35 from a dict
sd_targeting_recommendations_v35_from_dict = SDTargetingRecommendationsV35.from_dict(sd_targeting_recommendations_v35_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


