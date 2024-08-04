# SDTargetingBidRecommendationsResponseItemFailureV31

Failed bid recommendation response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of this item. | 
**details** | **str** | A human-readable description of this item on error. | 

## Example

```python
from openapi_client.models.sd_targeting_bid_recommendations_response_item_failure_v31 import SDTargetingBidRecommendationsResponseItemFailureV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingBidRecommendationsResponseItemFailureV31 from a JSON string
sd_targeting_bid_recommendations_response_item_failure_v31_instance = SDTargetingBidRecommendationsResponseItemFailureV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingBidRecommendationsResponseItemFailureV31.to_json())

# convert the object into a dict
sd_targeting_bid_recommendations_response_item_failure_v31_dict = sd_targeting_bid_recommendations_response_item_failure_v31_instance.to_dict()
# create an instance of SDTargetingBidRecommendationsResponseItemFailureV31 from a dict
sd_targeting_bid_recommendations_response_item_failure_v31_from_dict = SDTargetingBidRecommendationsResponseItemFailureV31.from_dict(sd_targeting_bid_recommendations_response_item_failure_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


