# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_headline_recommendation_identifier_notfound_exception import SDHeadlineRecommendationIdentifierNotfoundException

class TestSDHeadlineRecommendationIdentifierNotfoundException(unittest.TestCase):
    """SDHeadlineRecommendationIdentifierNotfoundException unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDHeadlineRecommendationIdentifierNotfoundException:
        """Test SDHeadlineRecommendationIdentifierNotfoundException
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDHeadlineRecommendationIdentifierNotfoundException`
        """
        model = SDHeadlineRecommendationIdentifierNotfoundException()
        if include_optional:
            return SDHeadlineRecommendationIdentifierNotfoundException(
                code = 'IDENTIFIER_NOT_FOUND',
                details = ''
            )
        else:
            return SDHeadlineRecommendationIdentifierNotfoundException(
        )
        """

    def testSDHeadlineRecommendationIdentifierNotfoundException(self):
        """Test SDHeadlineRecommendationIdentifierNotfoundException"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
