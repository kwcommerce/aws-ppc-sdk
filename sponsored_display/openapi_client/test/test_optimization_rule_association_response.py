# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.optimization_rule_association_response import OptimizationRuleAssociationResponse

class TestOptimizationRuleAssociationResponse(unittest.TestCase):
    """OptimizationRuleAssociationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptimizationRuleAssociationResponse:
        """Test OptimizationRuleAssociationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptimizationRuleAssociationResponse`
        """
        model = OptimizationRuleAssociationResponse()
        if include_optional:
            return OptimizationRuleAssociationResponse(
                code = '',
                responses = [
                    openapi_client.models.single_optimization_rule_association_response.SingleOptimizationRuleAssociationResponse(
                        code = '', 
                        details = '', 
                        optimization_rule_id = '', )
                    ]
            )
        else:
            return OptimizationRuleAssociationResponse(
        )
        """

    def testOptimizationRuleAssociationResponse(self):
        """Test OptimizationRuleAssociationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
