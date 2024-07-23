# CreateTargetingExpressionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | [**List[TargetingPredicateBase]**](TargetingPredicateBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_targeting_expression_inner import CreateTargetingExpressionInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetingExpressionInner from a JSON string
create_targeting_expression_inner_instance = CreateTargetingExpressionInner.from_json(json)
# print the JSON string representation of the object
print(CreateTargetingExpressionInner.to_json())

# convert the object into a dict
create_targeting_expression_inner_dict = create_targeting_expression_inner_instance.to_dict()
# create an instance of CreateTargetingExpressionInner from a dict
create_targeting_expression_inner_from_dict = CreateTargetingExpressionInner.from_dict(create_targeting_expression_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


