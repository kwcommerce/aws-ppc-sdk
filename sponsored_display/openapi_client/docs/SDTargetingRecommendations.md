# SDTargetingRecommendations

A collection of targeting recommendations. Results will be sorted with strongest recommendations in the beginning.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDProductRecommendation]**](SDProductRecommendation.md) | List of recommended product targets | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations import SDTargetingRecommendations

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendations from a JSON string
sd_targeting_recommendations_instance = SDTargetingRecommendations.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendations.to_json())

# convert the object into a dict
sd_targeting_recommendations_dict = sd_targeting_recommendations_instance.to_dict()
# create an instance of SDTargetingRecommendations from a dict
sd_targeting_recommendations_from_dict = SDTargetingRecommendations.from_dict(sd_targeting_recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


