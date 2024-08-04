# NegativeTargetingClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**target_id** | **int** |  | [optional] 
**ad_group_id** | **int** | The identifier of the ad group. | [optional] 
**expression_type** | **str** |  | [optional] 
**expression** | [**List[NegativeTargetingExpression]**](NegativeTargetingExpression.md) | The expression to negatively match against. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression. | [optional] 
**resolved_expression** | [**List[NegativeTargetingExpression]**](NegativeTargetingExpression.md) | The resolved negative targeting expression. | [optional] 

## Example

```python
from openapi_client.models.negative_targeting_clause import NegativeTargetingClause

# TODO update the JSON string below
json = "{}"
# create an instance of NegativeTargetingClause from a JSON string
negative_targeting_clause_instance = NegativeTargetingClause.from_json(json)
# print the JSON string representation of the object
print(NegativeTargetingClause.to_json())

# convert the object into a dict
negative_targeting_clause_dict = negative_targeting_clause_instance.to_dict()
# create an instance of NegativeTargetingClause from a dict
negative_targeting_clause_from_dict = NegativeTargetingClause.from_dict(negative_targeting_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


