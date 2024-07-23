# BudgetUsageCampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_ids** | **List[str]** | A list of campaign IDs | [optional] 

## Example

```python
from openapi_client.models.budget_usage_campaign_request import BudgetUsageCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUsageCampaignRequest from a JSON string
budget_usage_campaign_request_instance = BudgetUsageCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(BudgetUsageCampaignRequest.to_json())

# convert the object into a dict
budget_usage_campaign_request_dict = budget_usage_campaign_request_instance.to_dict()
# create an instance of BudgetUsageCampaignRequest from a dict
budget_usage_campaign_request_from_dict = BudgetUsageCampaignRequest.from_dict(budget_usage_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


