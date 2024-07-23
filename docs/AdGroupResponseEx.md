# AdGroupResponseEx

Object containing an extended set of data fields for an Ad Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_group_id** | **float** | The identifier of the ad group. | [optional] 
**name** | **str** | The name of the ad group. | [optional] 
**campaign_id** | **float** | The identifier of the campaign that this ad group is associated with. | [optional] 
**default_bid** | **float** | The amount of the default bid associated with the ad group. Used if no bid is specified. | [optional] 
**state** | **str** | The delivery state of the ad group. | [optional] 
**tactic** | [**Tactic**](Tactic.md) |  | [optional] 
**creative_type** | [**CreativeTypeInCreativeResponse**](CreativeTypeInCreativeResponse.md) |  | [optional] 
**serving_status** | **str** | The status of the ad group. | [optional] 
**bid_optimization** | **str** | Bid optimization type for the Adgroup. Default behavior is to optimize for clicks. Note, reach, clicks, leads are only accepted with productAds that include landingPageUrl OFF_AMAZON_LINK. |Name|CostType|Description| |----|--------|-----------| |reach|vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.| |clicks [Default]|cpc|Optimize for page visits.| |conversions|cpc|Optimize for conversion.| |leads |cpc| Optimize for lead generation.| | [optional] 
**creation_date** | **int** | Epoch time the ad group was created. | [optional] 
**last_updated_date** | **int** | Epoch time any property in the ad group was last updated. | [optional] 

## Example

```python
from openapi_client.models.ad_group_response_ex import AdGroupResponseEx

# TODO update the JSON string below
json = "{}"
# create an instance of AdGroupResponseEx from a JSON string
ad_group_response_ex_instance = AdGroupResponseEx.from_json(json)
# print the JSON string representation of the object
print(AdGroupResponseEx.to_json())

# convert the object into a dict
ad_group_response_ex_dict = ad_group_response_ex_instance.to_dict()
# create an instance of AdGroupResponseEx from a dict
ad_group_response_ex_from_dict = AdGroupResponseEx.from_dict(ad_group_response_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


