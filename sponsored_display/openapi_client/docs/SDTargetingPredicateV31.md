# SDTargetingPredicateV31

A predicate to match against in the Targeting Expression (only applicable to contextual targeting - T00020).  * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system. * Brand, price, and review predicates are optional and may only be specified if category is also specified. * Review predicates accept numbers between 0 and 5 and are inclusive. * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | The value to be targeted. | [optional] 

## Example

```python
from openapi_client.models.sd_targeting_predicate_v31 import SDTargetingPredicateV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDTargetingPredicateV31 from a JSON string
sd_targeting_predicate_v31_instance = SDTargetingPredicateV31.from_json(json)
# print the JSON string representation of the object
print(SDTargetingPredicateV31.to_json())

# convert the object into a dict
sd_targeting_predicate_v31_dict = sd_targeting_predicate_v31_instance.to_dict()
# create an instance of SDTargetingPredicateV31 from a dict
sd_targeting_predicate_v31_from_dict = SDTargetingPredicateV31.from_dict(sd_targeting_predicate_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


