# SDTargetingRecommendationsResponseV33

Response to a request for targeting recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**SDTargetingRecommendationsV33**](SDTargetingRecommendationsV33.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_response_v33 import SDTargetingRecommendationsResponseV33

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsResponseV33 from a JSON string
sd_targeting_recommendations_response_v33_instance = SDTargetingRecommendationsResponseV33.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsResponseV33.to_json())

# convert the object into a dict
sd_targeting_recommendations_response_v33_dict = sd_targeting_recommendations_response_v33_instance.to_dict()
# create an instance of SDTargetingRecommendationsResponseV33 from a dict
sd_targeting_recommendations_response_v33_from_dict = SDTargetingRecommendationsResponseV33.from_dict(sd_targeting_recommendations_response_v33_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


