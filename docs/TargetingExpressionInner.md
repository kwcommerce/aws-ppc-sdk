# TargetingExpressionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | [**List[TargetingPredicateBase]**](TargetingPredicateBase.md) |  | [optional] 
**event_type** | **str** | The type of event that the value applies to. Only available for similarProduct and exactProduct currently. * views event type corresponds to a customer who viewed the detail page of the product(s). | [optional] 

## Example

```python
from openapi_client.models.targeting_expression_inner import TargetingExpressionInner

# TODO update the JSON string below
json = "{}"
# create an instance of TargetingExpressionInner from a JSON string
targeting_expression_inner_instance = TargetingExpressionInner.from_json(json)
# print the JSON string representation of the object
print(TargetingExpressionInner.to_json())

# convert the object into a dict
targeting_expression_inner_dict = targeting_expression_inner_instance.to_dict()
# create an instance of TargetingExpressionInner from a dict
targeting_expression_inner_from_dict = TargetingExpressionInner.from_dict(targeting_expression_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


