# SDBudgetRecommendationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_recommendations_success_results** | [**List[SDBudgetRecommendation]**](SDBudgetRecommendation.md) | List of successful budget recommendation for campaigns. | 
**budget_recommendations_error_results** | [**List[SDBudgetRecommendationError]**](SDBudgetRecommendationError.md) | List of errors that occurred when generating budget recommendation. | 

## Example

```python
from openapi_client.models.sd_budget_recommendations_response import SDBudgetRecommendationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SDBudgetRecommendationsResponse from a JSON string
sd_budget_recommendations_response_instance = SDBudgetRecommendationsResponse.from_json(json)
# print the JSON string representation of the object
print(SDBudgetRecommendationsResponse.to_json())

# convert the object into a dict
sd_budget_recommendations_response_dict = sd_budget_recommendations_response_instance.to_dict()
# create an instance of SDBudgetRecommendationsResponse from a dict
sd_budget_recommendations_response_from_dict = SDBudgetRecommendationsResponse.from_dict(sd_budget_recommendations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


