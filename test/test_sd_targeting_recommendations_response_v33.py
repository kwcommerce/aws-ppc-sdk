# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_recommendations_response_v33 import SDTargetingRecommendationsResponseV33

class TestSDTargetingRecommendationsResponseV33(unittest.TestCase):
    """SDTargetingRecommendationsResponseV33 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingRecommendationsResponseV33:
        """Test SDTargetingRecommendationsResponseV33
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingRecommendationsResponseV33`
        """
        model = SDTargetingRecommendationsResponseV33()
        if include_optional:
            return SDTargetingRecommendationsResponseV33(
                recommendations = None
            )
        else:
            return SDTargetingRecommendationsResponseV33(
        )
        """

    def testSDTargetingRecommendationsResponseV33(self):
        """Test SDTargetingRecommendationsResponseV33"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()