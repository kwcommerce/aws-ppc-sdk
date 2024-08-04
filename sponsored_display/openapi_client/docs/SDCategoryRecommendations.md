# SDCategoryRecommendations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[SDCategoryRecommendation]**](SDCategoryRecommendation.md) | List of recommended category targets | [optional] 

## Example

```python
from openapi_client.models.sd_category_recommendations import SDCategoryRecommendations

# TODO update the JSON string below
json = "{}"
# create an instance of SDCategoryRecommendations from a JSON string
sd_category_recommendations_instance = SDCategoryRecommendations.from_json(json)
# print the JSON string representation of the object
print(SDCategoryRecommendations.to_json())

# convert the object into a dict
sd_category_recommendations_dict = sd_category_recommendations_instance.to_dict()
# create an instance of SDCategoryRecommendations from a dict
sd_category_recommendations_from_dict = SDCategoryRecommendations.from_dict(sd_category_recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


