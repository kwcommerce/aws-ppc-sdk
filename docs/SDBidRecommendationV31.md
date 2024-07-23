# SDBidRecommendationV31

A recommended bid range to use for a target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_lower** | **float** | The lowest recommended bid to use to win an ad placement for this target. | 
**range_upper** | **float** | The highest recommended bid to use to win an ad placement for this target. | 
**recommended** | **float** | The recommended bid to use to win an ad placement for this target. | 

## Example

```python
from openapi_client.models.sd_bid_recommendation_v31 import SDBidRecommendationV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDBidRecommendationV31 from a JSON string
sd_bid_recommendation_v31_instance = SDBidRecommendationV31.from_json(json)
# print the JSON string representation of the object
print(SDBidRecommendationV31.to_json())

# convert the object into a dict
sd_bid_recommendation_v31_dict = sd_bid_recommendation_v31_instance.to_dict()
# create an instance of SDBidRecommendationV31 from a dict
sd_bid_recommendation_v31_from_dict = SDBidRecommendationV31.from_dict(sd_bid_recommendation_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


