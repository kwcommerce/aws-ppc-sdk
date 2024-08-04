# SDTargetingRecommendationsRequestV35

Request for targeting recommendations for API version 3.5.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tactic** | [**SDTacticV31**](SDTacticV31.md) |  | 
**products** | [**List[SDTargetingRecommendationsProductsV31Inner]**](SDTargetingRecommendationsProductsV31Inner.md) | A list of products for which to get targeting recommendations. This array can only contain either asins or landing pages. If landingPageURL is used, there can only be one item in the array for each request. | 
**type_filter** | [**List[SDRecommendationTypeV33]**](SDRecommendationTypeV33.md) | A filter to indicate which types of recommendations to request. | 
**themes** | [**SDTargetingRecommendationsThemes**](SDTargetingRecommendationsThemes.md) |  | [optional] 
**category_type** | **str** | This field is optional unless the field locationExpression is present in the request. It is used for category audience targeting to specify if the audience is for views (re-marketing) or purchases (re-purchasing). The specified categories will be returned accordingly. | [optional] 
**location_expression** | [**List[LocationExpression]**](LocationExpression.md) | This optional field is used to specify the locations used in SD location targeting for non-Amazon sellers only at the moment. Therefore it&#39;s only supported if the product is a landing page url. | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_recommendations_request_v35 import SDTargetingRecommendationsRequestV35

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingRecommendationsRequestV35 from a JSON string
sd_targeting_recommendations_request_v35_instance = SDTargetingRecommendationsRequestV35.from_json(json)
# print the JSON string representation of the object
print(SDTargetingRecommendationsRequestV35.to_json())

# convert the object into a dict
sd_targeting_recommendations_request_v35_dict = sd_targeting_recommendations_request_v35_instance.to_dict()
# create an instance of SDTargetingRecommendationsRequestV35 from a dict
sd_targeting_recommendations_request_v35_from_dict = SDTargetingRecommendationsRequestV35.from_dict(sd_targeting_recommendations_request_v35_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


