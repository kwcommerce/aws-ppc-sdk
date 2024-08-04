# SDProductRecommendation

A recommended product to target ads on

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | Amazon Standard Identification Number | [optional] 
**rank** | **int** | A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation | [optional] 

## Example

```python
from openapi_client.models.sd_product_recommendation import SDProductRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of SDProductRecommendation from a JSON string
sd_product_recommendation_instance = SDProductRecommendation.from_json(json)
# print the JSON string representation of the object
print(SDProductRecommendation.to_json())

# convert the object into a dict
sd_product_recommendation_dict = sd_product_recommendation_instance.to_dict()
# create an instance of SDProductRecommendation from a dict
sd_product_recommendation_from_dict = SDProductRecommendation.from_dict(sd_product_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


