# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.creatives_api import CreativesApi


class TestCreativesApi(unittest.TestCase):
    """CreativesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CreativesApi()

    def tearDown(self) -> None:
        pass

    def test_create_creatives(self) -> None:
        """Test case for create_creatives

        A POST request of one or more creatives.
        """
        pass

    def test_list_creative_moderations(self) -> None:
        """Test case for list_creative_moderations

        Gets a list of creative moderations
        """
        pass

    def test_list_creatives(self) -> None:
        """Test case for list_creatives

        Gets a list of creatives
        """
        pass

    def test_post_creative_preview(self) -> None:
        """Test case for post_creative_preview

        Gets creative preview HTML.
        """
        pass

    def test_update_creatives(self) -> None:
        """Test case for update_creatives

        Updates one or more creatives.
        """
        pass


if __name__ == '__main__':
    unittest.main()
