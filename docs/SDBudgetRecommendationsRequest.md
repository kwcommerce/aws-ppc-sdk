# SDBudgetRecommendationsRequest

Request for budget recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_ids** | **List[str]** | A list of campaign ids for which to get budget recommendations and missed opportunities. | 

## Example

```python
from openapi_client.models.sd_budget_recommendations_request import SDBudgetRecommendationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SDBudgetRecommendationsRequest from a JSON string
sd_budget_recommendations_request_instance = SDBudgetRecommendationsRequest.from_json(json)
# print the JSON string representation of the object
print(SDBudgetRecommendationsRequest.to_json())

# convert the object into a dict
sd_budget_recommendations_request_dict = sd_budget_recommendations_request_instance.to_dict()
# create an instance of SDBudgetRecommendationsRequest from a dict
sd_budget_recommendations_request_from_dict = SDBudgetRecommendationsRequest.from_dict(sd_budget_recommendations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


