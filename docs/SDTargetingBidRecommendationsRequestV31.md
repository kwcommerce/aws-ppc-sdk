# SDTargetingBidRecommendationsRequestV31

Request for targeting bid recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDGoalProduct]**](SDGoalProduct.md) | A list of products to tailor bid recommendations for category and audience based targeting clauses. | [optional] 
**targeting_clauses** | [**List[SDTargetingBidRecommendationsRequestV33TargetingClausesInner]**](SDTargetingBidRecommendationsRequestV33TargetingClausesInner.md) | A list of targeting clauses to receive bid recommendations for. | 

## Example

```python
from openapi_client.models.sd_targeting_bid_recommendations_request_v31 import SDTargetingBidRecommendationsRequestV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingBidRecommendationsRequestV31 from a JSON string
sd_targeting_bid_recommendations_request_v31_instance = SDTargetingBidRecommendationsRequestV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingBidRecommendationsRequestV31.to_json())

# convert the object into a dict
sd_targeting_bid_recommendations_request_v31_dict = sd_targeting_bid_recommendations_request_v31_instance.to_dict()
# create an instance of SDTargetingBidRecommendationsRequestV31 from a dict
sd_targeting_bid_recommendations_request_v31_from_dict = SDTargetingBidRecommendationsRequestV31.from_dict(sd_targeting_bid_recommendations_request_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


