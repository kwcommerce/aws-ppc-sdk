# openapi_client.TargetingRecommendationsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_target_recommendations**](TargetingRecommendationsApi.md#get_target_recommendations) | **POST** /sd/targets/recommendations | Returns a set of recommended products and categories to target


# **get_target_recommendations**
> SDTargetingRecommendationsResponseV35 get_target_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, locale=locale, sd_targeting_recommendations_request_v35=sd_targeting_recommendations_request_v35)

Returns a set of recommended products and categories to target

This API provides product, category and standard audience recommendations to target based on the list of input ASINs. Allow 1 week for our systems to process data for any new ASINs listed on Amazon before using this service. Note -  recommendations are only available for productAds with SKU or ASIN.  For API v3.0, the API returns up to 100 recommendations for contextual targeting.  For API v3.1, the API returns up to 100 recommendations for both product and category targeting.  For API v3.2, the API introduces contextual targeting themes in the request and returns product recommendations based on different targeting themes.  For API v3.3, the API introduces standard audience recommendations and translated category recommendations based on locale.  For API v3.4, the API includes the theme expression used in contextual targeting recommendations in the response.  [PREVIEW ONLY] For API v3.5, the API supports recommendations for landing pages for audience targeting with tactic T00030. The API also supports entertainment targeting recommendations. Both features are currently limited to US marketplace.  The currently available tactic identifiers are:  |Tactic Name|Type|Description| |-----------|----|-----------| |T00020&nbsp;|Contextual Targeting|Products: Choose individual products to show your ads in placements related to those products.| |T00030&nbsp;|Audiences or Contextual Targeting| Select individual products, categories, refined categories, or audiences to show your ads.|

### Example


```python
import openapi_client
from openapi_client.models.sd_targeting_recommendations_locale import SDTargetingRecommendationsLocale
from openapi_client.models.sd_targeting_recommendations_request_v35 import SDTargetingRecommendationsRequestV35
from openapi_client.models.sd_targeting_recommendations_response_v35 import SDTargetingRecommendationsResponseV35
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
    api_instance = openapi_client.TargetingRecommendationsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    locale = openapi_client.SDTargetingRecommendationsLocale() # SDTargetingRecommendationsLocale | The requested locale from query parameter to return translated category recommendations. (optional)
    sd_targeting_recommendations_request_v35 = openapi_client.SDTargetingRecommendationsRequestV35() # SDTargetingRecommendationsRequestV35 |  (optional)

    try:
        # Returns a set of recommended products and categories to target
        api_response = api_instance.get_target_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, locale=locale, sd_targeting_recommendations_request_v35=sd_targeting_recommendations_request_v35)
        print("The response of TargetingRecommendationsApi->get_target_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetingRecommendationsApi->get_target_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **locale** | [**SDTargetingRecommendationsLocale**](.md)| The requested locale from query parameter to return translated category recommendations. | [optional] 
 **sd_targeting_recommendations_request_v35** | [**SDTargetingRecommendationsRequestV35**](SDTargetingRecommendationsRequestV35.md)|  | [optional] 

### Return type

[**SDTargetingRecommendationsResponseV35**](SDTargetingRecommendationsResponseV35.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.sdtargetingrecommendations.v3.5+json, application/vnd.sdtargetingrecommendations.v3.4+json, application/vnd.sdtargetingrecommendations.v3.3+json, application/vnd.sdtargetingrecommendations.v3.2+json, application/vnd.sdtargetingrecommendations.v3.1+json, application/vnd.sdtargetingrecommendations.v3.0+json
 - **Accept**: application/vnd.sdtargetingrecommendations.v3.5+json, application/vnd.sdtargetingrecommendations.v3.4+json, application/vnd.sdtargetingrecommendations.v3.3+json, application/vnd.sdtargetingrecommendations.v3.2+json, application/vnd.sdtargetingrecommendations.v3.1+json, application/vnd.sdtargetingrecommendations.v3.0+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Generic bad request error. |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

