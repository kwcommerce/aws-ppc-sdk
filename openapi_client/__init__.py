# coding: utf-8

# flake8: noqa

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.ad_groups_api import AdGroupsApi
from openapi_client.api.bid_recommendations_api import BidRecommendationsApi
from openapi_client.api.brand_safety_list_api import BrandSafetyListApi
from openapi_client.api.budget_recommendations_api import BudgetRecommendationsApi
from openapi_client.api.budget_rules_api import BudgetRulesApi
from openapi_client.api.budget_usage_api import BudgetUsageApi
from openapi_client.api.campaigns_api import CampaignsApi
from openapi_client.api.creatives_api import CreativesApi
from openapi_client.api.forecasts_api import ForecastsApi
from openapi_client.api.headline_recommendations_api import HeadlineRecommendationsApi
from openapi_client.api.locations_beta_api import LocationsBetaApi
from openapi_client.api.negative_targeting_api import NegativeTargetingApi
from openapi_client.api.optimization_rules_beta_api import OptimizationRulesBetaApi
from openapi_client.api.product_ads_api import ProductAdsApi
from openapi_client.api.profiles_api import ProfilesApi
from openapi_client.api.reports_api import ReportsApi
from openapi_client.api.snapshots_api import SnapshotsApi
from openapi_client.api.targeting_api import TargetingApi
from openapi_client.api.targeting_recommendations_api import TargetingRecommendationsApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.account_info import AccountInfo
from openapi_client.models.account_type import AccountType
from openapi_client.models.ad_group import AdGroup
from openapi_client.models.ad_group_response import AdGroupResponse
from openapi_client.models.ad_group_response_ex import AdGroupResponseEx
from openapi_client.models.archive_location_request import ArchiveLocationRequest
from openapi_client.models.archive_location_response import ArchiveLocationResponse
from openapi_client.models.background import Background
from openapi_client.models.background_creative_properties import BackgroundCreativeProperties
from openapi_client.models.base_ad_group import BaseAdGroup
from openapi_client.models.base_campaign import BaseCampaign
from openapi_client.models.base_location import BaseLocation
from openapi_client.models.base_negative_targeting_clause import BaseNegativeTargetingClause
from openapi_client.models.base_optimization_rule import BaseOptimizationRule
from openapi_client.models.base_product_ad import BaseProductAd
from openapi_client.models.base_targeting_clause import BaseTargetingClause
from openapi_client.models.brand_safety_deny_list_domain import BrandSafetyDenyListDomain
from openapi_client.models.brand_safety_deny_list_domain_state import BrandSafetyDenyListDomainState
from openapi_client.models.brand_safety_deny_list_domain_type import BrandSafetyDenyListDomainType
from openapi_client.models.brand_safety_deny_list_domain_update_result_status import BrandSafetyDenyListDomainUpdateResultStatus
from openapi_client.models.brand_safety_deny_list_processed_domain import BrandSafetyDenyListProcessedDomain
from openapi_client.models.brand_safety_get_response import BrandSafetyGetResponse
from openapi_client.models.brand_safety_get_response_pagination import BrandSafetyGetResponsePagination
from openapi_client.models.brand_safety_list_request_status_response import BrandSafetyListRequestStatusResponse
from openapi_client.models.brand_safety_post_request import BrandSafetyPostRequest
from openapi_client.models.brand_safety_request_result import BrandSafetyRequestResult
from openapi_client.models.brand_safety_request_results_response import BrandSafetyRequestResultsResponse
from openapi_client.models.brand_safety_request_status import BrandSafetyRequestStatus
from openapi_client.models.brand_safety_request_status_response import BrandSafetyRequestStatusResponse
from openapi_client.models.brand_safety_update_response import BrandSafetyUpdateResponse
from openapi_client.models.budget_change_type import BudgetChangeType
from openapi_client.models.budget_increase_by import BudgetIncreaseBy
from openapi_client.models.budget_rule_error import BudgetRuleError
from openapi_client.models.budget_rule_response import BudgetRuleResponse
from openapi_client.models.budget_usage_campaign import BudgetUsageCampaign
from openapi_client.models.budget_usage_campaign_batch_error import BudgetUsageCampaignBatchError
from openapi_client.models.budget_usage_campaign_request import BudgetUsageCampaignRequest
from openapi_client.models.budget_usage_campaign_response import BudgetUsageCampaignResponse
from openapi_client.models.budget_usage_error import BudgetUsageError
from openapi_client.models.call_to_action import CallToAction
from openapi_client.models.call_to_action_properties import CallToActionProperties
from openapi_client.models.call_to_action_type import CallToActionType
from openapi_client.models.campaign import Campaign
from openapi_client.models.campaign_response import CampaignResponse
from openapi_client.models.campaign_response_ex import CampaignResponseEx
from openapi_client.models.comparison_operator import ComparisonOperator
from openapi_client.models.content_targeting_predicate import ContentTargetingPredicate
from openapi_client.models.country_code import CountryCode
from openapi_client.models.create_ad_group import CreateAdGroup
from openapi_client.models.create_associated_optimization_rules_request import CreateAssociatedOptimizationRulesRequest
from openapi_client.models.create_budget_rules_response import CreateBudgetRulesResponse
from openapi_client.models.create_campaign import CreateCampaign
from openapi_client.models.create_creative import CreateCreative
from openapi_client.models.create_location import CreateLocation
from openapi_client.models.create_negative_targeting_clause import CreateNegativeTargetingClause
from openapi_client.models.create_optimization_rule import CreateOptimizationRule
from openapi_client.models.create_product_ad import CreateProductAd
from openapi_client.models.create_sd_budget_rules_request import CreateSDBudgetRulesRequest
from openapi_client.models.create_targeting_clause import CreateTargetingClause
from openapi_client.models.create_targeting_expression_inner import CreateTargetingExpressionInner
from openapi_client.models.creative import Creative
from openapi_client.models.creative_moderation import CreativeModeration
from openapi_client.models.creative_moderation_policy_violations_inner import CreativeModerationPolicyViolationsInner
from openapi_client.models.creative_moderation_policy_violations_inner_violating_brand_logo_contents_inner import CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInner
from openapi_client.models.creative_moderation_policy_violations_inner_violating_brand_logo_contents_inner_image_evidences_inner import CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInner
from openapi_client.models.creative_moderation_policy_violations_inner_violating_brand_logo_contents_inner_image_evidences_inner_violating_image_crop import CreativeModerationPolicyViolationsInnerViolatingBrandLogoContentsInnerImageEvidencesInnerViolatingImageCrop
from openapi_client.models.creative_moderation_policy_violations_inner_violating_headline_contents_inner import CreativeModerationPolicyViolationsInnerViolatingHeadlineContentsInner
from openapi_client.models.creative_moderation_policy_violations_inner_violating_headline_contents_inner_text_evidence_inner import CreativeModerationPolicyViolationsInnerViolatingHeadlineContentsInnerTextEvidenceInner
from openapi_client.models.creative_moderation_policy_violations_inner_violating_headline_contents_inner_text_evidence_inner_violating_text_position import CreativeModerationPolicyViolationsInnerViolatingHeadlineContentsInnerTextEvidenceInnerViolatingTextPosition
from openapi_client.models.creative_moderation_policy_violations_inner_violating_video_contents_inner import CreativeModerationPolicyViolationsInnerViolatingVideoContentsInner
from openapi_client.models.creative_moderation_policy_violations_inner_violating_video_contents_inner_video_evidences_inner import CreativeModerationPolicyViolationsInnerViolatingVideoContentsInnerVideoEvidencesInner
from openapi_client.models.creative_moderation_policy_violations_inner_violating_video_contents_inner_video_evidences_inner_violating_video_position import CreativeModerationPolicyViolationsInnerViolatingVideoContentsInnerVideoEvidencesInnerViolatingVideoPosition
from openapi_client.models.creative_preview_configuration import CreativePreviewConfiguration
from openapi_client.models.creative_preview_configuration_products_inner import CreativePreviewConfigurationProductsInner
from openapi_client.models.creative_preview_configuration_size import CreativePreviewConfigurationSize
from openapi_client.models.creative_preview_request import CreativePreviewRequest
from openapi_client.models.creative_preview_response import CreativePreviewResponse
from openapi_client.models.creative_properties import CreativeProperties
from openapi_client.models.creative_response import CreativeResponse
from openapi_client.models.creative_type import CreativeType
from openapi_client.models.creative_type_in_creative_request import CreativeTypeInCreativeRequest
from openapi_client.models.creative_type_in_creative_response import CreativeTypeInCreativeResponse
from openapi_client.models.creative_update import CreativeUpdate
from openapi_client.models.curve import Curve
from openapi_client.models.curve_point import CurvePoint
from openapi_client.models.curve_point_fixed_value import CurvePointFixedValue
from openapi_client.models.curve_point_ranged_value import CurvePointRangedValue
from openapi_client.models.custom_image_creative_properties import CustomImageCreativeProperties
from openapi_client.models.date_range_type_rule_duration import DateRangeTypeRuleDuration
from openapi_client.models.day_of_week import DayOfWeek
from openapi_client.models.error import Error
from openapi_client.models.event_type_rule_duration import EventTypeRuleDuration
from openapi_client.models.forecast import Forecast
from openapi_client.models.forecast_range import ForecastRange
from openapi_client.models.forecast_range_double import ForecastRangeDouble
from openapi_client.models.forecast_status import ForecastStatus
from openapi_client.models.get_sd_budget_rule_response import GetSDBudgetRuleResponse
from openapi_client.models.get_sd_budget_rules_for_advertiser_response import GetSDBudgetRulesForAdvertiserResponse
from openapi_client.models.headline_creative_properties import HeadlineCreativeProperties
from openapi_client.models.image import Image
from openapi_client.models.image_cropping_coordinates import ImageCroppingCoordinates
from openapi_client.models.landing_page_type import LandingPageType
from openapi_client.models.lead_gen_creative_properties import LeadGenCreativeProperties
from openapi_client.models.locale import Locale
from openapi_client.models.location import Location
from openapi_client.models.location_expression import LocationExpression
from openapi_client.models.location_expression_id_filter import LocationExpressionIdFilter
from openapi_client.models.location_predicate import LocationPredicate
from openapi_client.models.logo_creative_properties import LogoCreativeProperties
from openapi_client.models.negative_targeting_clause import NegativeTargetingClause
from openapi_client.models.negative_targeting_clause_ex import NegativeTargetingClauseEx
from openapi_client.models.negative_targeting_clause_ex_expression_inner import NegativeTargetingClauseExExpressionInner
from openapi_client.models.negative_targeting_expression import NegativeTargetingExpression
from openapi_client.models.optimization_rule import OptimizationRule
from openapi_client.models.optimization_rule_association_response import OptimizationRuleAssociationResponse
from openapi_client.models.optimization_rule_response import OptimizationRuleResponse
from openapi_client.models.performance_measure_condition import PerformanceMeasureCondition
from openapi_client.models.performance_metric import PerformanceMetric
from openapi_client.models.preview_creative_model import PreviewCreativeModel
from openapi_client.models.product_ad import ProductAd
from openapi_client.models.product_ad_response import ProductAdResponse
from openapi_client.models.product_ad_response_ex import ProductAdResponseEx
from openapi_client.models.profile import Profile
from openapi_client.models.profile_response import ProfileResponse
from openapi_client.models.recommended_headline import RecommendedHeadline
from openapi_client.models.recurrence import Recurrence
from openapi_client.models.recurrence_type import RecurrenceType
from openapi_client.models.report_request import ReportRequest
from openapi_client.models.report_response import ReportResponse
from openapi_client.models.resolved_location_expression import ResolvedLocationExpression
from openapi_client.models.rule_based_budget import RuleBasedBudget
from openapi_client.models.rule_condition import RuleCondition
from openapi_client.models.rule_duration import RuleDuration
from openapi_client.models.sd_audience_category import SDAudienceCategory
from openapi_client.models.sd_audience_category_recommendations import SDAudienceCategoryRecommendations
from openapi_client.models.sd_audience_recommendation import SDAudienceRecommendation
from openapi_client.models.sd_audience_recommendations import SDAudienceRecommendations
from openapi_client.models.sd_bid_optimization_v32 import SDBidOptimizationV32
from openapi_client.models.sd_bid_recommendation_v31 import SDBidRecommendationV31
from openapi_client.models.sd_budget_recommendation import SDBudgetRecommendation
from openapi_client.models.sd_budget_recommendation_error import SDBudgetRecommendationError
from openapi_client.models.sd_budget_recommendations_request import SDBudgetRecommendationsRequest
from openapi_client.models.sd_budget_recommendations_response import SDBudgetRecommendationsResponse
from openapi_client.models.sd_budget_rule import SDBudgetRule
from openapi_client.models.sd_budget_rule_details import SDBudgetRuleDetails
from openapi_client.models.sd_category_recommendation import SDCategoryRecommendation
from openapi_client.models.sd_category_recommendation_targetable_asin_count_range import SDCategoryRecommendationTargetableAsinCountRange
from openapi_client.models.sd_category_recommendation_v33 import SDCategoryRecommendationV33
from openapi_client.models.sd_category_recommendation_v33_targetable_asin_count_range import SDCategoryRecommendationV33TargetableAsinCountRange
from openapi_client.models.sd_category_recommendations import SDCategoryRecommendations
from openapi_client.models.sd_category_recommendations_v33 import SDCategoryRecommendationsV33
from openapi_client.models.sd_content_category_recommendations import SDContentCategoryRecommendations
from openapi_client.models.sd_content_targeting_predicate_v31 import SDContentTargetingPredicateV31
from openapi_client.models.sd_cost_type_v31 import SDCostTypeV31
from openapi_client.models.sd_creative_type import SDCreativeType
from openapi_client.models.sd_error_response import SDErrorResponse
from openapi_client.models.sd_forecast_error_response import SDForecastErrorResponse
from openapi_client.models.sd_forecast_request import SDForecastRequest
from openapi_client.models.sd_forecast_request_targeting_clause import SDForecastRequestTargetingClause
from openapi_client.models.sd_forecast_response import SDForecastResponse
from openapi_client.models.sd_goal_product import SDGoalProduct
from openapi_client.models.sd_headline_recommendation_access_denied_exception import SDHeadlineRecommendationAccessDeniedException
from openapi_client.models.sd_headline_recommendation_identifier_notfound_exception import SDHeadlineRecommendationIdentifierNotfoundException
from openapi_client.models.sd_headline_recommendation_internal_server_exception import SDHeadlineRecommendationInternalServerException
from openapi_client.models.sd_headline_recommendation_mars_throttling_exception import SDHeadlineRecommendationMarsThrottlingException
from openapi_client.models.sd_headline_recommendation_request import SDHeadlineRecommendationRequest
from openapi_client.models.sd_headline_recommendation_response import SDHeadlineRecommendationResponse
from openapi_client.models.sd_headline_recommendation_schema_validation_exception import SDHeadlineRecommendationSchemaValidationException
from openapi_client.models.sd_landing_page_type import SDLandingPageType
from openapi_client.models.sd_product_recommendation import SDProductRecommendation
from openapi_client.models.sd_product_recommendation_v32 import SDProductRecommendationV32
from openapi_client.models.sd_product_recommendations_v31 import SDProductRecommendationsV31
from openapi_client.models.sd_product_recommendations_v32 import SDProductRecommendationsV32
from openapi_client.models.sd_product_targeting_recommendations_success import SDProductTargetingRecommendationsSuccess
from openapi_client.models.sd_product_targeting_recommendations_success_v34 import SDProductTargetingRecommendationsSuccessV34
from openapi_client.models.sd_product_targeting_theme import SDProductTargetingTheme
from openapi_client.models.sd_product_targeting_theme_expression import SDProductTargetingThemeExpression
from openapi_client.models.sd_recommendation_type import SDRecommendationType
from openapi_client.models.sd_recommendation_type_v31 import SDRecommendationTypeV31
from openapi_client.models.sd_recommendation_type_v32 import SDRecommendationTypeV32
from openapi_client.models.sd_recommendation_type_v33 import SDRecommendationTypeV33
from openapi_client.models.sd_rule_type import SDRuleType
from openapi_client.models.sd_seven_days_missed_opportunities import SDSevenDaysMissedOpportunities
from openapi_client.models.sd_tactic import SDTactic
from openapi_client.models.sd_tactic_v31 import SDTacticV31
from openapi_client.models.sd_target_expression_v31 import SDTargetExpressionV31
from openapi_client.models.sd_target_expression_v32 import SDTargetExpressionV32
from openapi_client.models.sd_targeting_bid_recommendations_request_v31 import SDTargetingBidRecommendationsRequestV31
from openapi_client.models.sd_targeting_bid_recommendations_request_v32 import SDTargetingBidRecommendationsRequestV32
from openapi_client.models.sd_targeting_bid_recommendations_request_v33 import SDTargetingBidRecommendationsRequestV33
from openapi_client.models.sd_targeting_bid_recommendations_request_v33_targeting_clauses_inner import SDTargetingBidRecommendationsRequestV33TargetingClausesInner
from openapi_client.models.sd_targeting_bid_recommendations_request_v34 import SDTargetingBidRecommendationsRequestV34
from openapi_client.models.sd_targeting_bid_recommendations_request_v34_targeting_clauses_inner import SDTargetingBidRecommendationsRequestV34TargetingClausesInner
from openapi_client.models.sd_targeting_bid_recommendations_response_item_failure_v31 import SDTargetingBidRecommendationsResponseItemFailureV31
from openapi_client.models.sd_targeting_bid_recommendations_response_item_success_v31 import SDTargetingBidRecommendationsResponseItemSuccessV31
from openapi_client.models.sd_targeting_bid_recommendations_response_v31 import SDTargetingBidRecommendationsResponseV31
from openapi_client.models.sd_targeting_bid_recommendations_response_v32 import SDTargetingBidRecommendationsResponseV32
from openapi_client.models.sd_targeting_bid_recommendations_response_v32_bid_recommendations_inner import SDTargetingBidRecommendationsResponseV32BidRecommendationsInner
from openapi_client.models.sd_targeting_clause_v31 import SDTargetingClauseV31
from openapi_client.models.sd_targeting_clause_v32 import SDTargetingClauseV32
from openapi_client.models.sd_targeting_predicate_base_v31 import SDTargetingPredicateBaseV31
from openapi_client.models.sd_targeting_predicate_nested_v31 import SDTargetingPredicateNestedV31
from openapi_client.models.sd_targeting_predicate_v31 import SDTargetingPredicateV31
from openapi_client.models.sd_targeting_recommendations import SDTargetingRecommendations
from openapi_client.models.sd_targeting_recommendations_locale import SDTargetingRecommendationsLocale
from openapi_client.models.sd_targeting_recommendations_products_v31_inner import SDTargetingRecommendationsProductsV31Inner
from openapi_client.models.sd_targeting_recommendations_request import SDTargetingRecommendationsRequest
from openapi_client.models.sd_targeting_recommendations_request_v31 import SDTargetingRecommendationsRequestV31
from openapi_client.models.sd_targeting_recommendations_request_v32 import SDTargetingRecommendationsRequestV32
from openapi_client.models.sd_targeting_recommendations_request_v33 import SDTargetingRecommendationsRequestV33
from openapi_client.models.sd_targeting_recommendations_request_v34 import SDTargetingRecommendationsRequestV34
from openapi_client.models.sd_targeting_recommendations_request_v35 import SDTargetingRecommendationsRequestV35
from openapi_client.models.sd_targeting_recommendations_response import SDTargetingRecommendationsResponse
from openapi_client.models.sd_targeting_recommendations_response_v31 import SDTargetingRecommendationsResponseV31
from openapi_client.models.sd_targeting_recommendations_response_v32 import SDTargetingRecommendationsResponseV32
from openapi_client.models.sd_targeting_recommendations_response_v33 import SDTargetingRecommendationsResponseV33
from openapi_client.models.sd_targeting_recommendations_response_v34 import SDTargetingRecommendationsResponseV34
from openapi_client.models.sd_targeting_recommendations_response_v35 import SDTargetingRecommendationsResponseV35
from openapi_client.models.sd_targeting_recommendations_themes import SDTargetingRecommendationsThemes
from openapi_client.models.sd_targeting_recommendations_v31 import SDTargetingRecommendationsV31
from openapi_client.models.sd_targeting_recommendations_v32 import SDTargetingRecommendationsV32
from openapi_client.models.sd_targeting_recommendations_v33 import SDTargetingRecommendationsV33
from openapi_client.models.sd_targeting_recommendations_v34 import SDTargetingRecommendationsV34
from openapi_client.models.sd_targeting_recommendations_v35 import SDTargetingRecommendationsV35
from openapi_client.models.sd_theme_recommendations import SDThemeRecommendations
from openapi_client.models.sd_theme_recommendations_themes import SDThemeRecommendationsThemes
from openapi_client.models.sd_theme_recommendations_themes_products_inner import SDThemeRecommendationsThemesProductsInner
from openapi_client.models.sd_theme_recommendations_v34 import SDThemeRecommendationsV34
from openapi_client.models.sd_theme_recommendations_v34_themes import SDThemeRecommendationsV34Themes
from openapi_client.models.sd_theme_recommendations_v34_themes_products_inner import SDThemeRecommendationsV34ThemesProductsInner
from openapi_client.models.segment import Segment
from openapi_client.models.single_optimization_rule_association_response import SingleOptimizationRuleAssociationResponse
from openapi_client.models.snapshot_request import SnapshotRequest
from openapi_client.models.snapshot_response import SnapshotResponse
from openapi_client.models.state import State
from openapi_client.models.tactic import Tactic
from openapi_client.models.tactic_filter import TacticFilter
from openapi_client.models.tactic_report import TacticReport
from openapi_client.models.target_response import TargetResponse
from openapi_client.models.targeting_clause import TargetingClause
from openapi_client.models.targeting_clause_ex import TargetingClauseEx
from openapi_client.models.targeting_expression_inner import TargetingExpressionInner
from openapi_client.models.targeting_predicate import TargetingPredicate
from openapi_client.models.targeting_predicate_base import TargetingPredicateBase
from openapi_client.models.targeting_predicate_legacy import TargetingPredicateLegacy
from openapi_client.models.targeting_predicate_nested import TargetingPredicateNested
from openapi_client.models.time_of_day import TimeOfDay
from openapi_client.models.update_ad_group import UpdateAdGroup
from openapi_client.models.update_budget_rules_response import UpdateBudgetRulesResponse
from openapi_client.models.update_campaign import UpdateCampaign
from openapi_client.models.update_negative_targeting_clause import UpdateNegativeTargetingClause
from openapi_client.models.update_optimization_rule import UpdateOptimizationRule
from openapi_client.models.update_product_ad import UpdateProductAd
from openapi_client.models.update_sd_budget_rules_request import UpdateSDBudgetRulesRequest
from openapi_client.models.update_targeting_clause import UpdateTargetingClause
from openapi_client.models.video import Video
from openapi_client.models.video_creative_properties import VideoCreativeProperties
