# SDTargetingPredicateNestedV31

A behavioral event and list of targeting predicates that represents an audience to target (only applicable to audience targeting - T00030).  * For manual ASIN-grain targeting, the value array must contain only, 'exactProduct', 'similarProduct', 'relatedProduct' and 'lookback' TargetingPredicateBase components. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'. * For manual Category-grain targeting, the value array must contain a 'lookback' and 'asinCategorySameAs' TargetingPredicateBase component, which can be further refined with optional brand, price, star-rating and shipping eligibility refinements. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'. * For manual Category-grain targeting, the value array must contain a 'lookback' and 'asinCategorySameAs' TargetingPredicateBase component, which can be further refined with optional brand, price, star-rating and shipping eligibility refinements. * For Amazon Audiences targeting, the TargetingPredicateNested type should be set to 'audience' and the value array should include one TargetingPredicateBase component with type set to 'audienceSameAs'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | [**List[SDTargetingPredicateBaseV31]**](SDTargetingPredicateBaseV31.md) |  | 

## Example

```python
from openapi_client.models.sd_targeting_predicate_nested_v31 import SDTargetingPredicateNestedV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingPredicateNestedV31 from a JSON string
sd_targeting_predicate_nested_v31_instance = SDTargetingPredicateNestedV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingPredicateNestedV31.to_json())

# convert the object into a dict
sd_targeting_predicate_nested_v31_dict = sd_targeting_predicate_nested_v31_instance.to_dict()
# create an instance of SDTargetingPredicateNestedV31 from a dict
sd_targeting_predicate_nested_v31_from_dict = SDTargetingPredicateNestedV31.from_dict(sd_targeting_predicate_nested_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


