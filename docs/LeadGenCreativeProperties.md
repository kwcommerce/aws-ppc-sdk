# LeadGenCreativeProperties

User-customizable properties of a creative with lead generation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_to_actions** | [**List[CallToAction]**](CallToAction.md) |  | [optional] 

## Example

```python
from openapi_client.models.lead_gen_creative_properties import LeadGenCreativeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of LeadGenCreativeProperties from a JSON string
lead_gen_creative_properties_instance = LeadGenCreativeProperties.from_json(json)
# print the JSON string representation of the object
print(LeadGenCreativeProperties.to_json())

# convert the object into a dict
lead_gen_creative_properties_dict = lead_gen_creative_properties_instance.to_dict()
# create an instance of LeadGenCreativeProperties from a dict
lead_gen_creative_properties_from_dict = LeadGenCreativeProperties.from_dict(lead_gen_creative_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


