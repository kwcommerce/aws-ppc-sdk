# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_recommendations_request_v34 import SDTargetingRecommendationsRequestV34

class TestSDTargetingRecommendationsRequestV34(unittest.TestCase):
    """SDTargetingRecommendationsRequestV34 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingRecommendationsRequestV34:
        """Test SDTargetingRecommendationsRequestV34
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingRecommendationsRequestV34`
        """
        model = SDTargetingRecommendationsRequestV34()
        if include_optional:
            return SDTargetingRecommendationsRequestV34(
                tactic = 'T00020',
                products = [
                    openapi_client.models.sd_goal_product.SDGoalProduct(
                        asin = 'B00PN11UNW', )
                    ],
                type_filter = ["PRODUCT","CATEGORY","AUDIENCE"],
                themes = openapi_client.models.sd_targeting_recommendations_themes.SDTargetingRecommendationsThemes(
                    product = [
                        openapi_client.models.sd_product_targeting_theme.SDProductTargetingTheme(
                            name = '/jUR,rZ0', 
                            expression = [
                                openapi_client.models.sd_product_targeting_theme_expression.SDProductTargetingThemeExpression(
                                    type = 'asinPriceGreaterThan', )
                                ], )
                        ], )
            )
        else:
            return SDTargetingRecommendationsRequestV34(
                tactic = 'T00020',
                products = [
                    openapi_client.models.sd_goal_product.SDGoalProduct(
                        asin = 'B00PN11UNW', )
                    ],
                type_filter = ["PRODUCT","CATEGORY","AUDIENCE"],
        )
        """

    def testSDTargetingRecommendationsRequestV34(self):
        """Test SDTargetingRecommendationsRequestV34"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
