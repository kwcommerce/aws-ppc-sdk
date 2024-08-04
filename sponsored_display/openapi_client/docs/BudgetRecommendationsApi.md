# openapi_client.BudgetRecommendationsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sd_budget_recommendations**](BudgetRecommendationsApi.md#get_sd_budget_recommendations) | **POST** /sd/campaigns/budgetRecommendations | Returns recommended daily budget and estimated missed opportunities for campaigns


# **get_sd_budget_recommendations**
> SDBudgetRecommendationsResponse get_sd_budget_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope=amazon_advertising_api_scope, amazon_ads_account_id=amazon_ads_account_id, sd_budget_recommendations_request=sd_budget_recommendations_request)

Returns recommended daily budget and estimated missed opportunities for campaigns

Given a list of campaigns as input, this API provides the following metrics: <br> <b>1. Recommended daily budget - </b> Estimated budget needed to keep the campaign in budget for the full 24-hour period. Consider this budget to minimize your campaign's chances of running out of budget.  <br> <b>2. Percent time in budget </b> - The share of time the campaign was in budget during the past 7 days. <br> <b>3. Estimated missed impressions, clicks and sales </b> - These are the estimated additional impressions, clicks and sales the campaign might have generated had it adopted the recommended budget. These are estimates based on campaign's historical performance - and not a guarantee of actual impressions, clicks and sales. Consider using these metrics to further inform your budget allocation decisions.

### Example


```python
import openapi_client
from openapi_client.models.sd_budget_recommendations_request import SDBudgetRecommendationsRequest
from openapi_client.models.sd_budget_recommendations_response import SDBudgetRecommendationsResponse
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
    api_instance = openapi_client.BudgetRecommendationsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. (optional)
    amazon_ads_account_id = 'amazon_ads_account_id_example' # str | The identifier of an account. Account must be a global advertising account. (optional)
    sd_budget_recommendations_request = openapi_client.SDBudgetRecommendationsRequest() # SDBudgetRecommendationsRequest |  (optional)

    try:
        # Returns recommended daily budget and estimated missed opportunities for campaigns
        api_response = api_instance.get_sd_budget_recommendations(amazon_advertising_api_client_id, amazon_advertising_api_scope=amazon_advertising_api_scope, amazon_ads_account_id=amazon_ads_account_id, sd_budget_recommendations_request=sd_budget_recommendations_request)
        print("The response of BudgetRecommendationsApi->get_sd_budget_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetRecommendationsApi->get_sd_budget_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | [optional] 
 **amazon_ads_account_id** | **str**| The identifier of an account. Account must be a global advertising account. | [optional] 
 **sd_budget_recommendations_request** | [**SDBudgetRecommendationsRequest**](SDBudgetRecommendationsRequest.md)|  | [optional] 

### Return type

[**SDBudgetRecommendationsResponse**](SDBudgetRecommendationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.sdbudgetrecommendations.v3+json
 - **Accept**: application/vnd.sdbudgetrecommendations.v3+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. |  -  |
**400** | Generic bad request error. |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource. |  -  |
**415** | Unsupported Media Type. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

