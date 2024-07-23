# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_bid_recommendations_request_v33 import SDTargetingBidRecommendationsRequestV33

class TestSDTargetingBidRecommendationsRequestV33(unittest.TestCase):
    """SDTargetingBidRecommendationsRequestV33 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingBidRecommendationsRequestV33:
        """Test SDTargetingBidRecommendationsRequestV33
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingBidRecommendationsRequestV33`
        """
        model = SDTargetingBidRecommendationsRequestV33()
        if include_optional:
            return SDTargetingBidRecommendationsRequestV33(
                products = [
                    openapi_client.models.sd_goal_product.SDGoalProduct(
                        asin = 'B00PN11UNW', )
                    ],
                bid_optimization = 'reach',
                cost_type = 'cpc',
                creative_type = 'IMAGE',
                targeting_clauses = [
                    openapi_client.models.sd_targeting_bid_recommendations_request_v33_targeting_clauses_inner.SDTargetingBidRecommendationsRequestV33_targetingClauses_inner(
                        targeting_clause = openapi_client.models.sd_targeting_clause_v31.SDTargetingClauseV31(
                            expression_type = 'manual', 
                            expression = [
                                null
                                ], ), )
                    ]
            )
        else:
            return SDTargetingBidRecommendationsRequestV33(
                bid_optimization = 'reach',
                cost_type = 'cpc',
                targeting_clauses = [
                    openapi_client.models.sd_targeting_bid_recommendations_request_v33_targeting_clauses_inner.SDTargetingBidRecommendationsRequestV33_targetingClauses_inner(
                        targeting_clause = openapi_client.models.sd_targeting_clause_v31.SDTargetingClauseV31(
                            expression_type = 'manual', 
                            expression = [
                                null
                                ], ), )
                    ],
        )
        """

    def testSDTargetingBidRecommendationsRequestV33(self):
        """Test SDTargetingBidRecommendationsRequestV33"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
