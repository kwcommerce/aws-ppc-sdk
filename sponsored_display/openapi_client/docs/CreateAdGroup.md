# CreateAdGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ad group. | 
**campaign_id** | **int** | The identifier of the campaign. | 
**default_bid** | **float** | The amount of the default bid associated with the ad group. Used if no bid is specified. | [optional] 
**bid_optimization** | **str** | Bid Optimization for the Adgroup. Default behavior is to optimize for clicks. Leads is only supported when using landingPageType of OFF_AMAZON_LINK. |Name|CostType|Description| |----|--------|-----------| |reach |vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.| |clicks |cpc|[Default] Optimize for page visits.| |conversions |cpc|Optimize for conversion.| |leads |cpc| Optimize for lead generation.| | [optional] 
**state** | **str** | The state of the ad group. | 
**creative_type** | [**CreativeType**](CreativeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_ad_group import CreateAdGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdGroup from a JSON string
create_ad_group_instance = CreateAdGroup.from_json(json)
# print the JSON string representation of the object
print(CreateAdGroup.to_json())

# convert the object into a dict
create_ad_group_dict = create_ad_group_instance.to_dict()
# create an instance of CreateAdGroup from a dict
create_ad_group_from_dict = CreateAdGroup.from_dict(create_ad_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


