# SDTargetingClauseV31

The targeting clause

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression_type** | **str** | Tactic T00020 ad groups only allow manual targeting. | 
**expression** | [**List[SDTargetExpressionV31]**](SDTargetExpressionV31.md) | The targeting expression to match against.  ------- Applicable to contextual targeting (T00020) ------- * A &#39;TargetingExpression&#39; in a contextual targeting campaign can only contain &#39;TargetingPredicate&#39; components. * Expressions must specify either a category predicate or an ASIN predicate, but never both. * Only one category may be specified per targeting expression. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.  ------- Applicable to audiences or contextual targeting (T00030) ------- * A &#39;TargetingExpression&#39; in an audiences or contextual campaign can only contain &#39;TargetingPredicateNested&#39; components. | 

## Example

```python
from openapi_client.models.sd_targeting_clause_v31 import SDTargetingClauseV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingClauseV31 from a JSON string
sd_targeting_clause_v31_instance = SDTargetingClauseV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingClauseV31.to_json())

# convert the object into a dict
sd_targeting_clause_v31_dict = sd_targeting_clause_v31_instance.to_dict()
# create an instance of SDTargetingClauseV31 from a dict
sd_targeting_clause_v31_from_dict = SDTargetingClauseV31.from_dict(sd_targeting_clause_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


