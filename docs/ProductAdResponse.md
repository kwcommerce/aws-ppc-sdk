# ProductAdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of the response. | [optional] 
**description** | **str** | A human-readable description of the response. | [optional] 
**ad_id** | **float** | The identifier of the ad. | [optional] 

## Example

```python
from openapi_client.models.product_ad_response import ProductAdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAdResponse from a JSON string
product_ad_response_instance = ProductAdResponse.from_json(json)
# print the JSON string representation of the object
print(ProductAdResponse.to_json())

# convert the object into a dict
product_ad_response_dict = product_ad_response_instance.to_dict()
# create an instance of ProductAdResponse from a dict
product_ad_response_from_dict = ProductAdResponse.from_dict(product_ad_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


