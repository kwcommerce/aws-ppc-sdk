# TargetingPredicateNested

A behavioral event and list of targeting predicates that represents an audience to target (only applicable to audience targeting - T00030).  * For manual ASIN-grain targeting, the value array must contain only, 'exactProduct', 'similarProduct', 'relatedProduct' and 'lookback' TargetingPredicateBase components. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'. * For manual Category-grain targeting, the value array must contain a 'lookback' and 'asinCategorySameAs' TargetingPredicateBase component, which can be further refined with optional brand, price, star-rating and shipping eligibility refinements. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'. * For Amazon Audiences targeting, the TargetingPredicateNested type should be set to 'audience' and the value array should include one TargetingPredicateBase component with type set to 'audienceSameAs'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | [**List[TargetingPredicateBase]**](TargetingPredicateBase.md) |  | [optional] 

## Example

```python
from openapi_client.models.targeting_predicate_nested import TargetingPredicateNested

# TODO update the JSON string below
json = "{}"
# create an instance of TargetingPredicateNested from a JSON string
targeting_predicate_nested_instance = TargetingPredicateNested.from_json(json)
# print the JSON string representation of the object
print(TargetingPredicateNested.to_json())

# convert the object into a dict
targeting_predicate_nested_dict = targeting_predicate_nested_instance.to_dict()
# create an instance of TargetingPredicateNested from a dict
targeting_predicate_nested_from_dict = TargetingPredicateNested.from_dict(targeting_predicate_nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


