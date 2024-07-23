# SDTargetingRecommendationsV32

For v3.2 the service will continue to return the recommendations returned for v3.1 in products field, and return recommendations for contextual targeting themes in themes field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDProductRecommendationV32]**](SDProductRecommendationV32.md) | List of recommended product targets | [optional] 
**categories** | [**List[SDCategoryRecommendation]**](SDCategoryRecommendation.md) | List of recommended category targets | [optional] 
**themes** | [**SDThemeRecommendationsThemes**](SDThemeRecommendationsThemes.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_v32 import SDTargetingRecommendationsV32

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsV32 from a JSON string
sd_targeting_recommendations_v32_instance = SDTargetingRecommendationsV32.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsV32.to_json())

# convert the object into a dict
sd_targeting_recommendations_v32_dict = sd_targeting_recommendations_v32_instance.to_dict()
# create an instance of SDTargetingRecommendationsV32 from a dict
sd_targeting_recommendations_v32_from_dict = SDTargetingRecommendationsV32.from_dict(sd_targeting_recommendations_v32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


