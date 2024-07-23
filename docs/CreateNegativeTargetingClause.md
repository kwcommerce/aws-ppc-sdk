# CreateNegativeTargetingClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**ad_group_id** | **int** | The identifier of the ad group. | 
**expression** | [**List[NegativeTargetingExpression]**](NegativeTargetingExpression.md) | The expression to negatively match against. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression. | 
**expression_type** | **str** |  | 

## Example

```python
from openapi_client.models.create_negative_targeting_clause import CreateNegativeTargetingClause

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNegativeTargetingClause from a JSON string
create_negative_targeting_clause_instance = CreateNegativeTargetingClause.from_json(json)
# print the JSON string representation of the object
print(CreateNegativeTargetingClause.to_json())

# convert the object into a dict
create_negative_targeting_clause_dict = create_negative_targeting_clause_instance.to_dict()
# create an instance of CreateNegativeTargetingClause from a dict
create_negative_targeting_clause_from_dict = CreateNegativeTargetingClause.from_dict(create_negative_targeting_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


