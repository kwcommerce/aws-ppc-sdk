# SDProductRecommendationsV31


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[SDProductRecommendation]**](SDProductRecommendation.md) | List of recommended product targets | [optional] 

## Example

```python
from openapi_client.models.sd_product_recommendations_v31 import SDProductRecommendationsV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDProductRecommendationsV31 from a JSON string
sd_product_recommendations_v31_instance = SDProductRecommendationsV31.from_json(json)
# print the JSON string representation of the object
print(SDProductRecommendationsV31.to_json())

# convert the object into a dict
sd_product_recommendations_v31_dict = sd_product_recommendations_v31_instance.to_dict()
# create an instance of SDProductRecommendationsV31 from a dict
sd_product_recommendations_v31_from_dict = SDProductRecommendationsV31.from_dict(sd_product_recommendations_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


