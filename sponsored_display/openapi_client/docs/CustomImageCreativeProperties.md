# CustomImageCreativeProperties

User-customizable properties of a custom image creative.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rect_custom_image** | [**Image**](Image.md) |  | [optional] 
**square_custom_image** | [**Image**](Image.md) |  | [optional] 
**square_images** | [**List[Image]**](Image.md) | An optional collection of 1:1 square images which are displayed on the ad. | [optional] 
**horizontal_images** | [**List[Image]**](Image.md) | An optional collection of 1.91:1 horizontal images which are displayed on the ad. | [optional] 
**vertical_images** | [**List[Image]**](Image.md) | An optional collection of 9:16 vertical images which are displayed on the ad. | [optional] 

## Example

```python
from openapi_client.models.custom_image_creative_properties import CustomImageCreativeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CustomImageCreativeProperties from a JSON string
custom_image_creative_properties_instance = CustomImageCreativeProperties.from_json(json)
# print the JSON string representation of the object
print(CustomImageCreativeProperties.to_json())

# convert the object into a dict
custom_image_creative_properties_dict = custom_image_creative_properties_instance.to_dict()
# create an instance of CustomImageCreativeProperties from a dict
custom_image_creative_properties_from_dict = CustomImageCreativeProperties.from_dict(custom_image_creative_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


