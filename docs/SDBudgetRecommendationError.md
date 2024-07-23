# SDBudgetRecommendationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Correlate the recommendation to the campaign index in the request. Zero-based. | 
**campaign_id** | **str** | Campaign id. | 
**code** | **str** | The HTTP status code of the response. | 
**details** | **str** | A human-readable description of the response. | 

## Example

```python
from openapi_client.models.sd_budget_recommendation_error import SDBudgetRecommendationError

# TODO update the JSON string below
json = "{}"
# create an instance of SDBudgetRecommendationError from a JSON string
sd_budget_recommendation_error_instance = SDBudgetRecommendationError.from_json(json)
# print the JSON string representation of the object
print(SDBudgetRecommendationError.to_json())

# convert the object into a dict
sd_budget_recommendation_error_dict = sd_budget_recommendation_error_instance.to_dict()
# create an instance of SDBudgetRecommendationError from a dict
sd_budget_recommendation_error_from_dict = SDBudgetRecommendationError.from_dict(sd_budget_recommendation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


