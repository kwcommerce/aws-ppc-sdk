# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_content_targeting_predicate_v31 import SDContentTargetingPredicateV31

class TestSDContentTargetingPredicateV31(unittest.TestCase):
    """SDContentTargetingPredicateV31 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDContentTargetingPredicateV31:
        """Test SDContentTargetingPredicateV31
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDContentTargetingPredicateV31`
        """
        model = SDContentTargetingPredicateV31()
        if include_optional:
            return SDContentTargetingPredicateV31(
                type = 'contentCategorySameAs',
                value = 'amzn1.iab-content.325'
            )
        else:
            return SDContentTargetingPredicateV31(
                type = 'contentCategorySameAs',
                value = 'amzn1.iab-content.325',
        )
        """

    def testSDContentTargetingPredicateV31(self):
        """Test SDContentTargetingPredicateV31"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
