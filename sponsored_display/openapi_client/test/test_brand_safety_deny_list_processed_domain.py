# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.brand_safety_deny_list_processed_domain import BrandSafetyDenyListProcessedDomain

class TestBrandSafetyDenyListProcessedDomain(unittest.TestCase):
    """BrandSafetyDenyListProcessedDomain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandSafetyDenyListProcessedDomain:
        """Test BrandSafetyDenyListProcessedDomain
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandSafetyDenyListProcessedDomain`
        """
        model = BrandSafetyDenyListProcessedDomain()
        if include_optional:
            return BrandSafetyDenyListProcessedDomain(
                domain_id = 56,
                name = '',
                type = 'WEBSITE',
                state = 'ENABLED',
                created_at = '2018-09-16T11:43:21Z',
                last_modified = '2018-09-16T11:43:21Z'
            )
        else:
            return BrandSafetyDenyListProcessedDomain(
        )
        """

    def testBrandSafetyDenyListProcessedDomain(self):
        """Test BrandSafetyDenyListProcessedDomain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
