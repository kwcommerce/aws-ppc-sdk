# ResolvedLocationExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LocationPredicate**](LocationPredicate.md) |  | [optional] 
**value** | **str** | The human-readable location name. | [optional] 

## Example

```python
from openapi_client.models.resolved_location_expression import ResolvedLocationExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedLocationExpression from a JSON string
resolved_location_expression_instance = ResolvedLocationExpression.from_json(json)
# print the JSON string representation of the object
print(ResolvedLocationExpression.to_json())

# convert the object into a dict
resolved_location_expression_dict = resolved_location_expression_instance.to_dict()
# create an instance of ResolvedLocationExpression from a dict
resolved_location_expression_from_dict = ResolvedLocationExpression.from_dict(resolved_location_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


