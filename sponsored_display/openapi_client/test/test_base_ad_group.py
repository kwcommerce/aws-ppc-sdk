# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.base_ad_group import BaseAdGroup

class TestBaseAdGroup(unittest.TestCase):
    """BaseAdGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseAdGroup:
        """Test BaseAdGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseAdGroup`
        """
        model = BaseAdGroup()
        if include_optional:
            return BaseAdGroup(
                name = '',
                campaign_id = 56,
                default_bid = 1.337,
                bid_optimization = 'reach',
                state = 'enabled'
            )
        else:
            return BaseAdGroup(
        )
        """

    def testBaseAdGroup(self):
        """Test BaseAdGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
