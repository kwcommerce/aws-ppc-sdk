# SDTargetingClauseV32

The targeting clause

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression_type** | **str** | Tactic T00020 ad groups only allow manual targeting. | 
**expression** | [**List[SDTargetExpressionV32]**](SDTargetExpressionV32.md) | The targeting expression to match against.  ------- Applicable to contextual targeting (T00020) ------- * A &#39;TargetingExpression&#39; in a contextual targeting campaign can only contain &#39;TargetingPredicate&#39; or &#39;ContentTargetingPredicate&#39; components. * Expressions must specify either a category predicate or an ASIN predicate, but never both. * Only one category may be specified per targeting expression. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.  ------- Applicable to audience targeting (T00030) ------- * A &#39;TargetingExpression&#39; in an audience campaign can only contain &#39;TargetingPredicateNested&#39; or &#39;ContentTargetingPredicate&#39; components. | 

## Example

```python
from openapi_client.models.sd_targeting_clause_v32 import SDTargetingClauseV32

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingClauseV32 from a JSON string
sd_targeting_clause_v32_instance = SDTargetingClauseV32.from_json(json)
# print the JSON string representation of the object
print(SDTargetingClauseV32.to_json())

# convert the object into a dict
sd_targeting_clause_v32_dict = sd_targeting_clause_v32_instance.to_dict()
# create an instance of SDTargetingClauseV32 from a dict
sd_targeting_clause_v32_from_dict = SDTargetingClauseV32.from_dict(sd_targeting_clause_v32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


