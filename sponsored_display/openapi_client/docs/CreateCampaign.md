# CreateCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the campaign. | [optional] 
**budget_type** | **str** | The time period over which the amount specified in the &#x60;budget&#x60; property is allocated. | [optional] 
**budget** | **float** | The amount of the budget. | [optional] 
**start_date** | **str** | The YYYYMMDD start date of the campaign. The date must be today or in the future. | [optional] 
**end_date** | **str** | The YYYYMMDD end date of the campaign. | [optional] 
**cost_type** | **str** | Determines how the campaign will bid and charge. |Name|Description| |----|----------| |cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.| |vcpm |The performance of this campaign is measured by the viewed impressions triggered by the ad. |  To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). | [optional] 
**state** | **str** | The state of the campaign. | [optional] 
**portfolio_id** | **int** | Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported. | [optional] 
**tactic** | [**Tactic**](Tactic.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_campaign import CreateCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCampaign from a JSON string
create_campaign_instance = CreateCampaign.from_json(json)
# print the JSON string representation of the object
print(CreateCampaign.to_json())

# convert the object into a dict
create_campaign_dict = create_campaign_instance.to_dict()
# create an instance of CreateCampaign from a dict
create_campaign_from_dict = CreateCampaign.from_dict(create_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


