# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.snapshots_api import SnapshotsApi


class TestSnapshotsApi(unittest.TestCase):
    """SnapshotsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SnapshotsApi()

    def tearDown(self) -> None:
        pass

    def test_create_snapshot(self) -> None:
        """Test case for create_snapshot

        Request a file-based snapshot of all entities of the specified type in the account satisfying the filtering criteria
        """
        pass

    def test_download_snapshot(self) -> None:
        """Test case for download_snapshot

        Download previously requested snapshot
        """
        pass

    def test_get_snapshot(self) -> None:
        """Test case for get_snapshot

        Retrieve status, metadata, and location of previously requested snapshot
        """
        pass


if __name__ == '__main__':
    unittest.main()
