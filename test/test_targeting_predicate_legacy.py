# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.targeting_predicate_legacy import TargetingPredicateLegacy

class TestTargetingPredicateLegacy(unittest.TestCase):
    """TargetingPredicateLegacy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TargetingPredicateLegacy:
        """Test TargetingPredicateLegacy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TargetingPredicateLegacy`
        """
        model = TargetingPredicateLegacy()
        if include_optional:
            return TargetingPredicateLegacy(
                type = 'asinSameAs',
                value = 'B0123456789',
                event_type = 'views'
            )
        else:
            return TargetingPredicateLegacy(
        )
        """

    def testTargetingPredicateLegacy(self):
        """Test TargetingPredicateLegacy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()