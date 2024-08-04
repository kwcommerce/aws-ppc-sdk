# BudgetUsageCampaignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | [**List[BudgetUsageCampaign]**](BudgetUsageCampaign.md) | List of budget usage percentages that were successfully pulled | [optional] 
**error** | [**List[BudgetUsageCampaignBatchError]**](BudgetUsageCampaignBatchError.md) | List of budget usage percentages that failed to pull | [optional] 

## Example

```python
from openapi_client.models.budget_usage_campaign_response import BudgetUsageCampaignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUsageCampaignResponse from a JSON string
budget_usage_campaign_response_instance = BudgetUsageCampaignResponse.from_json(json)
# print the JSON string representation of the object
print(BudgetUsageCampaignResponse.to_json())

# convert the object into a dict
budget_usage_campaign_response_dict = budget_usage_campaign_response_instance.to_dict()
# create an instance of BudgetUsageCampaignResponse from a dict
budget_usage_campaign_response_from_dict = BudgetUsageCampaignResponse.from_dict(budget_usage_campaign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


