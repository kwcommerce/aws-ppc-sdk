# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.base_optimization_rule import BaseOptimizationRule

class TestBaseOptimizationRule(unittest.TestCase):
    """BaseOptimizationRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseOptimizationRule:
        """Test BaseOptimizationRule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseOptimizationRule`
        """
        model = BaseOptimizationRule()
        if include_optional:
            return BaseOptimizationRule(
                state = 'enabled',
                rule_name = '',
                rule_conditions = [
                    openapi_client.models.rule_condition.RuleCondition(
                        metric_name = 'COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS', 
                        comparison_operator = 'LESS_THAN_OR_EQUAL_TO', 
                        threshold = 1.5, )
                    ]
            )
        else:
            return BaseOptimizationRule(
        )
        """

    def testBaseOptimizationRule(self):
        """Test BaseOptimizationRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
