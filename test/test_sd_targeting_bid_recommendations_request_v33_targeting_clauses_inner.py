# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_bid_recommendations_request_v33_targeting_clauses_inner import SDTargetingBidRecommendationsRequestV33TargetingClausesInner

class TestSDTargetingBidRecommendationsRequestV33TargetingClausesInner(unittest.TestCase):
    """SDTargetingBidRecommendationsRequestV33TargetingClausesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingBidRecommendationsRequestV33TargetingClausesInner:
        """Test SDTargetingBidRecommendationsRequestV33TargetingClausesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingBidRecommendationsRequestV33TargetingClausesInner`
        """
        model = SDTargetingBidRecommendationsRequestV33TargetingClausesInner()
        if include_optional:
            return SDTargetingBidRecommendationsRequestV33TargetingClausesInner(
                targeting_clause = openapi_client.models.sd_targeting_clause_v31.SDTargetingClauseV31(
                    expression_type = 'manual', 
                    expression = [
                        null
                        ], )
            )
        else:
            return SDTargetingBidRecommendationsRequestV33TargetingClausesInner(
                targeting_clause = openapi_client.models.sd_targeting_clause_v31.SDTargetingClauseV31(
                    expression_type = 'manual', 
                    expression = [
                        null
                        ], ),
        )
        """

    def testSDTargetingBidRecommendationsRequestV33TargetingClausesInner(self):
        """Test SDTargetingBidRecommendationsRequestV33TargetingClausesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()