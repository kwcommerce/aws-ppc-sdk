# NegativeTargetingClauseExExpressionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The intent type. See the [targeting topic](https://advertising.amazon.com/help#GQCBASRVERXSARL3) in the Amazon Ads support center for more information. | [optional] 
**value** | **str** | The value to be negatively targeted. Used only in manual expressions. | [optional] 

## Example

```python
from openapi_client.models.negative_targeting_clause_ex_expression_inner import NegativeTargetingClauseExExpressionInner

# TODO update the JSON string below
json = "{}"
# create an instance of NegativeTargetingClauseExExpressionInner from a JSON string
negative_targeting_clause_ex_expression_inner_instance = NegativeTargetingClauseExExpressionInner.from_json(json)
# print the JSON string representation of the object
print(NegativeTargetingClauseExExpressionInner.to_json())

# convert the object into a dict
negative_targeting_clause_ex_expression_inner_dict = negative_targeting_clause_ex_expression_inner_instance.to_dict()
# create an instance of NegativeTargetingClauseExExpressionInner from a dict
negative_targeting_clause_ex_expression_inner_from_dict = NegativeTargetingClauseExExpressionInner.from_dict(negative_targeting_clause_ex_expression_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


