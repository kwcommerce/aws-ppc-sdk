# SDCategoryRecommendation

A recommended category to target ads on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **int** | The category identifier | [optional] 
**name** | **str** | The category name | [optional] 
**path** | **List[str]** | The path of the category within the category catalogue. | [optional] 
**targetable_asin_count_range** | [**SDCategoryRecommendationTargetableAsinCountRange**](SDCategoryRecommendationTargetableAsinCountRange.md) |  | [optional] 
**rank** | **int** | A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation | [optional] 

## Example

```python
from openapi_client.models.sd_category_recommendation import SDCategoryRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of SDCategoryRecommendation from a JSON string
sd_category_recommendation_instance = SDCategoryRecommendation.from_json(json)
# print the JSON string representation of the object
print(SDCategoryRecommendation.to_json())

# convert the object into a dict
sd_category_recommendation_dict = sd_category_recommendation_instance.to_dict()
# create an instance of SDCategoryRecommendation from a dict
sd_category_recommendation_from_dict = SDCategoryRecommendation.from_dict(sd_category_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


