# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_product_recommendation_v32 import SDProductRecommendationV32

class TestSDProductRecommendationV32(unittest.TestCase):
    """SDProductRecommendationV32 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDProductRecommendationV32:
        """Test SDProductRecommendationV32
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDProductRecommendationV32`
        """
        model = SDProductRecommendationV32()
        if include_optional:
            return SDProductRecommendationV32(
                asin = 'B00PN11UNW',
                rank = 1,
                advertised_asins = [
                    'B00PN11UNW'
                    ]
            )
        else:
            return SDProductRecommendationV32(
        )
        """

    def testSDProductRecommendationV32(self):
        """Test SDProductRecommendationV32"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
