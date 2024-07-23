# SDCategoryRecommendationV33

A recommended category to target ads on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **int** | The category identifier | [optional] 
**name** | **str** | The category name | [optional] 
**translated_name** | **str** | The translated category name by requested locale, field will not be provided if locale is not provided or campaign localization service is down. | [optional] 
**path** | **List[str]** | The path of the category within the category catalogue. | [optional] 
**translated_path** | **List[str]** | The translated path of the category within the category catalogue by requested locale, field will not be provided if locale is not provided or campaign localization is down. | [optional] 
**targetable_asin_count_range** | [**SDCategoryRecommendationV33TargetableAsinCountRange**](SDCategoryRecommendationV33TargetableAsinCountRange.md) |  | [optional] 
**rank** | **int** | A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation. | [optional] 

## Example

```python
from openapi_client.models.sd_category_recommendation_v33 import SDCategoryRecommendationV33

# TODO update the JSON string below
json = "{}"
# create an instance of SDCategoryRecommendationV33 from a JSON string
sd_category_recommendation_v33_instance = SDCategoryRecommendationV33.from_json(json)
# print the JSON string representation of the object
print(SDCategoryRecommendationV33.to_json())

# convert the object into a dict
sd_category_recommendation_v33_dict = sd_category_recommendation_v33_instance.to_dict()
# create an instance of SDCategoryRecommendationV33 from a dict
sd_category_recommendation_v33_from_dict = SDCategoryRecommendationV33.from_dict(sd_category_recommendation_v33_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


