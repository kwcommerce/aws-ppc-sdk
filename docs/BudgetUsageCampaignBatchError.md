# BudgetUsageCampaignBatchError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | An enumerated error code for machine use. | [optional] 
**campaign_id** | **str** | ID of requested resource | [optional] 
**index** | **float** | An index to maintain order of the campaignIds | [optional] 
**details** | **str** | A human-readable description of the response. | [optional] 

## Example

```python
from openapi_client.models.budget_usage_campaign_batch_error import BudgetUsageCampaignBatchError

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUsageCampaignBatchError from a JSON string
budget_usage_campaign_batch_error_instance = BudgetUsageCampaignBatchError.from_json(json)
# print the JSON string representation of the object
print(BudgetUsageCampaignBatchError.to_json())

# convert the object into a dict
budget_usage_campaign_batch_error_dict = budget_usage_campaign_batch_error_instance.to_dict()
# create an instance of BudgetUsageCampaignBatchError from a dict
budget_usage_campaign_batch_error_from_dict = BudgetUsageCampaignBatchError.from_dict(budget_usage_campaign_batch_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


