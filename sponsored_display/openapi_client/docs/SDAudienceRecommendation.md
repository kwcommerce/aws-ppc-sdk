# SDAudienceRecommendation

A recommended standard Amazon audience to target ads on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | The audience identifier | [optional] 
**name** | **str** | The Amazon audience name | [optional] 
**rank** | **int** | A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation | [optional] 

## Example

```python
from openapi_client.models.sd_audience_recommendation import SDAudienceRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of SDAudienceRecommendation from a JSON string
sd_audience_recommendation_instance = SDAudienceRecommendation.from_json(json)
# print the JSON string representation of the object
print(SDAudienceRecommendation.to_json())

# convert the object into a dict
sd_audience_recommendation_dict = sd_audience_recommendation_instance.to_dict()
# create an instance of SDAudienceRecommendation from a dict
sd_audience_recommendation_from_dict = SDAudienceRecommendation.from_dict(sd_audience_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


