# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_targeting_clause_v32 import SDTargetingClauseV32

class TestSDTargetingClauseV32(unittest.TestCase):
    """SDTargetingClauseV32 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDTargetingClauseV32:
        """Test SDTargetingClauseV32
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDTargetingClauseV32`
        """
        model = SDTargetingClauseV32()
        if include_optional:
            return SDTargetingClauseV32(
                expression_type = 'manual',
                expression = [
                    null
                    ]
            )
        else:
            return SDTargetingClauseV32(
                expression_type = 'manual',
                expression = [
                    null
                    ],
        )
        """

    def testSDTargetingClauseV32(self):
        """Test SDTargetingClauseV32"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()