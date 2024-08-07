# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.snapshot_request import SnapshotRequest

class TestSnapshotRequest(unittest.TestCase):
    """SnapshotRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotRequest:
        """Test SnapshotRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotRequest`
        """
        model = SnapshotRequest()
        if include_optional:
            return SnapshotRequest(
                state_filter = 'enabled',
                tactic_filter = 'T00020,T00030'
            )
        else:
            return SnapshotRequest(
        )
        """

    def testSnapshotRequest(self):
        """Test SnapshotRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
