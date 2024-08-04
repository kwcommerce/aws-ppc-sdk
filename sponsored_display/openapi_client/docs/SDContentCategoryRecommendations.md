# SDContentCategoryRecommendations

A recommended content category to target ads on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_category** | **str** | The content category value | [optional] 
**name** | **str** | The content category name | [optional] 
**rank** | **int** | A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation | [optional] 

## Example

```python
from openapi_client.models.sd_content_category_recommendations import SDContentCategoryRecommendations

# TODO update the JSON string below
json = "{}"
# create an instance of SDContentCategoryRecommendations from a JSON string
sd_content_category_recommendations_instance = SDContentCategoryRecommendations.from_json(json)
# print the JSON string representation of the object
print(SDContentCategoryRecommendations.to_json())

# convert the object into a dict
sd_content_category_recommendations_dict = sd_content_category_recommendations_instance.to_dict()
# create an instance of SDContentCategoryRecommendations from a dict
sd_content_category_recommendations_from_dict = SDContentCategoryRecommendations.from_dict(sd_content_category_recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


