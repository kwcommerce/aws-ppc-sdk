# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.base_campaign import BaseCampaign

class TestBaseCampaign(unittest.TestCase):
    """BaseCampaign unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseCampaign:
        """Test BaseCampaign
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseCampaign`
        """
        model = BaseCampaign()
        if include_optional:
            return BaseCampaign(
                name = '',
                budget_type = 'daily',
                budget = 3.00,
                start_date = '20190101',
                end_date = '',
                cost_type = 'cpc',
                state = 'enabled',
                portfolio_id = 56
            )
        else:
            return BaseCampaign(
        )
        """

    def testBaseCampaign(self):
        """Test BaseCampaign"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
