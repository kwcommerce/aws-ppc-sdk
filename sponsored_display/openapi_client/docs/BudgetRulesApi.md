# openapi_client.BudgetRulesApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_budget_rules_for_sd_campaigns**](BudgetRulesApi.md#create_budget_rules_for_sd_campaigns) | **POST** /sd/budgetRules | Creates one or more budget rules.
[**get_budget_rule_by_rule_id_for_sd_campaigns**](BudgetRulesApi.md#get_budget_rule_by_rule_id_for_sd_campaigns) | **GET** /sd/budgetRules/{budgetRuleId} | Gets a budget rule specified by identifier.
[**get_sd_budget_rules_for_advertiser**](BudgetRulesApi.md#get_sd_budget_rules_for_advertiser) | **GET** /sd/budgetRules | Get all budget rules created by an advertiser
[**update_budget_rules_for_sd_campaigns**](BudgetRulesApi.md#update_budget_rules_for_sd_campaigns) | **PUT** /sd/budgetRules | Update one or more budget rules.


# **create_budget_rules_for_sd_campaigns**
> CreateBudgetRulesResponse create_budget_rules_for_sd_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_sd_budget_rules_request)

Creates one or more budget rules.

### Example


```python
import openapi_client
from openapi_client.models.create_budget_rules_response import CreateBudgetRulesResponse
from openapi_client.models.create_sd_budget_rules_request import CreateSDBudgetRulesRequest
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
    api_instance = openapi_client.BudgetRulesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account. This is a required header for advertisers and integrators using the Advertising API.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API.
    create_sd_budget_rules_request = openapi_client.CreateSDBudgetRulesRequest() # CreateSDBudgetRulesRequest | 

    try:
        # Creates one or more budget rules.
        api_response = api_instance.create_budget_rules_for_sd_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_sd_budget_rules_request)
        print("The response of BudgetRulesApi->create_budget_rules_for_sd_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetRulesApi->create_budget_rules_for_sd_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. This is a required header for advertisers and integrators using the Advertising API. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API. | 
 **create_sd_budget_rules_request** | [**CreateSDBudgetRulesRequest**](CreateSDBudgetRulesRequest.md)|  | 

### Return type

[**CreateBudgetRulesResponse**](CreateBudgetRulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. An object containing a list of budget rule response objects reflecting the same order as the input. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden. The request failed because user does not have access to a specified resource. |  -  |
**422** | Unprocessable entity. The server understood the request, but was unable to process the instruction. |  -  |
**429** | Too Many Requests. The request was rate-limited. Retry later. |  -  |
**500** | Internal Server BudgetRuleError - Something went wrong on the server. Retry later and report an BudgetRuleError if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_rule_by_rule_id_for_sd_campaigns**
> GetSDBudgetRuleResponse get_budget_rule_by_rule_id_for_sd_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, budget_rule_id)

Gets a budget rule specified by identifier.

### Example


```python
import openapi_client
from openapi_client.models.get_sd_budget_rule_response import GetSDBudgetRuleResponse
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
    api_instance = openapi_client.BudgetRulesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account. This is a required header for advertisers and integrators using the Advertising API.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API.
    budget_rule_id = 'budget_rule_id_example' # str | The budget rule identifier.

    try:
        # Gets a budget rule specified by identifier.
        api_response = api_instance.get_budget_rule_by_rule_id_for_sd_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, budget_rule_id)
        print("The response of BudgetRulesApi->get_budget_rule_by_rule_id_for_sd_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetRulesApi->get_budget_rule_by_rule_id_for_sd_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. This is a required header for advertisers and integrators using the Advertising API. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API. | 
 **budget_rule_id** | **str**| The budget rule identifier. | 

### Return type

[**GetSDBudgetRuleResponse**](GetSDBudgetRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden. The request failed because user does not have access to a specified resource. |  -  |
**422** | Unprocessable entity. The server understood the request, but was unable to process the instruction. |  -  |
**429** | Too Many Requests. The request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error. Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sd_budget_rules_for_advertiser**
> GetSDBudgetRulesForAdvertiserResponse get_sd_budget_rules_for_advertiser(amazon_advertising_api_client_id, amazon_advertising_api_scope, page_size, next_token=next_token)

Get all budget rules created by an advertiser

### Example


```python
import openapi_client
from openapi_client.models.get_sd_budget_rules_for_advertiser_response import GetSDBudgetRulesForAdvertiserResponse
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
    api_instance = openapi_client.BudgetRulesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account. This is a required header for advertisers and integrators using the Advertising API.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API.
    page_size = 3.4 # float | Sets a limit on the number of results returned. Maximum limit of `pageSize` is 30.
    next_token = 'next_token_example' # str | To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results. (optional)

    try:
        # Get all budget rules created by an advertiser
        api_response = api_instance.get_sd_budget_rules_for_advertiser(amazon_advertising_api_client_id, amazon_advertising_api_scope, page_size, next_token=next_token)
        print("The response of BudgetRulesApi->get_sd_budget_rules_for_advertiser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetRulesApi->get_sd_budget_rules_for_advertiser: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. This is a required header for advertisers and integrators using the Advertising API. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API. | 
 **page_size** | **float**| Sets a limit on the number of results returned. Maximum limit of &#x60;pageSize&#x60; is 30. | 
 **next_token** | **str**| To retrieve the next page of results, call the same operation and specify this token in the request. If the &#x60;nextToken&#x60; field is empty, there are no further results. | [optional] 

### Return type

[**GetSDBudgetRulesForAdvertiserResponse**](GetSDBudgetRulesForAdvertiserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden. The request failed because user does not have access to a specified resource. |  -  |
**422** | Unprocessable entity. The server understood the request, but was unable to process the instruction. |  -  |
**429** | Too Many Requests. The request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error. Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget_rules_for_sd_campaigns**
> UpdateBudgetRulesResponse update_budget_rules_for_sd_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_sd_budget_rules_request)

Update one or more budget rules.

### Example


```python
import openapi_client
from openapi_client.models.update_budget_rules_response import UpdateBudgetRulesResponse
from openapi_client.models.update_sd_budget_rules_request import UpdateSDBudgetRulesRequest
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
    api_instance = openapi_client.BudgetRulesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account. This is a required header for advertisers and integrators using the Advertising API.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API.
    update_sd_budget_rules_request = openapi_client.UpdateSDBudgetRulesRequest() # UpdateSDBudgetRulesRequest | 

    try:
        # Update one or more budget rules.
        api_response = api_instance.update_budget_rules_for_sd_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_sd_budget_rules_request)
        print("The response of BudgetRulesApi->update_budget_rules_for_sd_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetRulesApi->update_budget_rules_for_sd_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. This is a required header for advertisers and integrators using the Advertising API. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. This is a required header for advertisers and integrators using the Advertising API. | 
 **update_sd_budget_rules_request** | [**UpdateSDBudgetRulesRequest**](UpdateSDBudgetRulesRequest.md)|  | 

### Return type

[**UpdateBudgetRulesResponse**](UpdateBudgetRulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. An object containing a list of budget rule response objects reflecting the same order as the input. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden. The request failed because user does not have access to a specified resource. |  -  |
**422** | Unprocessable entity. The server understood the request, but was unable to process the instruction. |  -  |
**429** | Too Many Requests. The request was rate-limited. Retry later. |  -  |
**500** | Internal Server BudgetRuleError - Something went wrong on the server. Retry later and report an BudgetRuleError if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

