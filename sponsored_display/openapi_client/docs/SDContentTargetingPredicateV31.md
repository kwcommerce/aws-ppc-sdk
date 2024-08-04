# SDContentTargetingPredicateV31

A predicate to match against in the content targeting expression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** | The value to be targeted. | 

## Example

```python
from openapi_client.models.sd_content_targeting_predicate_v31 import SDContentTargetingPredicateV31

# TODO update the JSON string below
json = "{}"
# create an instance of SDContentTargetingPredicateV31 from a JSON string
sd_content_targeting_predicate_v31_instance = SDContentTargetingPredicateV31.from_json(json)
# print the JSON string representation of the object
print(SDContentTargetingPredicateV31.to_json())

# convert the object into a dict
sd_content_targeting_predicate_v31_dict = sd_content_targeting_predicate_v31_instance.to_dict()
# create an instance of SDContentTargetingPredicateV31 from a dict
sd_content_targeting_predicate_v31_from_dict = SDContentTargetingPredicateV31.from_dict(sd_content_targeting_predicate_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


