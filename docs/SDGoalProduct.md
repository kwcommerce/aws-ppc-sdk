# SDGoalProduct

A product an advertisers wants to advertise. Recommendations will be made for specified goal products.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | Amazon Standard Identification Number | 

## Example

```python
from openapi_client.models.sd_goal_product import SDGoalProduct

# TODO update the JSON string below
json = "{}"
# create an instance of SDGoalProduct from a JSON string
sd_goal_product_instance = SDGoalProduct.from_json(json)
# print the JSON string representation of the object
print(SDGoalProduct.to_json())

# convert the object into a dict
sd_goal_product_dict = sd_goal_product_instance.to_dict()
# create an instance of SDGoalProduct from a dict
sd_goal_product_from_dict = SDGoalProduct.from_dict(sd_goal_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


