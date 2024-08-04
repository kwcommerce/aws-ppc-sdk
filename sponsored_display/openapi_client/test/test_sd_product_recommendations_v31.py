# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_product_recommendations_v31 import SDProductRecommendationsV31

class TestSDProductRecommendationsV31(unittest.TestCase):
    """SDProductRecommendationsV31 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDProductRecommendationsV31:
        """Test SDProductRecommendationsV31
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDProductRecommendationsV31`
        """
        model = SDProductRecommendationsV31()
        if include_optional:
            return SDProductRecommendationsV31(
                products = [
                    openapi_client.models.sd_product_recommendation.SDProductRecommendation(
                        asin = 'B00PN11UNW', 
                        rank = 1, )
                    ]
            )
        else:
            return SDProductRecommendationsV31(
        )
        """

    def testSDProductRecommendationsV31(self):
        """Test SDProductRecommendationsV31"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()