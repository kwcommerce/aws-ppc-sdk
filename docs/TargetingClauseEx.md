# TargetingClauseEx


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **float** |  | [optional] 
**ad_group_id** | **float** |  | [optional] 
**campaign_id** | **float** |  | [optional] 
**state** | **str** |  | [optional] 
**expression_type** | **str** |  | [optional] 
**bid** | **float** | If a value for &#x60;bid&#x60; is specified, it overrides the current adGroup bid. When using vcpm costType. $1 is the minimum bid for vCPM. Note that this field is ignored for negative targeting clauses. | [optional] 
**expression** | [**List[TargetingExpressionInner]**](TargetingExpressionInner.md) | The targeting expression to match against.  ------- Applicable to contextual or content targeting (T00020) ------- * A &#39;TargetingExpression&#39; in a contextual targeting campaign can contain &#39;TargetingPredicate&#39; or &#39;ContentTargetingPredicate&#39; components. * Contextual expressions must specify either a category predicate or an ASIN predicate, but never both. * Only one category may be specified per targeting expression. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.  ------- Applicable to audience targeting (T00030) ------- * A &#39;TargetingExpression&#39; in an audience campaign can contain &#39;TargetingPredicateNested&#39; or &#39;ContentTargetingPredicate&#39; components. * Expressions must specify ASIN-grain (&#39;exactProduct&#39;), manual ASIN-grain (&#39;relatedProducts&#39; or &#39;relatedProducts&#39;), or category-grain targeting. | [optional] 
**resolved_expression** | [**List[TargetingExpressionInner]**](TargetingExpressionInner.md) | The targeting expression to match against.  ------- Applicable to contextual or content targeting (T00020) ------- * A &#39;TargetingExpression&#39; in a contextual targeting campaign can contain &#39;TargetingPredicate&#39; or &#39;ContentTargetingPredicate&#39; components. * Contextual expressions must specify either a category predicate or an ASIN predicate, but never both. * Only one category may be specified per targeting expression. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.  ------- Applicable to audience targeting (T00030) ------- * A &#39;TargetingExpression&#39; in an audience campaign can contain &#39;TargetingPredicateNested&#39; or &#39;ContentTargetingPredicate&#39; components. * Expressions must specify ASIN-grain (&#39;exactProduct&#39;), manual ASIN-grain (&#39;relatedProducts&#39; or &#39;relatedProducts&#39;), or category-grain targeting. | [optional] 
**serving_status** | **str** | The status of the target. | [optional] 
**creation_date** | **int** | Epoch date the target was created. | [optional] 
**last_updated_date** | **int** | Epoch date of the last update to any property associated with the target. | [optional] 

## Example

```python
from openapi_client.models.targeting_clause_ex import TargetingClauseEx

# TODO update the JSON string below
json = "{}"
# create an instance of TargetingClauseEx from a JSON string
targeting_clause_ex_instance = TargetingClauseEx.from_json(json)
# print the JSON string representation of the object
print(TargetingClauseEx.to_json())

# convert the object into a dict
targeting_clause_ex_dict = targeting_clause_ex_instance.to_dict()
# create an instance of TargetingClauseEx from a dict
targeting_clause_ex_from_dict = TargetingClauseEx.from_dict(targeting_clause_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


