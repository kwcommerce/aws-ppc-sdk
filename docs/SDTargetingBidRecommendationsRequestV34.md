# SDTargetingBidRecommendationsRequestV34

Request for targeting bid recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDGoalProduct]**](SDGoalProduct.md) | A list of products to tailor bid recommendations for category and audience based targeting clauses. This array must contain consistent fields of either asins or landing pages (when linking to other pages), these cannot be mixed for any given request. If landingPageUrl is used, only one item is allowed for the list. | [optional] 
**bid_optimization** | [**SDBidOptimizationV32**](SDBidOptimizationV32.md) |  | 
**cost_type** | [**SDCostTypeV31**](SDCostTypeV31.md) |  | 
**creative_type** | [**SDCreativeType**](SDCreativeType.md) |  | [optional] 
**targeting_clauses** | [**List[SDTargetingBidRecommendationsRequestV34TargetingClausesInner]**](SDTargetingBidRecommendationsRequestV34TargetingClausesInner.md) | A list of targeting clauses to receive bid recommendations for. | 

## Example

```python
from openapi_client.models.sd_targeting_bid_recommendations_request_v34 import SDTargetingBidRecommendationsRequestV34

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingBidRecommendationsRequestV34 from a JSON string
sd_targeting_bid_recommendations_request_v34_instance = SDTargetingBidRecommendationsRequestV34.from_json(json)
# print the JSON string representation of the object
print(SDTargetingBidRecommendationsRequestV34.to_json())

# convert the object into a dict
sd_targeting_bid_recommendations_request_v34_dict = sd_targeting_bid_recommendations_request_v34_instance.to_dict()
# create an instance of SDTargetingBidRecommendationsRequestV34 from a dict
sd_targeting_bid_recommendations_request_v34_from_dict = SDTargetingBidRecommendationsRequestV34.from_dict(sd_targeting_bid_recommendations_request_v34_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


