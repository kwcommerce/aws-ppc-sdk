# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_recommendations_v31 import SDTargetingRecommendationsV31

class TestSDTargetingRecommendationsV31(unittest.TestCase):
    """SDTargetingRecommendationsV31 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingRecommendationsV31:
        """Test SDTargetingRecommendationsV31
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingRecommendationsV31`
        """
        model = SDTargetingRecommendationsV31()
        if include_optional:
            return SDTargetingRecommendationsV31(
                products = [
                    openapi_client.models.sd_product_recommendation.SDProductRecommendation(
                        asin = 'B00PN11UNW', 
                        rank = 1, )
                    ],
                categories = [
                    openapi_client.models.sd_category_recommendation.SDCategoryRecommendation(
                        category = 7352105011, 
                        name = '', 
                        path = [
                            ''
                            ], 
                        targetable_asin_count_range = openapi_client.models.sd_category_recommendation_targetable_asin_count_range.SDCategoryRecommendation_targetableAsinCountRange(
                            range_lower = 56, 
                            range_upper = 56, ), 
                        rank = 1, )
                    ]
            )
        else:
            return SDTargetingRecommendationsV31(
        )
        """

    def testSDTargetingRecommendationsV31(self):
        """Test SDTargetingRecommendationsV31"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
