# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.budget_usage_campaign_response import BudgetUsageCampaignResponse

class TestBudgetUsageCampaignResponse(unittest.TestCase):
    """BudgetUsageCampaignResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetUsageCampaignResponse:
        """Test BudgetUsageCampaignResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetUsageCampaignResponse`
        """
        model = BudgetUsageCampaignResponse()
        if include_optional:
            return BudgetUsageCampaignResponse(
                success = [
                    openapi_client.models.budget_usage_campaign.BudgetUsageCampaign(
                        budget_usage_percent = 1.337, 
                        campaign_id = '', 
                        usage_updated_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        index = 1.337, 
                        budget = 1.337, )
                    ],
                error = [
                    openapi_client.models.budget_usage_campaign_batch_error.BudgetUsageCampaignBatchError(
                        code = '', 
                        campaign_id = '', 
                        index = 1.337, 
                        details = '', )
                    ]
            )
        else:
            return BudgetUsageCampaignResponse(
        )
        """

    def testBudgetUsageCampaignResponse(self):
        """Test BudgetUsageCampaignResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
