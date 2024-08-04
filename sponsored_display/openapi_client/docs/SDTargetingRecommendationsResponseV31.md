# SDTargetingRecommendationsResponseV31

Response to a request for targeting recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**SDTargetingRecommendationsV31**](SDTargetingRecommendationsV31.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_response_v31 import SDTargetingRecommendationsResponseV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsResponseV31 from a JSON string
sd_targeting_recommendations_response_v31_instance = SDTargetingRecommendationsResponseV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsResponseV31.to_json())

# convert the object into a dict
sd_targeting_recommendations_response_v31_dict = sd_targeting_recommendations_response_v31_instance.to_dict()
# create an instance of SDTargetingRecommendationsResponseV31 from a dict
sd_targeting_recommendations_response_v31_from_dict = SDTargetingRecommendationsResponseV31.from_dict(sd_targeting_recommendations_response_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


