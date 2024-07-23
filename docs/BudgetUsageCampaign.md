# BudgetUsageCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_usage_percent** | **float** | Budget usage percentage (spend / available budget) for the given budget policy. | [optional] 
**campaign_id** | **str** | ID of requested resource | [optional] 
**usage_updated_timestamp** | **datetime** | Last evaluation time for budget usage | [optional] 
**index** | **float** | An index to maintain order of the campaignIds | [optional] 
**budget** | **float** | Budget amount of resource requested | [optional] 

## Example

```python
from openapi_client.models.budget_usage_campaign import BudgetUsageCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUsageCampaign from a JSON string
budget_usage_campaign_instance = BudgetUsageCampaign.from_json(json)
# print the JSON string representation of the object
print(BudgetUsageCampaign.to_json())

# convert the object into a dict
budget_usage_campaign_dict = budget_usage_campaign_instance.to_dict()
# create an instance of BudgetUsageCampaign from a dict
budget_usage_campaign_from_dict = BudgetUsageCampaign.from_dict(budget_usage_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


