# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_recommendations_v33 import SDTargetingRecommendationsV33

class TestSDTargetingRecommendationsV33(unittest.TestCase):
    """SDTargetingRecommendationsV33 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingRecommendationsV33:
        """Test SDTargetingRecommendationsV33
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingRecommendationsV33`
        """
        model = SDTargetingRecommendationsV33()
        if include_optional:
            return SDTargetingRecommendationsV33(
                products = [
                    openapi_client.models.sd_product_recommendation_v32.SDProductRecommendationV32(
                        asin = 'B00PN11UNW', 
                        rank = 1, 
                        advertised_asins = [
                            'B00PN11UNW'
                            ], )
                    ],
                categories = [
                    openapi_client.models.sd_category_recommendation_v33.SDCategoryRecommendationV33(
                        category = 7352105011, 
                        name = '', 
                        translated_name = '', 
                        path = [
                            ''
                            ], 
                        translated_path = [
                            ''
                            ], 
                        targetable_asin_count_range = openapi_client.models.sd_category_recommendation_v33_targetable_asin_count_range.SDCategoryRecommendationV33_targetableAsinCountRange(
                            range_lower = 56, 
                            range_upper = 56, ), 
                        rank = 1, )
                    ],
                audiences = [
                    openapi_client.models.sd_audience_category_recommendations.SDAudienceCategoryRecommendations(
                        category = 'In-Market', )
                    ],
                themes = openapi_client.models.sd_theme_recommendations_themes.SDThemeRecommendations_themes(
                    products = [
                        null
                        ], )
            )
        else:
            return SDTargetingRecommendationsV33(
        )
        """

    def testSDTargetingRecommendationsV33(self):
        """Test SDTargetingRecommendationsV33"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
