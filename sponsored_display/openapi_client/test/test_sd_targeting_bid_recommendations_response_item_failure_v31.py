# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_bid_recommendations_response_item_failure_v31 import SDTargetingBidRecommendationsResponseItemFailureV31

class TestSDTargetingBidRecommendationsResponseItemFailureV31(unittest.TestCase):
    """SDTargetingBidRecommendationsResponseItemFailureV31 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingBidRecommendationsResponseItemFailureV31:
        """Test SDTargetingBidRecommendationsResponseItemFailureV31
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingBidRecommendationsResponseItemFailureV31`
        """
        model = SDTargetingBidRecommendationsResponseItemFailureV31()
        if include_optional:
            return SDTargetingBidRecommendationsResponseItemFailureV31(
                code = '400',
                details = 'Targeting expression does not conform to language specific rules.'
            )
        else:
            return SDTargetingBidRecommendationsResponseItemFailureV31(
                code = '400',
                details = 'Targeting expression does not conform to language specific rules.',
        )
        """

    def testSDTargetingBidRecommendationsResponseItemFailureV31(self):
        """Test SDTargetingBidRecommendationsResponseItemFailureV31"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
