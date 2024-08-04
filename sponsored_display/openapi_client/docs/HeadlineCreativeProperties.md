# HeadlineCreativeProperties

User-customizable properties of a creative with headline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headline** | **str** | A marketing phrase to display on the ad. This field is optional and mutable. Maximum number of characters allowed is 50. | [optional] 
**has_terms_and_conditions** | **bool** | Indicates that the ad promotes a free product or service (e.g., &#39;buy one get one free&#39; or &#39;free one-month trial&#39;) and has qualifying terms and conditions applicable to your customer. Only supported for productAds with landingPageType of OFF_AMAZON_LINK. LandingPageURL must link out to a page detailing terms and conditions or contain a link to those. | [optional] 

## Example

```python
from openapi_client.models.headline_creative_properties import HeadlineCreativeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of HeadlineCreativeProperties from a JSON string
headline_creative_properties_instance = HeadlineCreativeProperties.from_json(json)
# print the JSON string representation of the object
print(HeadlineCreativeProperties.to_json())

# convert the object into a dict
headline_creative_properties_dict = headline_creative_properties_instance.to_dict()
# create an instance of HeadlineCreativeProperties from a dict
headline_creative_properties_from_dict = HeadlineCreativeProperties.from_dict(headline_creative_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


