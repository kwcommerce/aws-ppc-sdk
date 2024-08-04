# CreativeProperties

Select customizations on your creative from any combination of headline, logo, custom image and backgrounds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headline** | **str** | A marketing phrase to display on the ad. This field is optional and mutable. Maximum number of characters allowed is 50. | [optional] 
**has_terms_and_conditions** | **bool** | Indicates that the ad promotes a free product or service (e.g., &#39;buy one get one free&#39; or &#39;free one-month trial&#39;) and has qualifying terms and conditions applicable to your customer. Only supported for productAds with landingPageType of OFF_AMAZON_LINK. LandingPageURL must link out to a page detailing terms and conditions or contain a link to those. | [optional] 
**brand_logo** | [**Image**](Image.md) |  | [optional] 
**rect_custom_image** | [**Image**](Image.md) |  | [optional] 
**square_custom_image** | [**Image**](Image.md) |  | [optional] 
**square_images** | [**List[Image]**](Image.md) | An optional collection of 1:1 square images which are displayed on the ad. | [optional] 
**horizontal_images** | [**List[Image]**](Image.md) | An optional collection of 1.91:1 horizontal images which are displayed on the ad. | [optional] 
**vertical_images** | [**List[Image]**](Image.md) | An optional collection of 9:16 vertical images which are displayed on the ad. | [optional] 
**video** | [**Video**](Video.md) |  | [optional] 
**backgrounds** | [**List[Background]**](Background.md) | An optional collection of backgrounds which are displayed on the ad. | [optional] 
**call_to_actions** | [**List[CallToAction]**](CallToAction.md) |  | [optional] 

## Example

```python
from openapi_client.models.creative_properties import CreativeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CreativeProperties from a JSON string
creative_properties_instance = CreativeProperties.from_json(json)
# print the JSON string representation of the object
print(CreativeProperties.to_json())

# convert the object into a dict
creative_properties_dict = creative_properties_instance.to_dict()
# create an instance of CreativeProperties from a dict
creative_properties_from_dict = CreativeProperties.from_dict(creative_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


