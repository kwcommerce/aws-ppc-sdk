# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_headline_recommendation_access_denied_exception import SDHeadlineRecommendationAccessDeniedException

class TestSDHeadlineRecommendationAccessDeniedException(unittest.TestCase):
    """SDHeadlineRecommendationAccessDeniedException unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDHeadlineRecommendationAccessDeniedException:
        """Test SDHeadlineRecommendationAccessDeniedException
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDHeadlineRecommendationAccessDeniedException`
        """
        model = SDHeadlineRecommendationAccessDeniedException()
        if include_optional:
            return SDHeadlineRecommendationAccessDeniedException(
                code = 'ACCESS_DENIED',
                details = ''
            )
        else:
            return SDHeadlineRecommendationAccessDeniedException(
        )
        """

    def testSDHeadlineRecommendationAccessDeniedException(self):
        """Test SDHeadlineRecommendationAccessDeniedException"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
