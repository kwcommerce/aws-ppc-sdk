# CreativePreviewConfiguration

Optional configuration for creative preview.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | [**CreativePreviewConfigurationSize**](CreativePreviewConfigurationSize.md) |  | [optional] 
**products** | [**List[CreativePreviewConfigurationProductsInner]**](CreativePreviewConfigurationProductsInner.md) | The products to preview. Currently only the first product is previewable. | [optional] 
**landing_page_url** | **str** | The URL where customers will land after clicking on its link. Must be provided if a LandingPageType is set. Please note that if a single product ad sets the landing page url, only one product ad can be added to the ad group. This field is not supported when using ASIN or SKU fields. ||Specifications| |------------------|------------------| |LandingPageType| Description| |STORE| The url should be in the format of https://www.amazon.com/stores/* (using a correct Amazon url based on the marketplace)| |OFF_AMAZON_LINK| The url should be in the format of https://www.****.com. Note that this LandingPageType is not supported when using ASIN or SKU fields. A custom creative of headline, logo, image are require for this LandingPageType. | |MOMENT| Not yet supported. The url should be in the format of https://www.amazon.com/moments/promotion/{campaignId} (using a correct Amazon url based on the marketplace)| | [optional] 
**landing_page_type** | [**LandingPageType**](LandingPageType.md) |  | [optional] 
**ad_name** | **str** | The name of the ad. Note that this field is not supported when using ASIN or SKU fields. | [optional] 
**is_mobile** | **bool** | Preview the creative as if it is on a mobile environment. | [optional] 
**is_on_amazon** | **bool** | Preview the creative as if it is on an amazon site or third party site. The main difference is whether the preview will contain an AdChoices icon. | [optional] 

## Example

```python
from openapi_client.models.creative_preview_configuration import CreativePreviewConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CreativePreviewConfiguration from a JSON string
creative_preview_configuration_instance = CreativePreviewConfiguration.from_json(json)
# print the JSON string representation of the object
print(CreativePreviewConfiguration.to_json())

# convert the object into a dict
creative_preview_configuration_dict = creative_preview_configuration_instance.to_dict()
# create an instance of CreativePreviewConfiguration from a dict
creative_preview_configuration_from_dict = CreativePreviewConfiguration.from_dict(creative_preview_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


