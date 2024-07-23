# LocationExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LocationPredicate**](LocationPredicate.md) |  | [optional] 
**value** | **str** | The location identifier. Currently, this can correspond to either a &#39;city&#39;, &#39;state&#39;, &#39;dma&#39;, &#39;postal code&#39;, or &#39;country&#39;. Its value is discoverable using the GET /locations API. | [optional] 

## Example

```python
from openapi_client.models.location_expression import LocationExpression

# TODO update the JSON string below
json = "{}"
# create an instance of LocationExpression from a JSON string
location_expression_instance = LocationExpression.from_json(json)
# print the JSON string representation of the object
print(LocationExpression.to_json())

# convert the object into a dict
location_expression_dict = location_expression_instance.to_dict()
# create an instance of LocationExpression from a dict
location_expression_from_dict = LocationExpression.from_dict(location_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


