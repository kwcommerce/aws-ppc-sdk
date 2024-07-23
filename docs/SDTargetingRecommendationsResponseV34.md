# SDTargetingRecommendationsResponseV34

Response to a request for targeting recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**SDTargetingRecommendationsV34**](SDTargetingRecommendationsV34.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_response_v34 import SDTargetingRecommendationsResponseV34

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsResponseV34 from a JSON string
sd_targeting_recommendations_response_v34_instance = SDTargetingRecommendationsResponseV34.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsResponseV34.to_json())

# convert the object into a dict
sd_targeting_recommendations_response_v34_dict = sd_targeting_recommendations_response_v34_instance.to_dict()
# create an instance of SDTargetingRecommendationsResponseV34 from a dict
sd_targeting_recommendations_response_v34_from_dict = SDTargetingRecommendationsResponseV34.from_dict(sd_targeting_recommendations_response_v34_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


