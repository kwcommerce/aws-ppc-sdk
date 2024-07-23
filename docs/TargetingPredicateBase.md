# TargetingPredicateBase

A predicate to match against inside the TargetingPredicateNested component (only applicable to audience targeting - T00030).  * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system. * Brand, price, and review predicates are optional and may only be specified if category is also specified. * Review predicates accept numbers between 0 and 5 and are inclusive. * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive. * The 'exactProduct', 'similarProduct', 'relatedProduct', and 'negative' types do not utilize the value field. * The only type currently applicable to Amazon Audiences targeting is 'audienceSameAs'. * A 'relatedProduct' TargetingPredicateBase will Target an audience that has purchased a related product in the past 7,14,30,60,90,180, or 365 days.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** | The value to be targeted. | [optional] 

## Example

```python
from openapi_client.models.targeting_predicate_base import TargetingPredicateBase

# TODO update the JSON string below
json = "{}"
# create an instance of TargetingPredicateBase from a JSON string
targeting_predicate_base_instance = TargetingPredicateBase.from_json(json)
# print the JSON string representation of the object
print(TargetingPredicateBase.to_json())

# convert the object into a dict
targeting_predicate_base_dict = targeting_predicate_base_instance.to_dict()
# create an instance of TargetingPredicateBase from a dict
targeting_predicate_base_from_dict = TargetingPredicateBase.from_dict(targeting_predicate_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


