# SDProductRecommendationsV32


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDProductRecommendationV32]**](SDProductRecommendationV32.md) | List of recommended product targets | [optional] 

## Example

```python
from openapi_client.models.sd_product_recommendations_v32 import SDProductRecommendationsV32

# TODO update the JSON string below
json = "{}"
# create an instance of SDProductRecommendationsV32 from a JSON string
sd_product_recommendations_v32_instance = SDProductRecommendationsV32.from_json(json)
# print the JSON string representation of the object
print(SDProductRecommendationsV32.to_json())

# convert the object into a dict
sd_product_recommendations_v32_dict = sd_product_recommendations_v32_instance.to_dict()
# create an instance of SDProductRecommendationsV32 from a dict
sd_product_recommendations_v32_from_dict = SDProductRecommendationsV32.from_dict(sd_product_recommendations_v32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


