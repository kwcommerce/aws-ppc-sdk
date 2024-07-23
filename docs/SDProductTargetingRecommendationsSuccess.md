# SDProductTargetingRecommendationsSuccess

Recommendation results for contextual targeting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | HTTP status code 200 indicating a successful response for product recomendations. | [optional] 
**name** | **str** | The theme name specified in the request. | [optional] 
**recommendations** | [**List[SDProductRecommendationV32]**](SDProductRecommendationV32.md) | A list of recommended products. | [optional] 

## Example

```python
from openapi_client.models.sd_product_targeting_recommendations_success import SDProductTargetingRecommendationsSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of SDProductTargetingRecommendationsSuccess from a JSON string
sd_product_targeting_recommendations_success_instance = SDProductTargetingRecommendationsSuccess.from_json(json)
# print the JSON string representation of the object
print(SDProductTargetingRecommendationsSuccess.to_json())

# convert the object into a dict
sd_product_targeting_recommendations_success_dict = sd_product_targeting_recommendations_success_instance.to_dict()
# create an instance of SDProductTargetingRecommendationsSuccess from a dict
sd_product_targeting_recommendations_success_from_dict = SDProductTargetingRecommendationsSuccess.from_dict(sd_product_targeting_recommendations_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


