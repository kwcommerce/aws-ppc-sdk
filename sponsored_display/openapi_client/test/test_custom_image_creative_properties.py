# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.custom_image_creative_properties import CustomImageCreativeProperties

class TestCustomImageCreativeProperties(unittest.TestCase):
    """CustomImageCreativeProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomImageCreativeProperties:
        """Test CustomImageCreativeProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomImageCreativeProperties`
        """
        model = CustomImageCreativeProperties()
        if include_optional:
            return CustomImageCreativeProperties(
                rect_custom_image = openapi_client.models.image.Image(
                    asset_id = '', 
                    asset_version = '', 
                    cropping_coordinates = openapi_client.models.image_cropping_coordinates.Image_croppingCoordinates(
                        top = 0, 
                        left = 0, 
                        width = 0, 
                        height = 0, ), ),
                square_custom_image = openapi_client.models.image.Image(
                    asset_id = '', 
                    asset_version = '', 
                    cropping_coordinates = openapi_client.models.image_cropping_coordinates.Image_croppingCoordinates(
                        top = 0, 
                        left = 0, 
                        width = 0, 
                        height = 0, ), ),
                square_images = [
                    openapi_client.models.image.Image(
                        asset_id = '', 
                        asset_version = '', 
                        cropping_coordinates = openapi_client.models.image_cropping_coordinates.Image_croppingCoordinates(
                            top = 0, 
                            left = 0, 
                            width = 0, 
                            height = 0, ), )
                    ],
                horizontal_images = [
                    openapi_client.models.image.Image(
                        asset_id = '', 
                        asset_version = '', 
                        cropping_coordinates = openapi_client.models.image_cropping_coordinates.Image_croppingCoordinates(
                            top = 0, 
                            left = 0, 
                            width = 0, 
                            height = 0, ), )
                    ],
                vertical_images = [
                    openapi_client.models.image.Image(
                        asset_id = '', 
                        asset_version = '', 
                        cropping_coordinates = openapi_client.models.image_cropping_coordinates.Image_croppingCoordinates(
                            top = 0, 
                            left = 0, 
                            width = 0, 
                            height = 0, ), )
                    ]
            )
        else:
            return CustomImageCreativeProperties(
        )
        """

    def testCustomImageCreativeProperties(self):
        """Test CustomImageCreativeProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
