# SDAudienceCategoryRecommendations

List of recommended standard Amazon audience targets of a specific audience category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**SDAudienceCategory**](SDAudienceCategory.md) |  | [optional] 
**audiences** | [**List[SDAudienceRecommendation]**](SDAudienceRecommendation.md) | List of recommended standard Amazon audience targets | [optional] 

## Example

```python
from openapi_client.models.sd_audience_category_recommendations import SDAudienceCategoryRecommendations

# TODO update the JSON string below
json = "{}"
# create an instance of SDAudienceCategoryRecommendations from a JSON string
sd_audience_category_recommendations_instance = SDAudienceCategoryRecommendations.from_json(json)
# print the JSON string representation of the object
print(SDAudienceCategoryRecommendations.to_json())

# convert the object into a dict
sd_audience_category_recommendations_dict = sd_audience_category_recommendations_instance.to_dict()
# create an instance of SDAudienceCategoryRecommendations from a dict
sd_audience_category_recommendations_from_dict = SDAudienceCategoryRecommendations.from_dict(sd_audience_category_recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


