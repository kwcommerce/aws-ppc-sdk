# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_target_expression_v32 import SDTargetExpressionV32

class TestSDTargetExpressionV32(unittest.TestCase):
    """SDTargetExpressionV32 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetExpressionV32:
        """Test SDTargetExpressionV32
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetExpressionV32`
        """
        model = SDTargetExpressionV32()
        if include_optional:
            return SDTargetExpressionV32(
                type = 'asinSameAs',
                value = 'amzn1.iab-content.325'
            )
        else:
            return SDTargetExpressionV32(
                type = 'asinSameAs',
                value = 'amzn1.iab-content.325',
        )
        """

    def testSDTargetExpressionV32(self):
        """Test SDTargetExpressionV32"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
