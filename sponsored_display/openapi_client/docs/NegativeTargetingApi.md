# openapi_client.NegativeTargetingApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_negative_targeting_clause**](NegativeTargetingApi.md#archive_negative_targeting_clause) | **DELETE** /sd/negativeTargets/{negativeTargetId} | Sets the &#x60;state&#x60; of a negative targeting clause to &#x60;archived&#x60;.
[**create_negative_targeting_clauses**](NegativeTargetingApi.md#create_negative_targeting_clauses) | **POST** /sd/negativeTargets | Creates one or more negative targeting clauses.
[**get_negative_targets**](NegativeTargetingApi.md#get_negative_targets) | **GET** /sd/negativeTargets/{negativeTargetId} | Gets a negative targeting clause specified by identifier.
[**get_negative_targets_ex**](NegativeTargetingApi.md#get_negative_targets_ex) | **GET** /sd/negativeTargets/extended/{negativeTargetId} | Gets extended information for a negative targeting clause.
[**list_negative_targeting_clauses**](NegativeTargetingApi.md#list_negative_targeting_clauses) | **GET** /sd/negativeTargets | Gets a list of negative targeting clauses.
[**list_negative_targeting_clauses_ex**](NegativeTargetingApi.md#list_negative_targeting_clauses_ex) | **GET** /sd/negativeTargets/extended | Gets a list of negative targeting clause objects with extended fields.
[**update_negative_targeting_clauses**](NegativeTargetingApi.md#update_negative_targeting_clauses) | **PUT** /sd/negativeTargets | Updates one or more negative targeting clauses.


# **archive_negative_targeting_clause**
> TargetResponse archive_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, negative_target_id)

Sets the `state` of a negative targeting clause to `archived`.

Equivalent to using the updateNegativeTargetingClauses operation to set the `state` property of a targeting clause to `archived`. See [Developer Notes](http://advertising.amazon.com/API/docs/guides/developer_notes#Archiving) for more information.

### Example


```python
import openapi_client
from openapi_client.models.target_response import TargetResponse
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
    api_instance = openapi_client.NegativeTargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    negative_target_id = 56 # int | The identifier of a negative targeting clause.

    try:
        # Sets the `state` of a negative targeting clause to `archived`.
        api_response = api_instance.archive_negative_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, negative_target_id)
        print("The response of NegativeTargetingApi->archive_negative_targeting_clause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NegativeTargetingApi->archive_negative_targeting_clause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **negative_target_id** | **int**| The identifier of a negative targeting clause. | 

### Return type

[**TargetResponse**](TargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**404** | Not Found - Requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_negative_targeting_clauses**
> List[TargetResponse] create_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_negative_targeting_clause=create_negative_targeting_clause)

Creates one or more negative targeting clauses.

Successfully created negative targeting clauses associated with an ad group are assigned a unique target identifier. Product negative targeting clause examples: | Negative targeting clause | Description | |---------------------------|-------------| | asinSameAs=B0123456789 | Negatively target this product.| | asinBrandSameAs=12345 | Negatively target products in the brand.|

### Example


```python
import openapi_client
from openapi_client.models.create_negative_targeting_clause import CreateNegativeTargetingClause
from openapi_client.models.target_response import TargetResponse
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
    api_instance = openapi_client.NegativeTargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_negative_targeting_clause = [openapi_client.CreateNegativeTargetingClause()] # List[CreateNegativeTargetingClause] | A list of up to 100 negative targeting clauses for creation. (optional)

    try:
        # Creates one or more negative targeting clauses.
        api_response = api_instance.create_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_negative_targeting_clause=create_negative_targeting_clause)
        print("The response of NegativeTargetingApi->create_negative_targeting_clauses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NegativeTargetingApi->create_negative_targeting_clauses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **create_negative_targeting_clause** | [**List[CreateNegativeTargetingClause]**](CreateNegativeTargetingClause.md)| A list of up to 100 negative targeting clauses for creation. | [optional] 

### Return type

[**List[TargetResponse]**](TargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-Status |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negative_targets**
> NegativeTargetingClause get_negative_targets(amazon_advertising_api_client_id, amazon_advertising_api_scope, negative_target_id)

Gets a negative targeting clause specified by identifier.

This call returns the minimal set of negative targeting clause fields, but is more efficient than getNegativeTargetsEx.

### Example


```python
import openapi_client
from openapi_client.models.negative_targeting_clause import NegativeTargetingClause
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
    api_instance = openapi_client.NegativeTargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    negative_target_id = 56 # int | The negative targeting clause identifier.

    try:
        # Gets a negative targeting clause specified by identifier.
        api_response = api_instance.get_negative_targets(amazon_advertising_api_client_id, amazon_advertising_api_scope, negative_target_id)
        print("The response of NegativeTargetingApi->get_negative_targets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NegativeTargetingApi->get_negative_targets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **negative_target_id** | **int**| The negative targeting clause identifier. | 

### Return type

[**NegativeTargetingClause**](NegativeTargetingClause.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**404** | Not Found - Requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_negative_targets_ex**
> NegativeTargetingClauseEx get_negative_targets_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, negative_target_id)

Gets extended information for a negative targeting clause.

Gets a negative targeting clause with extended fields. Note that this call returns the full set of negative targeting clause extended fields, but is less efficient than getNegativeTarget.

### Example


```python
import openapi_client
from openapi_client.models.negative_targeting_clause_ex import NegativeTargetingClauseEx
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
    api_instance = openapi_client.NegativeTargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    negative_target_id = 56 # int | The negative targeting clause identifier.

    try:
        # Gets extended information for a negative targeting clause.
        api_response = api_instance.get_negative_targets_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, negative_target_id)
        print("The response of NegativeTargetingApi->get_negative_targets_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NegativeTargetingApi->get_negative_targets_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **negative_target_id** | **int**| The negative targeting clause identifier. | 

### Return type

[**NegativeTargetingClauseEx**](NegativeTargetingClauseEx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**404** | Not Found - Requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_negative_targeting_clauses**
> List[NegativeTargetingClause] list_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)

Gets a list of negative targeting clauses.

Gets a list of negative targeting clauses objects for a requested set of Sponsored Display negative targets. Note that the Negative Targeting Clause object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use the negative target operations that return the NegativeTargetingClauseEx object.

### Example


```python
import openapi_client
from openapi_client.models.negative_targeting_clause import NegativeTargetingClause
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
    api_instance = openapi_client.NegativeTargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. 0-indexed record offset for the result set. Defaults to 0. (optional)
    count = 56 # int | Optional. Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. Restricts results to those with state within the specified comma-separated list. Must be one of: `enabled`, `paused`, or `archived`. Default behavior is to include enabled, paused, and archived. (optional) (default to enabled, paused, archived)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional list of comma separated adGroupIds. Restricts results to negative targeting clauses with the specified `adGroupId`. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. Restricts results to targeting clauses within campaigns specified in comma-separated list. (optional)

    try:
        # Gets a list of negative targeting clauses.
        api_response = api_instance.list_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)
        print("The response of NegativeTargetingApi->list_negative_targeting_clauses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NegativeTargetingApi->list_negative_targeting_clauses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. 0-indexed record offset for the result set. Defaults to 0. | [optional] 
 **count** | **int**| Optional. Number of records to include in the paged response. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. Restricts results to those with state within the specified comma-separated list. Must be one of: &#x60;enabled&#x60;, &#x60;paused&#x60;, or &#x60;archived&#x60;. Default behavior is to include enabled, paused, and archived. | [optional] [default to enabled, paused, archived]
 **ad_group_id_filter** | **str**| Optional list of comma separated adGroupIds. Restricts results to negative targeting clauses with the specified &#x60;adGroupId&#x60;. | [optional] 
 **campaign_id_filter** | **str**| Optional. Restricts results to targeting clauses within campaigns specified in comma-separated list. | [optional] 

### Return type

[**List[NegativeTargetingClause]**](NegativeTargetingClause.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_negative_targeting_clauses_ex**
> List[NegativeTargetingClauseEx] list_negative_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, target_id_filter=target_id_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)

Gets a list of negative targeting clause objects with extended fields.

Gets an array of NegativeTargetingClauseEx objects for a set of requested negative targets. Note that this call returns the full set of negative targeting clause extended fields, but is less efficient than getNegativeTargets.

### Example


```python
import openapi_client
from openapi_client.models.negative_targeting_clause_ex import NegativeTargetingClauseEx
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
    api_instance = openapi_client.NegativeTargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. 0-indexed record offset for the result set. Defaults to 0. (optional)
    count = 56 # int | Optional. Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. Restricts results to keywords with state within the specified comma-separated list. Must be one of: `enabled`, `paused`, or `archived`. Default behavior is to include `enabled`, `paused`, and `archived`. (optional) (default to enabled, paused, archived)
    target_id_filter = 'target_id_filter_example' # str | Optional. Restricts results to ads with the specified `tagetId` specified in comma-separated list (optional)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional list of comma separated adGroupIds. Restricts results to negative targeting clauses with the specified `adGroupId`. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. Restricts results to ads within campaigns specified in the comma-separated list. (optional)

    try:
        # Gets a list of negative targeting clause objects with extended fields.
        api_response = api_instance.list_negative_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, target_id_filter=target_id_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)
        print("The response of NegativeTargetingApi->list_negative_targeting_clauses_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NegativeTargetingApi->list_negative_targeting_clauses_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. 0-indexed record offset for the result set. Defaults to 0. | [optional] 
 **count** | **int**| Optional. Number of records to include in the paged response. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. Restricts results to keywords with state within the specified comma-separated list. Must be one of: &#x60;enabled&#x60;, &#x60;paused&#x60;, or &#x60;archived&#x60;. Default behavior is to include &#x60;enabled&#x60;, &#x60;paused&#x60;, and &#x60;archived&#x60;. | [optional] [default to enabled, paused, archived]
 **target_id_filter** | **str**| Optional. Restricts results to ads with the specified &#x60;tagetId&#x60; specified in comma-separated list | [optional] 
 **ad_group_id_filter** | **str**| Optional list of comma separated adGroupIds. Restricts results to negative targeting clauses with the specified &#x60;adGroupId&#x60;. | [optional] 
 **campaign_id_filter** | **str**| Optional. Restricts results to ads within campaigns specified in the comma-separated list. | [optional] 

### Return type

[**List[NegativeTargetingClauseEx]**](NegativeTargetingClauseEx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**404** | Not Found - Requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_negative_targeting_clauses**
> List[TargetResponse] update_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_negative_targeting_clause=update_negative_targeting_clause)

Updates one or more negative targeting clauses.

Updates one or more negative targeting clauses. Negative targeting clauses are identified using their targetId. The mutable field is `state`. Maximum length of the array is 100 objects.

### Example


```python
import openapi_client
from openapi_client.models.target_response import TargetResponse
from openapi_client.models.update_negative_targeting_clause import UpdateNegativeTargetingClause
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
    api_instance = openapi_client.NegativeTargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_negative_targeting_clause = [openapi_client.UpdateNegativeTargetingClause()] # List[UpdateNegativeTargetingClause] | A list of up to 100 negative targeting clauses. Note that the only mutable field is `state`. (optional)

    try:
        # Updates one or more negative targeting clauses.
        api_response = api_instance.update_negative_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_negative_targeting_clause=update_negative_targeting_clause)
        print("The response of NegativeTargetingApi->update_negative_targeting_clauses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NegativeTargetingApi->update_negative_targeting_clauses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **update_negative_targeting_clause** | [**List[UpdateNegativeTargetingClause]**](UpdateNegativeTargetingClause.md)| A list of up to 100 negative targeting clauses. Note that the only mutable field is &#x60;state&#x60;. | [optional] 

### Return type

[**List[TargetResponse]**](TargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-Status |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

