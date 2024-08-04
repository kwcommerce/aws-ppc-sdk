# SDCategoryRecommendationTargetableAsinCountRange

The range of ASINs available within the category catalogue. If no targetable ASIN counts are available then the targetableAsinCountRange value will be null without any properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_lower** | **int** |  | [optional] 
**range_upper** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.sd_category_recommendation_targetable_asin_count_range import SDCategoryRecommendationTargetableAsinCountRange

# TODO update the JSON string below
json = "{}"
# create an instance of SDCategoryRecommendationTargetableAsinCountRange from a JSON string
sd_category_recommendation_targetable_asin_count_range_instance = SDCategoryRecommendationTargetableAsinCountRange.from_json(json)
# print the JSON string representation of the object
print(SDCategoryRecommendationTargetableAsinCountRange.to_json())

# convert the object into a dict
sd_category_recommendation_targetable_asin_count_range_dict = sd_category_recommendation_targetable_asin_count_range_instance.to_dict()
# create an instance of SDCategoryRecommendationTargetableAsinCountRange from a dict
sd_category_recommendation_targetable_asin_count_range_from_dict = SDCategoryRecommendationTargetableAsinCountRange.from_dict(sd_category_recommendation_targetable_asin_count_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


