# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.product_ad_response import ProductAdResponse

class TestProductAdResponse(unittest.TestCase):
    """ProductAdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductAdResponse:
        """Test ProductAdResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductAdResponse`
        """
        model = ProductAdResponse()
        if include_optional:
            return ProductAdResponse(
                code = '',
                description = '',
                ad_id = 1.337
            )
        else:
            return ProductAdResponse(
        )
        """

    def testProductAdResponse(self):
        """Test ProductAdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
