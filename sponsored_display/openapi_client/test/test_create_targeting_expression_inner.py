# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_targeting_expression_inner import CreateTargetingExpressionInner

class TestCreateTargetingExpressionInner(unittest.TestCase):
    """CreateTargetingExpressionInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTargetingExpressionInner:
        """Test CreateTargetingExpressionInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTargetingExpressionInner`
        """
        model = CreateTargetingExpressionInner()
        if include_optional:
            return CreateTargetingExpressionInner(
                type = 'asinSameAs',
                value = [
                    openapi_client.models.targeting_predicate_base.TargetingPredicateBase(
                        type = 'asinCategorySameAs', )
                    ]
            )
        else:
            return CreateTargetingExpressionInner(
        )
        """

    def testCreateTargetingExpressionInner(self):
        """Test CreateTargetingExpressionInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
