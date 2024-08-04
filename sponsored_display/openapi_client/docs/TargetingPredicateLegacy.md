# TargetingPredicateLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** | The value to be targeted. | [optional] 
**event_type** | **str** | The type of event that the value applies to. Only available for similarProduct and exactProduct currently. * views event type corresponds to a customer who viewed the detail page of the product(s). | [optional] 

## Example

```python
from openapi_client.models.targeting_predicate_legacy import TargetingPredicateLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of TargetingPredicateLegacy from a JSON string
targeting_predicate_legacy_instance = TargetingPredicateLegacy.from_json(json)
# print the JSON string representation of the object
print(TargetingPredicateLegacy.to_json())

# convert the object into a dict
targeting_predicate_legacy_dict = targeting_predicate_legacy_instance.to_dict()
# create an instance of TargetingPredicateLegacy from a dict
targeting_predicate_legacy_from_dict = TargetingPredicateLegacy.from_dict(targeting_predicate_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


