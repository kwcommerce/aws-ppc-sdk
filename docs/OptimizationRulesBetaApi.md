# openapi_client.OptimizationRulesBetaApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_optimization_rules_with_ad_group**](OptimizationRulesBetaApi.md#associate_optimization_rules_with_ad_group) | **POST** /sd/adGroups/{adGroupId}/optimizationRules | Associate one or more optimization rules to an ad group specified by identifier.
[**create_optimization_rules**](OptimizationRulesBetaApi.md#create_optimization_rules) | **POST** /sd/optimizationRules | Creates one or more optimization rules, also known as outcome optimizations.
[**disassociate_optimization_rules_from_ad_group**](OptimizationRulesBetaApi.md#disassociate_optimization_rules_from_ad_group) | **POST** /sd/adGroups/{adGroupId}/optimizationRules/disassociate | Disassociate one or more optimization rules from an ad group specified by identifier.
[**list_optimization_rules**](OptimizationRulesBetaApi.md#list_optimization_rules) | **GET** /sd/optimizationRules | Gets a list of optimization rules.
[**sd_ad_groups_ad_group_id_optimization_rules_get**](OptimizationRulesBetaApi.md#sd_ad_groups_ad_group_id_optimization_rules_get) | **GET** /sd/adGroups/{adGroupId}/optimizationRules | Gets a list of optimization rules associated to an adgroup specified by identifier.
[**sd_optimization_rules_optimization_rule_id_get**](OptimizationRulesBetaApi.md#sd_optimization_rules_optimization_rule_id_get) | **GET** /sd/optimizationRules/{optimizationRuleId} | Gets a requested optimization rule.
[**update_optimization_rules**](OptimizationRulesBetaApi.md#update_optimization_rules) | **PUT** /sd/optimizationRules | Updates one or more optimization rules.


# **associate_optimization_rules_with_ad_group**
> List[OptimizationRuleResponse] associate_optimization_rules_with_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id, create_associated_optimization_rules_request=create_associated_optimization_rules_request)

Associate one or more optimization rules to an ad group specified by identifier.

 * When an optimization rule is associated to an ad group, manual bids for individual targets will be overridden. * Only one optimization rule can be associated per adGroup. This note will be removed when multiple rules are supported per adGroup.

### Example


```python
import openapi_client
from openapi_client.models.create_associated_optimization_rules_request import CreateAssociatedOptimizationRulesRequest
from openapi_client.models.optimization_rule_response import OptimizationRuleResponse
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
    api_instance = openapi_client.OptimizationRulesBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 56 # int | The identifier of the ad group.
    create_associated_optimization_rules_request = openapi_client.CreateAssociatedOptimizationRulesRequest() # CreateAssociatedOptimizationRulesRequest | A list of optimization rule identifiers. Only one optimization rule identifier is currently supported per request. This note will be removed when multiple rule identifiers are supported.  For each ad group, only one optimization rule metric name is supported, based on the ad group's `bidOptimization` type. Refer to the following table for the metric names supported for each type. |  AdGroup.bidOptimization |     Supported OptimizationRule.metricName       | |------------------|--------------------| |   reach       | COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS  | |   clicks      | COST_PER_CLICK          | |  conversions  | COST_PER_ORDER          | (optional)

    try:
        # Associate one or more optimization rules to an ad group specified by identifier.
        api_response = api_instance.associate_optimization_rules_with_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id, create_associated_optimization_rules_request=create_associated_optimization_rules_request)
        print("The response of OptimizationRulesBetaApi->associate_optimization_rules_with_ad_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationRulesBetaApi->associate_optimization_rules_with_ad_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_group_id** | **int**| The identifier of the ad group. | 
 **create_associated_optimization_rules_request** | [**CreateAssociatedOptimizationRulesRequest**](CreateAssociatedOptimizationRulesRequest.md)| A list of optimization rule identifiers. Only one optimization rule identifier is currently supported per request. This note will be removed when multiple rule identifiers are supported.  For each ad group, only one optimization rule metric name is supported, based on the ad group&#39;s &#x60;bidOptimization&#x60; type. Refer to the following table for the metric names supported for each type. |  AdGroup.bidOptimization |     Supported OptimizationRule.metricName       | |------------------|--------------------| |   reach       | COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS  | |   clicks      | COST_PER_CLICK          | |  conversions  | COST_PER_ORDER          | | [optional] 

### Return type

[**List[OptimizationRuleResponse]**](OptimizationRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_optimization_rules**
> List[OptimizationRuleResponse] create_optimization_rules(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_optimization_rule=create_optimization_rule)

Creates one or more optimization rules, also known as outcome optimizations.

 * When an optimization rule is associated to an ad group, manual bids for individual targets will be overridden. * Optimization rules can only be associated to ad groups that have productAds with ASIN or SKU. * We may add targets while your campaign is running to try to stay at or below a cost per order value you have specified. * Only one optimization rule can be associated per adGroup.  * If you are using optimization rules, the following campaign budget must be at least:   - 5x the value of any COST_PER_ORDER threshold.   - 10x the value of any COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS threshold.   - 20x the value of any COST_PER_CLICK threshold.

### Example


```python
import openapi_client
from openapi_client.models.create_optimization_rule import CreateOptimizationRule
from openapi_client.models.optimization_rule_response import OptimizationRuleResponse
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
    api_instance = openapi_client.OptimizationRulesBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_optimization_rule = [openapi_client.CreateOptimizationRule()] # List[CreateOptimizationRule] | An array of OptimizationRule objects. For each object, specify required fields and their values. Required fields are `state` and `ruleConditions`. (optional)

    try:
        # Creates one or more optimization rules, also known as outcome optimizations.
        api_response = api_instance.create_optimization_rules(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_optimization_rule=create_optimization_rule)
        print("The response of OptimizationRulesBetaApi->create_optimization_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationRulesBetaApi->create_optimization_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **create_optimization_rule** | [**List[CreateOptimizationRule]**](CreateOptimizationRule.md)| An array of OptimizationRule objects. For each object, specify required fields and their values. Required fields are &#x60;state&#x60; and &#x60;ruleConditions&#x60;. | [optional] 

### Return type

[**List[OptimizationRuleResponse]**](OptimizationRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disassociate_optimization_rules_from_ad_group**
> OptimizationRuleAssociationResponse disassociate_optimization_rules_from_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id, create_associated_optimization_rules_request=create_associated_optimization_rules_request)

Disassociate one or more optimization rules from an ad group specified by identifier.

 * Only one optimization rule can be disassociated per adGroup. This note will be removed when multiple rules are supported per adGroup. * When an optimization rule is disassociated from an ad group, you can set the manual bids for the individual targets under the adGroup.

### Example


```python
import openapi_client
from openapi_client.models.create_associated_optimization_rules_request import CreateAssociatedOptimizationRulesRequest
from openapi_client.models.optimization_rule_association_response import OptimizationRuleAssociationResponse
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
    api_instance = openapi_client.OptimizationRulesBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 56 # int | The identifier of the ad group.
    create_associated_optimization_rules_request = openapi_client.CreateAssociatedOptimizationRulesRequest() # CreateAssociatedOptimizationRulesRequest | A list of optimization rule identifiers. Only one optimization rule identifier is currently supported per request. This note will be removed when multiple rule identifiers are supported. (optional)

    try:
        # Disassociate one or more optimization rules from an ad group specified by identifier.
        api_response = api_instance.disassociate_optimization_rules_from_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id, create_associated_optimization_rules_request=create_associated_optimization_rules_request)
        print("The response of OptimizationRulesBetaApi->disassociate_optimization_rules_from_ad_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationRulesBetaApi->disassociate_optimization_rules_from_ad_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_group_id** | **int**| The identifier of the ad group. | 
 **create_associated_optimization_rules_request** | [**CreateAssociatedOptimizationRulesRequest**](CreateAssociatedOptimizationRulesRequest.md)| A list of optimization rule identifiers. Only one optimization rule identifier is currently supported per request. This note will be removed when multiple rule identifiers are supported. | [optional] 

### Return type

[**OptimizationRuleAssociationResponse**](OptimizationRuleAssociationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_optimization_rules**
> List[OptimizationRule] list_optimization_rules(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, name=name, optimization_rule_id_filter=optimization_rule_id_filter, ad_group_id_filter=ad_group_id_filter)

Gets a list of optimization rules.

Gets an array of OptimizationRule objects for a requested set of Sponsored Display optimization rules.

### Example


```python
import openapi_client
from openapi_client.models.optimization_rule import OptimizationRule
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
    api_instance = openapi_client.OptimizationRulesBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. Sets a cursor into the requested set of optimization rules. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional)
    count = 56 # int | Optional. Sets the number of OptimizationRule objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten optimization rules set `startIndex=0` and `count=10`. To return the next ten optimization rules, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional)
    state_filter = 'enabled' # str | Optional. The returned array is filtered to include only optimization rules with state set to one of the values in the specified comma-delimited list. Available values:   - enabled   - paused [COMING LATER]   - enabled, paused [COMING LATER] (optional) (default to 'enabled')
    name = 'name_example' # str | Optional. The returned array includes only optimization rules with the specified name using an exact string match. (optional)
    optimization_rule_id_filter = 'optimization_rule_id_filter_example' # str | Optional. The returned array is filtered to include only optimization rules associated with the optimization rule identifiers in the specified comma-delimited list.  Maximum size limit 50. (optional)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional. The returned array is filtered to include only optimization rules associated with the ad group identifiers in the comma-delimited list.  Maximum size limit 50. (optional)

    try:
        # Gets a list of optimization rules.
        api_response = api_instance.list_optimization_rules(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, name=name, optimization_rule_id_filter=optimization_rule_id_filter, ad_group_id_filter=ad_group_id_filter)
        print("The response of OptimizationRulesBetaApi->list_optimization_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationRulesBetaApi->list_optimization_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of optimization rules. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] 
 **count** | **int**| Optional. Sets the number of OptimizationRule objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten optimization rules set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten optimization rules, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. The returned array is filtered to include only optimization rules with state set to one of the values in the specified comma-delimited list. Available values:   - enabled   - paused [COMING LATER]   - enabled, paused [COMING LATER] | [optional] [default to &#39;enabled&#39;]
 **name** | **str**| Optional. The returned array includes only optimization rules with the specified name using an exact string match. | [optional] 
 **optimization_rule_id_filter** | **str**| Optional. The returned array is filtered to include only optimization rules associated with the optimization rule identifiers in the specified comma-delimited list.  Maximum size limit 50. | [optional] 
 **ad_group_id_filter** | **str**| Optional. The returned array is filtered to include only optimization rules associated with the ad group identifiers in the comma-delimited list.  Maximum size limit 50. | [optional] 

### Return type

[**List[OptimizationRule]**](OptimizationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sd_ad_groups_ad_group_id_optimization_rules_get**
> List[OptimizationRule] sd_ad_groups_ad_group_id_optimization_rules_get(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Gets a list of optimization rules associated to an adgroup specified by identifier.

Gets an OptimizationRule object for a requested Sponsored Display optimization rule.

### Example


```python
import openapi_client
from openapi_client.models.optimization_rule import OptimizationRule
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
    api_instance = openapi_client.OptimizationRulesBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 56 # int | The identifier of the ad group.

    try:
        # Gets a list of optimization rules associated to an adgroup specified by identifier.
        api_response = api_instance.sd_ad_groups_ad_group_id_optimization_rules_get(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        print("The response of OptimizationRulesBetaApi->sd_ad_groups_ad_group_id_optimization_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationRulesBetaApi->sd_ad_groups_ad_group_id_optimization_rules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_group_id** | **int**| The identifier of the ad group. | 

### Return type

[**List[OptimizationRule]**](OptimizationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**404** | Not Found - Requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sd_optimization_rules_optimization_rule_id_get**
> OptimizationRule sd_optimization_rules_optimization_rule_id_get(amazon_advertising_api_client_id, amazon_advertising_api_scope, optimization_rule_id)

Gets a requested optimization rule.

Gets an OptimizationRule object for a requested Sponsored Display optimization rule.

### Example


```python
import openapi_client
from openapi_client.models.optimization_rule import OptimizationRule
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
    api_instance = openapi_client.OptimizationRulesBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    optimization_rule_id = 'optimization_rule_id_example' # str | The identifier of the requested optimization rule.

    try:
        # Gets a requested optimization rule.
        api_response = api_instance.sd_optimization_rules_optimization_rule_id_get(amazon_advertising_api_client_id, amazon_advertising_api_scope, optimization_rule_id)
        print("The response of OptimizationRulesBetaApi->sd_optimization_rules_optimization_rule_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationRulesBetaApi->sd_optimization_rules_optimization_rule_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **optimization_rule_id** | **str**| The identifier of the requested optimization rule. | 

### Return type

[**OptimizationRule**](OptimizationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**404** | Not Found - Requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_optimization_rules**
> List[OptimizationRuleResponse] update_optimization_rules(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_optimization_rule=update_optimization_rule)

Updates one or more optimization rules.

### Example


```python
import openapi_client
from openapi_client.models.optimization_rule_response import OptimizationRuleResponse
from openapi_client.models.update_optimization_rule import UpdateOptimizationRule
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
    api_instance = openapi_client.OptimizationRulesBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_optimization_rule = [openapi_client.UpdateOptimizationRule()] # List[UpdateOptimizationRule] | An array of OptimizationRule objects. For each object, specify an optimization rule identifier and mutable fields with their updated values. The mutable fields are `ruleName`, `state`, and `ruleConditions`. (optional)

    try:
        # Updates one or more optimization rules.
        api_response = api_instance.update_optimization_rules(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_optimization_rule=update_optimization_rule)
        print("The response of OptimizationRulesBetaApi->update_optimization_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptimizationRulesBetaApi->update_optimization_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **update_optimization_rule** | [**List[UpdateOptimizationRule]**](UpdateOptimizationRule.md)| An array of OptimizationRule objects. For each object, specify an optimization rule identifier and mutable fields with their updated values. The mutable fields are &#x60;ruleName&#x60;, &#x60;state&#x60;, and &#x60;ruleConditions&#x60;. | [optional] 

### Return type

[**List[OptimizationRuleResponse]**](OptimizationRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

