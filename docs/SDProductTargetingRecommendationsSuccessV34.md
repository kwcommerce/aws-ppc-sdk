# SDProductTargetingRecommendationsSuccessV34

Recommendation results for contextual targeting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | HTTP status code 200 indicating a successful response for product recommendations. | [optional] 
**name** | **str** | The theme name specified in the request. | [optional] 
**expression** | [**List[SDProductTargetingThemeExpression]**](SDProductTargetingThemeExpression.md) | A list of expressions defining the product targeting theme. The list will define an AND operator on different expressions. For example, asinPriceGreaterThan and asinReviewRatingLessThan can be used to request product recommendations which are both with greater price and less review rating compared to the goal products. Note: currently the service only support one item in the array. | [optional] 
**recommendations** | [**List[SDProductRecommendationV32]**](SDProductRecommendationV32.md) | A list of recommended products. | [optional] 

## Example

```python
from openapi_client.models.sd_product_targeting_recommendations_success_v34 import SDProductTargetingRecommendationsSuccessV34

# TODO update the JSON string below
json = "{}"
# create an instance of SDProductTargetingRecommendationsSuccessV34 from a JSON string
sd_product_targeting_recommendations_success_v34_instance = SDProductTargetingRecommendationsSuccessV34.from_json(json)
# print the JSON string representation of the object
print(SDProductTargetingRecommendationsSuccessV34.to_json())

# convert the object into a dict
sd_product_targeting_recommendations_success_v34_dict = sd_product_targeting_recommendations_success_v34_instance.to_dict()
# create an instance of SDProductTargetingRecommendationsSuccessV34 from a dict
sd_product_targeting_recommendations_success_v34_from_dict = SDProductTargetingRecommendationsSuccessV34.from_dict(sd_product_targeting_recommendations_success_v34_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


