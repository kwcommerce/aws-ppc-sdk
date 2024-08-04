# SDTargetingBidRecommendationsResponseItemSuccessV31

A recommended bid range to use for a target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_lower** | **float** | The lowest recommended bid to use to win an ad placement for this target. | 
**range_upper** | **float** | The highest recommended bid to use to win an ad placement for this target. | 
**recommended** | **float** | The recommended bid to use to win an ad placement for this target. | 
**code** | **str** | The HTTP status code of this item. | 

## Example

```python
from openapi_client.models.sd_targeting_bid_recommendations_response_item_success_v31 import SDTargetingBidRecommendationsResponseItemSuccessV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingBidRecommendationsResponseItemSuccessV31 from a JSON string
sd_targeting_bid_recommendations_response_item_success_v31_instance = SDTargetingBidRecommendationsResponseItemSuccessV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingBidRecommendationsResponseItemSuccessV31.to_json())

# convert the object into a dict
sd_targeting_bid_recommendations_response_item_success_v31_dict = sd_targeting_bid_recommendations_response_item_success_v31_instance.to_dict()
# create an instance of SDTargetingBidRecommendationsResponseItemSuccessV31 from a dict
sd_targeting_bid_recommendations_response_item_success_v31_from_dict = SDTargetingBidRecommendationsResponseItemSuccessV31.from_dict(sd_targeting_bid_recommendations_response_item_success_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


