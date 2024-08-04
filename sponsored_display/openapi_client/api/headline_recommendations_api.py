# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from openapi_client.models.sd_headline_recommendation_request import SDHeadlineRecommendationRequest
from openapi_client.models.sd_headline_recommendation_response import SDHeadlineRecommendationResponse

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class HeadlineRecommendationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_headline_recommendations_for_sd(
        self,
        amazon_advertising_api_client_id: Annotated[StrictStr, Field(description="The identifier of a client associated with a \"Login with Amazon\" account.")],
        amazon_advertising_api_scope: Annotated[StrictStr, Field(description="The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.")],
        sd_headline_recommendation_request: Annotated[SDHeadlineRecommendationRequest, Field(description="Request body for SD headline recommendations API.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SDHeadlineRecommendationResponse:
        """get_headline_recommendations_for_sd

        You can use this Sponsored Display API to retrieve creative headline recommendations from an array of ASINs.  **Requires one of these permissions**: [\"advertiser_campaign_view\"]

        :param amazon_advertising_api_client_id: The identifier of a client associated with a \"Login with Amazon\" account. (required)
        :type amazon_advertising_api_client_id: str
        :param amazon_advertising_api_scope: The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. (required)
        :type amazon_advertising_api_scope: str
        :param sd_headline_recommendation_request: Request body for SD headline recommendations API. (required)
        :type sd_headline_recommendation_request: SDHeadlineRecommendationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_headline_recommendations_for_sd_serialize(
            amazon_advertising_api_client_id=amazon_advertising_api_client_id,
            amazon_advertising_api_scope=amazon_advertising_api_scope,
            sd_headline_recommendation_request=sd_headline_recommendation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SDHeadlineRecommendationResponse",
            '400': "SDHeadlineRecommendationSchemaValidationException",
            '403': "SDHeadlineRecommendationAccessDeniedException",
            '404': "SDHeadlineRecommendationIdentifierNotfoundException",
            '429': "SDHeadlineRecommendationMarsThrottlingException",
            '500': "SDHeadlineRecommendationInternalServerException",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_headline_recommendations_for_sd_with_http_info(
        self,
        amazon_advertising_api_client_id: Annotated[StrictStr, Field(description="The identifier of a client associated with a \"Login with Amazon\" account.")],
        amazon_advertising_api_scope: Annotated[StrictStr, Field(description="The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.")],
        sd_headline_recommendation_request: Annotated[SDHeadlineRecommendationRequest, Field(description="Request body for SD headline recommendations API.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SDHeadlineRecommendationResponse]:
        """get_headline_recommendations_for_sd

        You can use this Sponsored Display API to retrieve creative headline recommendations from an array of ASINs.  **Requires one of these permissions**: [\"advertiser_campaign_view\"]

        :param amazon_advertising_api_client_id: The identifier of a client associated with a \"Login with Amazon\" account. (required)
        :type amazon_advertising_api_client_id: str
        :param amazon_advertising_api_scope: The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. (required)
        :type amazon_advertising_api_scope: str
        :param sd_headline_recommendation_request: Request body for SD headline recommendations API. (required)
        :type sd_headline_recommendation_request: SDHeadlineRecommendationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_headline_recommendations_for_sd_serialize(
            amazon_advertising_api_client_id=amazon_advertising_api_client_id,
            amazon_advertising_api_scope=amazon_advertising_api_scope,
            sd_headline_recommendation_request=sd_headline_recommendation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SDHeadlineRecommendationResponse",
            '400': "SDHeadlineRecommendationSchemaValidationException",
            '403': "SDHeadlineRecommendationAccessDeniedException",
            '404': "SDHeadlineRecommendationIdentifierNotfoundException",
            '429': "SDHeadlineRecommendationMarsThrottlingException",
            '500': "SDHeadlineRecommendationInternalServerException",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_headline_recommendations_for_sd_without_preload_content(
        self,
        amazon_advertising_api_client_id: Annotated[StrictStr, Field(description="The identifier of a client associated with a \"Login with Amazon\" account.")],
        amazon_advertising_api_scope: Annotated[StrictStr, Field(description="The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.")],
        sd_headline_recommendation_request: Annotated[SDHeadlineRecommendationRequest, Field(description="Request body for SD headline recommendations API.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """get_headline_recommendations_for_sd

        You can use this Sponsored Display API to retrieve creative headline recommendations from an array of ASINs.  **Requires one of these permissions**: [\"advertiser_campaign_view\"]

        :param amazon_advertising_api_client_id: The identifier of a client associated with a \"Login with Amazon\" account. (required)
        :type amazon_advertising_api_client_id: str
        :param amazon_advertising_api_scope: The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. (required)
        :type amazon_advertising_api_scope: str
        :param sd_headline_recommendation_request: Request body for SD headline recommendations API. (required)
        :type sd_headline_recommendation_request: SDHeadlineRecommendationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_headline_recommendations_for_sd_serialize(
            amazon_advertising_api_client_id=amazon_advertising_api_client_id,
            amazon_advertising_api_scope=amazon_advertising_api_scope,
            sd_headline_recommendation_request=sd_headline_recommendation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SDHeadlineRecommendationResponse",
            '400': "SDHeadlineRecommendationSchemaValidationException",
            '403': "SDHeadlineRecommendationAccessDeniedException",
            '404': "SDHeadlineRecommendationIdentifierNotfoundException",
            '429': "SDHeadlineRecommendationMarsThrottlingException",
            '500': "SDHeadlineRecommendationInternalServerException",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_headline_recommendations_for_sd_serialize(
        self,
        amazon_advertising_api_client_id,
        amazon_advertising_api_scope,
        sd_headline_recommendation_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if amazon_advertising_api_client_id is not None:
            _header_params['Amazon-Advertising-API-ClientId'] = amazon_advertising_api_client_id
        if amazon_advertising_api_scope is not None:
            _header_params['Amazon-Advertising-API-Scope'] = amazon_advertising_api_scope
        # process the form parameters
        # process the body parameter
        if sd_headline_recommendation_request is not None:
            _body_params = sd_headline_recommendation_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.sdheadlinerecommendationresponse.v4.0+json', 
                    'application/vnd.sdheadlinerecommendationschemavalidationexception.v4.0+json', 
                    'application/vnd.sdheadlinerecommendationaccessdeniedexception.v4.0+json', 
                    'application/vnd.sdheadlinerecommendationidentifiernotfoundexception.v4.0+json', 
                    'application/vnd.sdheadlinerecommendationthrottlingexception.v4.0+json', 
                    'application/vnd.sdheadlinerecommendationinternalserverexception.v4.0+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.sdheadlinerecommendationrequest.v4.0+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/sd/recommendations/creative/headline',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

