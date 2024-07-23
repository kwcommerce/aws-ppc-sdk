# openapi_client.HeadlineRecommendationsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_headline_recommendations_for_sd**](HeadlineRecommendationsApi.md#get_headline_recommendations_for_sd) | **POST** /sd/recommendations/creative/headline | 


# **get_headline_recommendations_for_sd**
> SDHeadlineRecommendationResponse get_headline_recommendations_for_sd(amazon_advertising_api_client_id, amazon_advertising_api_scope, sd_headline_recommendation_request)



You can use this Sponsored Display API to retrieve creative headline recommendations from an array of ASINs.  **Requires one of these permissions**: [\"advertiser_campaign_view\"]

### Example


```python
import openapi_client
from openapi_client.models.sd_headline_recommendation_request import SDHeadlineRecommendationRequest
from openapi_client.models.sd_headline_recommendation_response import SDHeadlineRecommendationResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.HeadlineRecommendationsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    sd_headline_recommendation_request = openapi_client.SDHeadlineRecommendationRequest() # SDHeadlineRecommendationRequest | Request body for SD headline recommendations API.

    try:
        api_response = api_instance.get_headline_recommendations_for_sd(amazon_advertising_api_client_id, amazon_advertising_api_scope, sd_headline_recommendation_request)
        print("The response of HeadlineRecommendationsApi->get_headline_recommendations_for_sd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeadlineRecommendationsApi->get_headline_recommendations_for_sd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **sd_headline_recommendation_request** | [**SDHeadlineRecommendationRequest**](SDHeadlineRecommendationRequest.md)| Request body for SD headline recommendations API. | 

### Return type

[**SDHeadlineRecommendationResponse**](SDHeadlineRecommendationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.sdheadlinerecommendationrequest.v4.0+json
 - **Accept**: application/vnd.sdheadlinerecommendationresponse.v4.0+json, application/vnd.sdheadlinerecommendationschemavalidationexception.v4.0+json, application/vnd.sdheadlinerecommendationaccessdeniedexception.v4.0+json, application/vnd.sdheadlinerecommendationidentifiernotfoundexception.v4.0+json, application/vnd.sdheadlinerecommendationthrottlingexception.v4.0+json, application/vnd.sdheadlinerecommendationinternalserverexception.v4.0+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | SchemaValidationException 400 response. |  -  |
**403** | AccessDeniedException 403 response. |  -  |
**404** | IdentifierNotFoundException 404 response. |  -  |
**429** | ThrottlingException 429 response. |  -  |
**500** | InternalServerException 500 response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

