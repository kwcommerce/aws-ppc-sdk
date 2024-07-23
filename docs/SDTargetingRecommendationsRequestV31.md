# SDTargetingRecommendationsRequestV31

Request for targeting recommendations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tactic** | [**SDTacticV31**](SDTacticV31.md) |  | 
**products** | [**List[SDGoalProduct]**](SDGoalProduct.md) | A list of products for which to get targeting recommendations | 
**type_filter** | [**List[SDRecommendationTypeV31]**](SDRecommendationTypeV31.md) | A filter to indicate which types of recommendations to request. | 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_request_v31 import SDTargetingRecommendationsRequestV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsRequestV31 from a JSON string
sd_targeting_recommendations_request_v31_instance = SDTargetingRecommendationsRequestV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsRequestV31.to_json())

# convert the object into a dict
sd_targeting_recommendations_request_v31_dict = sd_targeting_recommendations_request_v31_instance.to_dict()
# create an instance of SDTargetingRecommendationsRequestV31 from a dict
sd_targeting_recommendations_request_v31_from_dict = SDTargetingRecommendationsRequestV31.from_dict(sd_targeting_recommendations_request_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


