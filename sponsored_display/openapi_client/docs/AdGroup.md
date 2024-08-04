# AdGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ad group. | [optional] 
**campaign_id** | **int** | The identifier of the campaign. | [optional] 
**default_bid** | **float** | The amount of the default bid associated with the ad group. Used if no bid is specified. | [optional] 
**bid_optimization** | **str** | Bid Optimization for the Adgroup. Default behavior is to optimize for clicks. Leads is only supported when using landingPageType of OFF_AMAZON_LINK. |Name|CostType|Description| |----|--------|-----------| |reach |vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.| |clicks |cpc|[Default] Optimize for page visits.| |conversions |cpc|Optimize for conversion.| |leads |cpc| Optimize for lead generation.| | [optional] 
**state** | **str** | The state of the ad group. | [optional] 
**ad_group_id** | **int** | The identifier of the ad group. | [optional] 
**tactic** | [**Tactic**](Tactic.md) |  | [optional] 
**creative_type** | [**CreativeType**](CreativeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.ad_group import AdGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AdGroup from a JSON string
ad_group_instance = AdGroup.from_json(json)
# print the JSON string representation of the object
print(AdGroup.to_json())

# convert the object into a dict
ad_group_dict = ad_group_instance.to_dict()
# create an instance of AdGroup from a dict
ad_group_from_dict = AdGroup.from_dict(ad_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


