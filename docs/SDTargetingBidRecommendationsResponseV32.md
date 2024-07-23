# SDTargetingBidRecommendationsResponseV32

Response to a request for targeting bid recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_optimization** | [**SDBidOptimizationV32**](SDBidOptimizationV32.md) |  | 
**cost_type** | [**SDCostTypeV31**](SDCostTypeV31.md) |  | 
**bid_recommendations** | [**List[SDTargetingBidRecommendationsResponseV32BidRecommendationsInner]**](SDTargetingBidRecommendationsResponseV32BidRecommendationsInner.md) |  | 

## Example

```python
from openapi_client.models.sd_targeting_bid_recommendations_response_v32 import SDTargetingBidRecommendationsResponseV32

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingBidRecommendationsResponseV32 from a JSON string
sd_targeting_bid_recommendations_response_v32_instance = SDTargetingBidRecommendationsResponseV32.from_json(json)
# print the JSON string representation of the object
print(SDTargetingBidRecommendationsResponseV32.to_json())

# convert the object into a dict
sd_targeting_bid_recommendations_response_v32_dict = sd_targeting_bid_recommendations_response_v32_instance.to_dict()
# create an instance of SDTargetingBidRecommendationsResponseV32 from a dict
sd_targeting_bid_recommendations_response_v32_from_dict = SDTargetingBidRecommendationsResponseV32.from_dict(sd_targeting_bid_recommendations_response_v32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


