# SDBudgetRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Correlate the recommendation to the campaign index in the request. Zero-based. | 
**campaign_id** | **str** | Campaign id. | 
**suggested_budget** | **float** | Recommended budget for the campaign. This will be in local currency. | 
**seven_days_missed_opportunities** | [**SDSevenDaysMissedOpportunities**](SDSevenDaysMissedOpportunities.md) |  | 

## Example

```python
from openapi_client.models.sd_budget_recommendation import SDBudgetRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of SDBudgetRecommendation from a JSON string
sd_budget_recommendation_instance = SDBudgetRecommendation.from_json(json)
# print the JSON string representation of the object
print(SDBudgetRecommendation.to_json())

# convert the object into a dict
sd_budget_recommendation_dict = sd_budget_recommendation_instance.to_dict()
# create an instance of SDBudgetRecommendation from a dict
sd_budget_recommendation_from_dict = SDBudgetRecommendation.from_dict(sd_budget_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


