# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_recommendations_products_v31_inner import SDTargetingRecommendationsProductsV31Inner

class TestSDTargetingRecommendationsProductsV31Inner(unittest.TestCase):
    """SDTargetingRecommendationsProductsV31Inner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingRecommendationsProductsV31Inner:
        """Test SDTargetingRecommendationsProductsV31Inner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingRecommendationsProductsV31Inner`
        """
        model = SDTargetingRecommendationsProductsV31Inner()
        if include_optional:
            return SDTargetingRecommendationsProductsV31Inner(
                asin = 'B00PN11UNW',
                landing_page_type = 'OFF_AMAZON_LINK',
                landing_page_url = ''
            )
        else:
            return SDTargetingRecommendationsProductsV31Inner(
        )
        """

    def testSDTargetingRecommendationsProductsV31Inner(self):
        """Test SDTargetingRecommendationsProductsV31Inner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
