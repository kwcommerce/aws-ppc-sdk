# SDForecastRequestTargetingClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**bid** | **float** | The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign&#39;s marketplace; for a list of maximum allowable bids, find the [\&quot;Bid constraints by marketplace\&quot; table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause&#39;s adGroup has an enabled optimization rule. | [optional] 
**target_id** | **int** |  | [optional] 
**ad_group_id** | **int** | The identifier of the ad group. | [optional] 
**expression_type** | **str** | Tactic T00020 &amp; T00030 ad groups should use &#39;manual&#39; targeting. | [optional] 
**expression** | [**List[TargetingExpressionInner]**](TargetingExpressionInner.md) | The targeting expression to match against.  ------- Applicable to contextual or content targeting (T00020) ------- * A &#39;TargetingExpression&#39; in a contextual targeting campaign can contain &#39;TargetingPredicate&#39; or &#39;ContentTargetingPredicate&#39; components. * Contextual expressions must specify either a category predicate or an ASIN predicate, but never both. * Only one category may be specified per targeting expression. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.  ------- Applicable to audience targeting (T00030) ------- * A &#39;TargetingExpression&#39; in an audience campaign can contain &#39;TargetingPredicateNested&#39; or &#39;ContentTargetingPredicate&#39; components. * Expressions must specify ASIN-grain (&#39;exactProduct&#39;), manual ASIN-grain (&#39;relatedProducts&#39; or &#39;relatedProducts&#39;), or category-grain targeting. | [optional] 
**resolved_expression** | [**List[TargetingExpressionInner]**](TargetingExpressionInner.md) | The targeting expression to match against.  ------- Applicable to contextual or content targeting (T00020) ------- * A &#39;TargetingExpression&#39; in a contextual targeting campaign can contain &#39;TargetingPredicate&#39; or &#39;ContentTargetingPredicate&#39; components. * Contextual expressions must specify either a category predicate or an ASIN predicate, but never both. * Only one category may be specified per targeting expression. * Only one brand may be specified per targeting expression. * Only one asin may be specified per targeting expression. * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.  ------- Applicable to audience targeting (T00030) ------- * A &#39;TargetingExpression&#39; in an audience campaign can contain &#39;TargetingPredicateNested&#39; or &#39;ContentTargetingPredicate&#39; components. * Expressions must specify ASIN-grain (&#39;exactProduct&#39;), manual ASIN-grain (&#39;relatedProducts&#39; or &#39;relatedProducts&#39;), or category-grain targeting. | [optional] 

## Example

```python
from openapi_client.models.sd_forecast_request_targeting_clause import SDForecastRequestTargetingClause

# TODO update the JSON string below
json = "{}"
# create an instance of SDForecastRequestTargetingClause from a JSON string
sd_forecast_request_targeting_clause_instance = SDForecastRequestTargetingClause.from_json(json)
# print the JSON string representation of the object
print(SDForecastRequestTargetingClause.to_json())

# convert the object into a dict
sd_forecast_request_targeting_clause_dict = sd_forecast_request_targeting_clause_instance.to_dict()
# create an instance of SDForecastRequestTargetingClause from a dict
sd_forecast_request_targeting_clause_from_dict = SDForecastRequestTargetingClause.from_dict(sd_forecast_request_targeting_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


