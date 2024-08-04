# Image

This field denotes image which is displayed on the ad. This can either be a brand logo or a custom image. This field is optional and mutable. For custom image, both rectCustomImage and squareCustomImage should use the same asset id and asset version. Specific restrictions based on the Image type are listed in the following table. |Image type|Maximum file size|Minimum width|Minimum height|Accepted file formats| |------|-----------|-----------|-----------|-----------| |Custom Image|5MB|1200|628|JPEG, JPG, PNG, GIF| |Brand Logo|1MB|600|100|JPEG, JPG, PNG| Note: For square custom images the cropped image should be 628x628 at minimum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The unique identifier of the image asset. This assetId comes from the Creative Asset Library. | 
**asset_version** | **str** | The identifier of the particular image assetversion. | 
**cropping_coordinates** | [**ImageCroppingCoordinates**](ImageCroppingCoordinates.md) |  | [optional] 

## Example

```python
from openapi_client.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print(Image.to_json())

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_from_dict = Image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


