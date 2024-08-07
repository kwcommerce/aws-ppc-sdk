# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.campaign_response_ex import CampaignResponseEx

class TestCampaignResponseEx(unittest.TestCase):
    """CampaignResponseEx unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CampaignResponseEx:
        """Test CampaignResponseEx
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignResponseEx`
        """
        model = CampaignResponseEx()
        if include_optional:
            return CampaignResponseEx(
                campaign_id = 1.337,
                name = '',
                tactic = 'T00020',
                budget_type = 'daily',
                budget = 1.337,
                start_date = '',
                end_date = '',
                state = 'enabled',
                portfolio_id = 56,
                serving_status = 'ADVERTISER_STATUS_ENABLED',
                cost_type = 'cpc',
                creation_date = 56,
                last_updated_date = 56,
                rule_based_budget = openapi_client.models.rule_based_budget.RuleBasedBudget(
                    is_processing = True, 
                    applicable_rule_name = '', 
                    value = 1.337, 
                    applicable_rule_id = '', )
            )
        else:
            return CampaignResponseEx(
        )
        """

    def testCampaignResponseEx(self):
        """Test CampaignResponseEx"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
