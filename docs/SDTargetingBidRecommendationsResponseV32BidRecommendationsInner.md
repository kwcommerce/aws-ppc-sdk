# SDTargetingBidRecommendationsResponseV32BidRecommendationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of this item. | 
**range_lower** | **float** | The lowest recommended bid to use to win an ad placement for this target. | 
**range_upper** | **float** | The highest recommended bid to use to win an ad placement for this target. | 
**recommended** | **float** | The recommended bid to use to win an ad placement for this target. | 
**details** | **str** | A human-readable description of this item on error. | 

## Example

```python
from openapi_client.models.sd_targeting_bid_recommendations_response_v32_bid_recommendations_inner import SDTargetingBidRecommendationsResponseV32BidRecommendationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingBidRecommendationsResponseV32BidRecommendationsInner from a JSON string
sd_targeting_bid_recommendations_response_v32_bid_recommendations_inner_instance = SDTargetingBidRecommendationsResponseV32BidRecommendationsInner.from_json(json)
# print the JSON string representation of the object
print(SDTargetingBidRecommendationsResponseV32BidRecommendationsInner.to_json())

# convert the object into a dict
sd_targeting_bid_recommendations_response_v32_bid_recommendations_inner_dict = sd_targeting_bid_recommendations_response_v32_bid_recommendations_inner_instance.to_dict()
# create an instance of SDTargetingBidRecommendationsResponseV32BidRecommendationsInner from a dict
sd_targeting_bid_recommendations_response_v32_bid_recommendations_inner_from_dict = SDTargetingBidRecommendationsResponseV32BidRecommendationsInner.from_dict(sd_targeting_bid_recommendations_response_v32_bid_recommendations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


