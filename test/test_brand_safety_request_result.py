# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.brand_safety_request_result import BrandSafetyRequestResult

class TestBrandSafetyRequestResult(unittest.TestCase):
    """BrandSafetyRequestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandSafetyRequestResult:
        """Test BrandSafetyRequestResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandSafetyRequestResult`
        """
        model = BrandSafetyRequestResult()
        if include_optional:
            return BrandSafetyRequestResult(
                status = 'SUCCESS',
                details = '',
                domain_id = 56,
                name = ''
            )
        else:
            return BrandSafetyRequestResult(
        )
        """

    def testBrandSafetyRequestResult(self):
        """Test BrandSafetyRequestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
