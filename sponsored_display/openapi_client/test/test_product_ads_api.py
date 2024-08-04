# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.product_ads_api import ProductAdsApi


class TestProductAdsApi(unittest.TestCase):
    """ProductAdsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductAdsApi()

    def tearDown(self) -> None:
        pass

    def test_archive_product_ad(self) -> None:
        """Test case for archive_product_ad

        Sets the status of a sproduct ad to archived.
        """
        pass

    def test_create_product_ads(self) -> None:
        """Test case for create_product_ads

        Creates one or more product ads.
        """
        pass

    def test_get_product_ad(self) -> None:
        """Test case for get_product_ad

        Gets a requested product ad.
        """
        pass

    def test_get_product_ad_response_ex(self) -> None:
        """Test case for get_product_ad_response_ex

        Gets extended information for a product ad.
        """
        pass

    def test_list_product_ads(self) -> None:
        """Test case for list_product_ads

        Gets a list of product ads.
        """
        pass

    def test_list_product_ads_ex(self) -> None:
        """Test case for list_product_ads_ex

        Gets a list of product ads with extended fields.
        """
        pass

    def test_update_product_ads(self) -> None:
        """Test case for update_product_ads

        Updates one or more product ads.
        """
        pass


if __name__ == '__main__':
    unittest.main()