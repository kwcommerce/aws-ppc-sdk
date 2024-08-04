# openapi_client.BidRecommendationsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_target_bid_recommendations**](BidRecommendationsApi.md#get_target_bid_recommendations) | **POST** /sd/targets/bid/recommendations | Returns a set of bid recommendations for targeting clauses


# **get_target_bid_recommendations**
> SDTargetingBidRecommendationsResponseV32 get_target_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, sd_targeting_bid_recommendations_request_v34=sd_targeting_bid_recommendations_request_v34)

Returns a set of bid recommendations for targeting clauses

Provides a list of bid recommendations based on the list of input advertised ASINs and targeting clauses in the same format as the targeting API. For each targeting clause in the request a corresponding bid recommendation will be returned in the response. Currently the API will accept up to 100 targeting clauses. Note - these recommendations are only available when productAds have ASIN or SKU fields. This API provides a corresponding bid recommendation for each targeting clause in a request. Currently the API will accept up to 100 targeting clauses.  For API v3.1, the API provides a list of bid recommendations based on the list of input advertised ASINs and targeting clauses in the same format as the targeting API. Note - these recommendations are only available when productAds have ASIN or SKU fields.  For API v3.2, the API accepts optimizationType and costType and returns bid recommendations accordingly.  For API v3.3, the API accepts creativeType and returns bid recommendations accordingly.  [PREVIEW ONLY] For API v3.4, the API supports entertainment targeting bid recommendations which is currently limited to US marketplace.  The recommended bids are derived from the last 7 days of winning auction bids for the related targeting clause.   Receive bid recommendations using the following: Contextual targeting clause|Description| |-----------|----| |asinSameAs=B0123456789|Receive a bid recommendation for this target product |asinCategorySameAs=12345|Receive a bid recommendation for this target category |similarProduct|Receive a bid recommendation for targets that are similar to the advertised asins.   Audience targeting clause|Description| |-----------|----| |views(asinCategorySameAs=12345 lookback=30)|Receive a bid recommendation for a target audience that has viewed products in the given category |views(similarProduct lookback=30)|Receive a bid recommendation for a target audience that has viewed similar products to the advertised asins |views(exactProduct lookback=30)|Receive a bid recommendation for a target audience that has viewed the advertised asins |purchases(asinCategorySameAs=12345 lookback=30)|Receive a bid recommendation for a target audience that has purchased products in the given category |purchases(exactProduct lookback=30)|Receive a bid recommendation for a target audience that has purchased the advertised asins |purchases(relatedProduct lookback=30)|Receive a bid recommendation for a target audience that has purchased related products to the advertised asins |audience(audienceSameAs=12345)|Receive a bid recommendation for the given target audience  | Content targeting clause | Description | |------------------|-------------| | [PREVIEW ONLY] contentCategorySameAs=amzn1.iab-content.325 | Receive a bid recommendation for the given content target |   #### Notes: - Refinements are currently not supported and if included will not impact the bid recommendation for the target.   #### Advertised ASIN Notes: - For asinSameAs targets the advertised asins will not impact the bid recommendation - For asinCategorySameAs targets the advertised asins are optional, but including them will provide a more refined bid recommendation - For similarProduct, exactProduct, and relatedProduct targets the advertised asins are required

### Example


```python
import openapi_client
from openapi_client.models.sd_targeting_bid_recommendations_request_v34 import SDTargetingBidRecommendationsRequestV34
from openapi_client.models.sd_targeting_bid_recommendations_response_v32 import SDTargetingBidRecommendationsResponseV32
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
    api_instance = openapi_client.BidRecommendationsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    sd_targeting_bid_recommendations_request_v34 = openapi_client.SDTargetingBidRecommendationsRequestV34() # SDTargetingBidRecommendationsRequestV34 |  (optional)

    try:
        # Returns a set of bid recommendations for targeting clauses
        api_response = api_instance.get_target_bid_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope, sd_targeting_bid_recommendations_request_v34=sd_targeting_bid_recommendations_request_v34)
        print("The response of BidRecommendationsApi->get_target_bid_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BidRecommendationsApi->get_target_bid_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **sd_targeting_bid_recommendations_request_v34** | [**SDTargetingBidRecommendationsRequestV34**](SDTargetingBidRecommendationsRequestV34.md)|  | [optional] 

### Return type

[**SDTargetingBidRecommendationsResponseV32**](SDTargetingBidRecommendationsResponseV32.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.sdtargetingrecommendations.v3.4+json, application/vnd.sdtargetingrecommendations.v3.3+json, application/vnd.sdtargetingrecommendations.v3.2+json, application/vnd.sdtargetingrecommendations.v3.1+json
 - **Accept**: application/vnd.sdtargetingrecommendations.v3.3+json, application/vnd.sdtargetingrecommendations.v3.2+json, application/vnd.sdtargetingrecommendations.v3.1+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | multi-status |  -  |
**400** | Generic bad request error. |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

