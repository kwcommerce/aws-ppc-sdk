# CreateTargetingClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**bid** | **float** | The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign&#39;s marketplace; for a list of maximum allowable bids, find the [\&quot;Bid constraints by marketplace\&quot; table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause&#39;s adGroup has an enabled optimization rule. | [optional] 
**ad_group_id** | **int** | The identifier of the ad group. | 
**expression_type** | **str** | Tactic T00020 ad groups only allow manual targeting. | 
**expression** | [**List[CreateTargetingExpressionInner]**](CreateTargetingExpressionInner.md) | The targeting expression to match against.  ------- Applicable to contextual targeting (T00020) ------- * A &#39;TargetingExpression&#39; in a contextual targeting campaign can only contain &#39;TargetingPredicate&#39; components. * Expressions must specify either a category predicate or an ASIN predicate, but never both. * Only one category may be specified per targeting expression. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.  ------- Applicable to audiences or contextual targeting (T00030) ------- * A &#39;TargetingExpression&#39; in a audiences or contextual campaign can only contain &#39;TargetingPredicateNested&#39; components. * Expressions must specify either auto ASIN-grain (exact products), manual ASIN-grain (similar products), or manual category-grain targeting. | 

## Example

```python
from openapi_client.models.create_targeting_clause import CreateTargetingClause

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetingClause from a JSON string
create_targeting_clause_instance = CreateTargetingClause.from_json(json)
# print the JSON string representation of the object
print(CreateTargetingClause.to_json())

# convert the object into a dict
create_targeting_clause_dict = create_targeting_clause_instance.to_dict()
# create an instance of CreateTargetingClause from a dict
create_targeting_clause_from_dict = CreateTargetingClause.from_dict(create_targeting_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


