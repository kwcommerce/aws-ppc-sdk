# LogoCreativeProperties

User-customizable properties of a creative with a logo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_logo** | [**Image**](Image.md) |  | [optional] 

## Example

```python
from openapi_client.models.logo_creative_properties import LogoCreativeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of LogoCreativeProperties from a JSON string
logo_creative_properties_instance = LogoCreativeProperties.from_json(json)
# print the JSON string representation of the object
print(LogoCreativeProperties.to_json())

# convert the object into a dict
logo_creative_properties_dict = logo_creative_properties_instance.to_dict()
# create an instance of LogoCreativeProperties from a dict
logo_creative_properties_from_dict = LogoCreativeProperties.from_dict(logo_creative_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


