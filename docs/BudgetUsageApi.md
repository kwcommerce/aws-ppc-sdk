# openapi_client.BudgetUsageApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sd_campaigns_budget_usage**](BudgetUsageApi.md#sd_campaigns_budget_usage) | **POST** /sd/campaigns/budget/usage | Budget usage API for SD campaigns


# **sd_campaigns_budget_usage**
> BudgetUsageCampaignResponse sd_campaigns_budget_usage(amazon_advertising_api_client_id, amazon_advertising_api_scope, budget_usage_campaign_request=budget_usage_campaign_request)

Budget usage API for SD campaigns

**Requires one of these permissions**: [\"advertiser_campaign_edit\",\"advertiser_campaign_view\"]

### Example


```python
import openapi_client
from openapi_client.models.budget_usage_campaign_request import BudgetUsageCampaignRequest
from openapi_client.models.budget_usage_campaign_response import BudgetUsageCampaignResponse
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
    api_instance = openapi_client.BudgetUsageApi(api_client)
    amazon_advertising_api_client_id = None # object | The identifier of a client associated with a \"Login with Amazon\" account. This is a required header for advertisers and integrators using the Advertising API.
    amazon_advertising_api_scope = None # object | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API.
    budget_usage_campaign_request = openapi_client.BudgetUsageCampaignRequest() # BudgetUsageCampaignRequest |  (optional)

    try:
        # Budget usage API for SD campaigns
        api_response = api_instance.sd_campaigns_budget_usage(amazon_advertising_api_client_id, amazon_advertising_api_scope, budget_usage_campaign_request=budget_usage_campaign_request)
        print("The response of BudgetUsageApi->sd_campaigns_budget_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetUsageApi->sd_campaigns_budget_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | [**object**](.md)| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. This is a required header for advertisers and integrators using the Advertising API. | 
 **amazon_advertising_api_scope** | [**object**](.md)| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API. | 
 **budget_usage_campaign_request** | [**BudgetUsageCampaignRequest**](BudgetUsageCampaignRequest.md)|  | [optional] 

### Return type

[**BudgetUsageCampaignResponse**](BudgetUsageCampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.sdcampaignbudgetusage.v1+json
 - **Accept**: application/vnd.sdcampaignbudgetusage.v1+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. An object containing a list of budget usage response objects reflecting the same order as the input. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden. The request failed because user does not have access to a specified resource. |  -  |
**422** | Unprocessable entity. The server understood the request, but was unable to process the instruction. |  -  |
**429** | Too Many Requests. The request was rate-limited. Retry later. |  -  |
**500** | Internal Server BudgetUsageError - Something went wrong on the server. Retry later and report an BudgetUsageError if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

