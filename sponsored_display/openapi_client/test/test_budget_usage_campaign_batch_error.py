# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.budget_usage_campaign_batch_error import BudgetUsageCampaignBatchError

class TestBudgetUsageCampaignBatchError(unittest.TestCase):
    """BudgetUsageCampaignBatchError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetUsageCampaignBatchError:
        """Test BudgetUsageCampaignBatchError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetUsageCampaignBatchError`
        """
        model = BudgetUsageCampaignBatchError()
        if include_optional:
            return BudgetUsageCampaignBatchError(
                code = '',
                campaign_id = '',
                index = 1.337,
                details = ''
            )
        else:
            return BudgetUsageCampaignBatchError(
        )
        """

    def testBudgetUsageCampaignBatchError(self):
        """Test BudgetUsageCampaignBatchError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
