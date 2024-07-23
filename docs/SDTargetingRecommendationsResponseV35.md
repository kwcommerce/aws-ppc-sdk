# SDTargetingRecommendationsResponseV35

Response to a request for targeting recommendations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**SDTargetingRecommendationsV35**](SDTargetingRecommendationsV35.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_response_v35 import SDTargetingRecommendationsResponseV35

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsResponseV35 from a JSON string
sd_targeting_recommendations_response_v35_instance = SDTargetingRecommendationsResponseV35.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsResponseV35.to_json())

# convert the object into a dict
sd_targeting_recommendations_response_v35_dict = sd_targeting_recommendations_response_v35_instance.to_dict()
# create an instance of SDTargetingRecommendationsResponseV35 from a dict
sd_targeting_recommendations_response_v35_from_dict = SDTargetingRecommendationsResponseV35.from_dict(sd_targeting_recommendations_response_v35_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


