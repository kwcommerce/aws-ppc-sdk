# ImageCroppingCoordinates

Optional cropping coordinates to apply to the image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **int** | Pixel distance from the top edge of the cropping zone to the top edge of the original image. | 
**left** | **int** | Pixel distance from the left edge of the cropping zone to the left edge of the original image. | 
**width** | **int** | Pixel width of the cropping zone. | 
**height** | **int** | Pixel height of the cropping zone. | 

## Example

```python
from openapi_client.models.image_cropping_coordinates import ImageCroppingCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCroppingCoordinates from a JSON string
image_cropping_coordinates_instance = ImageCroppingCoordinates.from_json(json)
# print the JSON string representation of the object
print(ImageCroppingCoordinates.to_json())

# convert the object into a dict
image_cropping_coordinates_dict = image_cropping_coordinates_instance.to_dict()
# create an instance of ImageCroppingCoordinates from a dict
image_cropping_coordinates_from_dict = ImageCroppingCoordinates.from_dict(image_cropping_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


