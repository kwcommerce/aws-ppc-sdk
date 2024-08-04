# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.creative_update import CreativeUpdate

class TestCreativeUpdate(unittest.TestCase):
    """CreativeUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreativeUpdate:
        """Test CreativeUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreativeUpdate`
        """
        model = CreativeUpdate()
        if include_optional:
            return CreativeUpdate(
                creative_id = 1.337,
                creative_type = 'IMAGE',
                properties = None
            )
        else:
            return CreativeUpdate(
                creative_id = 1.337,
                properties = None,
        )
        """

    def testCreativeUpdate(self):
        """Test CreativeUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()