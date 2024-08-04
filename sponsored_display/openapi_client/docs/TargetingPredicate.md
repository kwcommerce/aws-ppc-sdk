# TargetingPredicate

A predicate to match against in the targeting expression (only applicable to contextual targeting - T00020).  * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system. * Brand, price, and review predicates are optional and may only be specified if category is also specified. * Review predicates accept numbers between 0 and 5 and are inclusive. * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** | The value to be targeted. | [optional] 

## Example

```python
from openapi_client.models.targeting_predicate import TargetingPredicate

# TODO update the JSON string below
json = "{}"
# create an instance of TargetingPredicate from a JSON string
targeting_predicate_instance = TargetingPredicate.from_json(json)
# print the JSON string representation of the object
print(TargetingPredicate.to_json())

# convert the object into a dict
targeting_predicate_dict = targeting_predicate_instance.to_dict()
# create an instance of TargetingPredicate from a dict
targeting_predicate_from_dict = TargetingPredicate.from_dict(targeting_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


