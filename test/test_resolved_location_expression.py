# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.resolved_location_expression import ResolvedLocationExpression

class TestResolvedLocationExpression(unittest.TestCase):
    """ResolvedLocationExpression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResolvedLocationExpression:
        """Test ResolvedLocationExpression
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResolvedLocationExpression`
        """
        model = ResolvedLocationExpression()
        if include_optional:
            return ResolvedLocationExpression(
                type = 'location',
                value = 'New York City, New York, US'
            )
        else:
            return ResolvedLocationExpression(
        )
        """

    def testResolvedLocationExpression(self):
        """Test ResolvedLocationExpression"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()