# SDTargetingRecommendationsRequestV32

Request for targeting recommendations for API version 3.2.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tactic** | [**SDTacticV31**](SDTacticV31.md) |  | 
**products** | [**List[SDGoalProduct]**](SDGoalProduct.md) | A list of products for which to get targeting recommendations | 
**type_filter** | [**List[SDRecommendationTypeV31]**](SDRecommendationTypeV31.md) | A filter to indicate which types of recommendations to request. | 
**themes** | [**SDTargetingRecommendationsThemes**](SDTargetingRecommendationsThemes.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_request_v32 import SDTargetingRecommendationsRequestV32

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsRequestV32 from a JSON string
sd_targeting_recommendations_request_v32_instance = SDTargetingRecommendationsRequestV32.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsRequestV32.to_json())

# convert the object into a dict
sd_targeting_recommendations_request_v32_dict = sd_targeting_recommendations_request_v32_instance.to_dict()
# create an instance of SDTargetingRecommendationsRequestV32 from a dict
sd_targeting_recommendations_request_v32_from_dict = SDTargetingRecommendationsRequestV32.from_dict(sd_targeting_recommendations_request_v32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


