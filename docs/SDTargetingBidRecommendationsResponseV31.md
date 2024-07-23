# SDTargetingBidRecommendationsResponseV31

Response to a request for targeting bid recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_type** | [**SDCostTypeV31**](SDCostTypeV31.md) |  | 
**bid_recommendations** | [**List[SDTargetingBidRecommendationsResponseV32BidRecommendationsInner]**](SDTargetingBidRecommendationsResponseV32BidRecommendationsInner.md) |  | 

## Example

```python
from openapi_client.models.sd_targeting_bid_recommendations_response_v31 import SDTargetingBidRecommendationsResponseV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingBidRecommendationsResponseV31 from a JSON string
sd_targeting_bid_recommendations_response_v31_instance = SDTargetingBidRecommendationsResponseV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingBidRecommendationsResponseV31.to_json())

# convert the object into a dict
sd_targeting_bid_recommendations_response_v31_dict = sd_targeting_bid_recommendations_response_v31_instance.to_dict()
# create an instance of SDTargetingBidRecommendationsResponseV31 from a dict
sd_targeting_bid_recommendations_response_v31_from_dict = SDTargetingBidRecommendationsResponseV31.from_dict(sd_targeting_bid_recommendations_response_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


