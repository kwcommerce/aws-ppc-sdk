# BackgroundCreativeProperties

User-customizable properties of a creative with background. Only supported for productAds with landingPageType of OFF_AMAZON_LINK.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backgrounds** | [**List[Background]**](Background.md) | An optional collection of backgrounds which are displayed on the ad. | [optional] 

## Example

```python
from openapi_client.models.background_creative_properties import BackgroundCreativeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundCreativeProperties from a JSON string
background_creative_properties_instance = BackgroundCreativeProperties.from_json(json)
# print the JSON string representation of the object
print(BackgroundCreativeProperties.to_json())

# convert the object into a dict
background_creative_properties_dict = background_creative_properties_instance.to_dict()
# create an instance of BackgroundCreativeProperties from a dict
background_creative_properties_from_dict = BackgroundCreativeProperties.from_dict(background_creative_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


