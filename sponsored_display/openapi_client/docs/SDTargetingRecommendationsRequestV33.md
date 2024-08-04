# SDTargetingRecommendationsRequestV33

Request for targeting recommendations for API version 3.3.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tactic** | [**SDTacticV31**](SDTacticV31.md) |  | 
**products** | [**List[SDGoalProduct]**](SDGoalProduct.md) | A list of products for which to get targeting recommendations | 
**type_filter** | [**List[SDRecommendationTypeV32]**](SDRecommendationTypeV32.md) | A filter to indicate which types of recommendations to request. | 
**themes** | [**SDTargetingRecommendationsThemes**](SDTargetingRecommendationsThemes.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_request_v33 import SDTargetingRecommendationsRequestV33

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsRequestV33 from a JSON string
sd_targeting_recommendations_request_v33_instance = SDTargetingRecommendationsRequestV33.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsRequestV33.to_json())

# convert the object into a dict
sd_targeting_recommendations_request_v33_dict = sd_targeting_recommendations_request_v33_instance.to_dict()
# create an instance of SDTargetingRecommendationsRequestV33 from a dict
sd_targeting_recommendations_request_v33_from_dict = SDTargetingRecommendationsRequestV33.from_dict(sd_targeting_recommendations_request_v33_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


