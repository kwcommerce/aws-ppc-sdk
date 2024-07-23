# NegativeTargetingClauseEx


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **float** |  | [optional] 
**ad_group_id** | **float** |  | [optional] 
**state** | **str** |  | [optional] 
**expression_type** | **str** |  | [optional] 
**expression** | [**List[NegativeTargetingClauseExExpressionInner]**](NegativeTargetingClauseExExpressionInner.md) | The expression to negatively match against. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression. | [optional] 
**serving_status** | **str** | The status of the target. | [optional] 
**creation_date** | **int** | Epoch date the target was created. | [optional] 
**last_updated_date** | **int** | Epoch date of the last update to any property associated with the target. | [optional] 

## Example

```python
from openapi_client.models.negative_targeting_clause_ex import NegativeTargetingClauseEx

# TODO update the JSON string below
json = "{}"
# create an instance of NegativeTargetingClauseEx from a JSON string
negative_targeting_clause_ex_instance = NegativeTargetingClauseEx.from_json(json)
# print the JSON string representation of the object
print(NegativeTargetingClauseEx.to_json())

# convert the object into a dict
negative_targeting_clause_ex_dict = negative_targeting_clause_ex_instance.to_dict()
# create an instance of NegativeTargetingClauseEx from a dict
negative_targeting_clause_ex_from_dict = NegativeTargetingClauseEx.from_dict(negative_targeting_clause_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


