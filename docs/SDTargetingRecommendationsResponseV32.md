# SDTargetingRecommendationsResponseV32

Response to a request for targeting recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**SDTargetingRecommendationsV32**](SDTargetingRecommendationsV32.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_response_v32 import SDTargetingRecommendationsResponseV32

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsResponseV32 from a JSON string
sd_targeting_recommendations_response_v32_instance = SDTargetingRecommendationsResponseV32.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsResponseV32.to_json())

# convert the object into a dict
sd_targeting_recommendations_response_v32_dict = sd_targeting_recommendations_response_v32_instance.to_dict()
# create an instance of SDTargetingRecommendationsResponseV32 from a dict
sd_targeting_recommendations_response_v32_from_dict = SDTargetingRecommendationsResponseV32.from_dict(sd_targeting_recommendations_response_v32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


