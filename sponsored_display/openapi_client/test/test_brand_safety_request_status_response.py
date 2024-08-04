# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.brand_safety_request_status_response import BrandSafetyRequestStatusResponse

class TestBrandSafetyRequestStatusResponse(unittest.TestCase):
    """BrandSafetyRequestStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandSafetyRequestStatusResponse:
        """Test BrandSafetyRequestStatusResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandSafetyRequestStatusResponse`
        """
        model = BrandSafetyRequestStatusResponse()
        if include_optional:
            return BrandSafetyRequestStatusResponse(
                request_status = openapi_client.models.brand_safety_request_status.BrandSafetyRequestStatus(
                    request_id = '', 
                    timestamp = '', 
                    status = 'IN_PROGRESS', 
                    status_details = '', )
            )
        else:
            return BrandSafetyRequestStatusResponse(
        )
        """

    def testBrandSafetyRequestStatusResponse(self):
        """Test BrandSafetyRequestStatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
