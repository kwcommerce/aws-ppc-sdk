# SDAudienceRecommendations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | [**List[SDAudienceCategoryRecommendations]**](SDAudienceCategoryRecommendations.md) | List of recommended audience targets, broken down by audience category | [optional] 

## Example

```python
from openapi_client.models.sd_audience_recommendations import SDAudienceRecommendations

# TODO update the JSON string below
json = "{}"
# create an instance of SDAudienceRecommendations from a JSON string
sd_audience_recommendations_instance = SDAudienceRecommendations.from_json(json)
# print the JSON string representation of the object
print(SDAudienceRecommendations.to_json())

# convert the object into a dict
sd_audience_recommendations_dict = sd_audience_recommendations_instance.to_dict()
# create an instance of SDAudienceRecommendations from a dict
sd_audience_recommendations_from_dict = SDAudienceRecommendations.from_dict(sd_audience_recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


