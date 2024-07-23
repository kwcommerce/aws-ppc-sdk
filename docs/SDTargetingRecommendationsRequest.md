# SDTargetingRecommendationsRequest

Request for targeting recommendations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tactic** | [**SDTactic**](SDTactic.md) |  | 
**products** | [**List[SDGoalProduct]**](SDGoalProduct.md) | A list of products for which to get targeting recommendations | 
**type_filter** | [**List[SDRecommendationType]**](SDRecommendationType.md) | A filter to indicate which types of recommendations to request. | 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_request import SDTargetingRecommendationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsRequest from a JSON string
sd_targeting_recommendations_request_instance = SDTargetingRecommendationsRequest.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsRequest.to_json())

# convert the object into a dict
sd_targeting_recommendations_request_dict = sd_targeting_recommendations_request_instance.to_dict()
# create an instance of SDTargetingRecommendationsRequest from a dict
sd_targeting_recommendations_request_from_dict = SDTargetingRecommendationsRequest.from_dict(sd_targeting_recommendations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


