# SDTargetingRecommendationsResponse

Response to a request for targeting recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**SDTargetingRecommendations**](SDTargetingRecommendations.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_response import SDTargetingRecommendationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsResponse from a JSON string
sd_targeting_recommendations_response_instance = SDTargetingRecommendationsResponse.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsResponse.to_json())

# convert the object into a dict
sd_targeting_recommendations_response_dict = sd_targeting_recommendations_response_instance.to_dict()
# create an instance of SDTargetingRecommendationsResponse from a dict
sd_targeting_recommendations_response_from_dict = SDTargetingRecommendationsResponse.from_dict(sd_targeting_recommendations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


