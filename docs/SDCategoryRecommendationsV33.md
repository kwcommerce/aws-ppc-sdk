# SDCategoryRecommendationsV33


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[SDCategoryRecommendationV33]**](SDCategoryRecommendationV33.md) | List of recommended category targets. | [optional] 

## Example

```python
from openapi_client.models.sd_category_recommendations_v33 import SDCategoryRecommendationsV33

# TODO update the JSON string below
json = "{}"
# create an instance of SDCategoryRecommendationsV33 from a JSON string
sd_category_recommendations_v33_instance = SDCategoryRecommendationsV33.from_json(json)
# print the JSON string representation of the object
print(SDCategoryRecommendationsV33.to_json())

# convert the object into a dict
sd_category_recommendations_v33_dict = sd_category_recommendations_v33_instance.to_dict()
# create an instance of SDCategoryRecommendationsV33 from a dict
sd_category_recommendations_v33_from_dict = SDCategoryRecommendationsV33.from_dict(sd_category_recommendations_v33_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


