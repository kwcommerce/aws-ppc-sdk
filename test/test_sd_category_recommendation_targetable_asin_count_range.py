# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sd_category_recommendation_targetable_asin_count_range import SDCategoryRecommendationTargetableAsinCountRange

class TestSDCategoryRecommendationTargetableAsinCountRange(unittest.TestCase):
    """SDCategoryRecommendationTargetableAsinCountRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SDCategoryRecommendationTargetableAsinCountRange:
        """Test SDCategoryRecommendationTargetableAsinCountRange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SDCategoryRecommendationTargetableAsinCountRange`
        """
        model = SDCategoryRecommendationTargetableAsinCountRange()
        if include_optional:
            return SDCategoryRecommendationTargetableAsinCountRange(
                range_lower = 56,
                range_upper = 56
            )
        else:
            return SDCategoryRecommendationTargetableAsinCountRange(
        )
        """

    def testSDCategoryRecommendationTargetableAsinCountRange(self):
        """Test SDCategoryRecommendationTargetableAsinCountRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()