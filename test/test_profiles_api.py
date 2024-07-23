# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.profiles_api import ProfilesApi


class TestProfilesApi(unittest.TestCase):
    """ProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_get_profile_by_id(self) -> None:
        """Test case for get_profile_by_id

        Gets a profile specified by identifier.
        """
        pass

    def test_list_profiles(self) -> None:
        """Test case for list_profiles

        Gets a list of profiles.
        """
        pass

    def test_update_profiles(self) -> None:
        """Test case for update_profiles

        Update the daily budget for one or more profiles.
        """
        pass


if __name__ == '__main__':
    unittest.main()
