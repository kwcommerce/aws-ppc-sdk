# openapi_client.TargetingApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_targeting_clause**](TargetingApi.md#archive_targeting_clause) | **DELETE** /sd/targets/{targetId} | Sets the &#x60;state&#x60; of a targeting clause to &#x60;archived&#x60;.
[**create_targeting_clauses**](TargetingApi.md#create_targeting_clauses) | **POST** /sd/targets | Creates one or more targeting clauses.
[**get_targets**](TargetingApi.md#get_targets) | **GET** /sd/targets/{targetId} | Gets a targeting clause specified by identifier.
[**get_targets_ex**](TargetingApi.md#get_targets_ex) | **GET** /sd/targets/extended/{targetId} | Gets extended information for a targeting clause.
[**list_targeting_clauses**](TargetingApi.md#list_targeting_clauses) | **GET** /sd/targets | Gets a list of targeting clauses.
[**list_targeting_clauses_ex**](TargetingApi.md#list_targeting_clauses_ex) | **GET** /sd/targets/extended | Gets a list of targeting clause objects with extended fields.
[**update_targeting_clauses**](TargetingApi.md#update_targeting_clauses) | **PUT** /sd/targets | Updates one or more targeting clauses.


# **archive_targeting_clause**
> TargetResponse archive_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Sets the `state` of a targeting clause to `archived`.

Equivalent to using the `updateTargetingClauses` operation to set the `state` property of a targeting clause to `archived`. See [Developer Notes](http://advertising.amazon.com/API/docs/guides/developer_notes#Archiving) for more information.

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
    api_instance = openapi_client.TargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 56 # int | The identifer of a targeting clause.

    try:
        # Sets the `state` of a targeting clause to `archived`.
        api_response = api_instance.archive_targeting_clause(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        print("The response of TargetingApi->archive_targeting_clause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetingApi->archive_targeting_clause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **target_id** | **int**| The identifer of a targeting clause. | 

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

# **create_targeting_clauses**
> List[TargetResponse] create_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_targeting_clause=create_targeting_clause)

Creates one or more targeting clauses.

Successfully created targeting clauses are assigned a unique `targetId` value.  Create new targeting clauses for **both** Audience and Contextual campaigns with tactic 'T00030' using the above and the following: | Contextual targeting clause | Description | |------------------|-------------| | similarProduct | Dynamic segment to target products that are similar to the advertised asin. We recommend using 'similarProduct' targeting for all adGroups. | | asinSameAs=B0123456789 | Target this product. | | asinCategorySameAs=12345 | Target products in the category. | | asinCategorySameAs=12345 asinBrandSameAs=45678 | Target products in the category and brand. |  **Refinements:** - asinBrandSameAs - asinPriceBetween - asinPriceGreaterThan - asinPriceLessThan - asinReviewRatingLessThan - asinReviewRatingGreaterThan - asinReviewRatingBetween - asinIsPrimeShippingEligible - asinAgeRangeSameAs - asinGenreSameAs  **Refinement Notes:** * Brand, price, and review predicates are optional and may only be specified if category is also specified. * Review predicates accept numbers between 0 and 5 and are inclusive. * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive. * 'similarProduct' has no expression value or refinements.  | Audience targeting clause | Description | |------------------|-------------| | views(exactProduct lookback=30) | Target an audience that has viewed the advertised asins in the past 7,14,30,60, or 90 days. Note: This target should only be used for productAds with SKU or ASIN. | | views(similarProduct lookback=60) | Target an audience that has viewed similar products to the advertised asins in the past 7,14,30,60, or 90 days. Note: This target should only be used for productAds with SKU or ASIN.| | views(asinCategorySameAs=12345 lookback=90) | Target an audience that has viewed products in the given category in the past 7,14,30,60, or 90 days. | | views(asinCategorySameAs=12345 asinBrandSameAs=45678 asinPriceBetween=50-100 lookback=60) | Target an audience that has viewed products in the given category, brand, and price range in the past 7,14,30,60, or 90 days. | | purchases(relatedProduct lookback=180) | Target an audience that has purchased a related product in the past 7,14,30,60,90,180 or 365 days. Note: This target should only be used for productAds with SKU or ASIN.| | purchases(exactProduct lookback=365) | Target an audience that has purchased the advertised asins in the past 7,14,30,60,90,180 or 365 days. Note: This target should only be used for productAds with SKU or ASIN.| | purchases(asinCategorySameAs=12345 asinBrandSameAs=45678 asinPriceBetween=50-100 lookback=90) | Target an audience that has purchased products in the given category, brand, and price range in the past 7,14,30,60,90,180 or 365 days |  | Content targeting clause | Description | |------------------|-------------| | contentCategorySameAs=amzn1.iab-content.325 | Target all Movies and Television Shows in the Action or Adventure genre |  Notes on content targeting: * The `contentCategorySameAs` targeting predicate is required  Note: 1. You can still create new targeting clauses for Contextual campaigns with tactic 'T00020' using the Contextual clauses above. 2. There is a limit of 200 targeting clauses per request for T00030. 3. There is a limit of 1000 targeting clauses per request for T00020. 4. There is a total limit of 1000 targeting clauses per ad group. 5. If you receive the error of \"Cannot create targeting clause: audience size is too small\", please expand or broaden your targeting clause to increase the audience size.

### Example


```python
import openapi_client
from openapi_client.models.create_targeting_clause import CreateTargetingClause
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
    api_instance = openapi_client.TargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_targeting_clause = [openapi_client.CreateTargetingClause()] # List[CreateTargetingClause] | A list of targeting clauses for creation. (optional)

    try:
        # Creates one or more targeting clauses.
        api_response = api_instance.create_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_targeting_clause=create_targeting_clause)
        print("The response of TargetingApi->create_targeting_clauses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetingApi->create_targeting_clauses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **create_targeting_clause** | [**List[CreateTargetingClause]**](CreateTargetingClause.md)| A list of targeting clauses for creation. | [optional] 

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
**207** | multi-status |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_targets**
> TargetingClause get_targets(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Gets a targeting clause specified by identifier.

This call returns the minimal set of targeting clause fields.

### Example


```python
import openapi_client
from openapi_client.models.targeting_clause import TargetingClause
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
    api_instance = openapi_client.TargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 56 # int | The identifier of a targeting clause.

    try:
        # Gets a targeting clause specified by identifier.
        api_response = api_instance.get_targets(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        print("The response of TargetingApi->get_targets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetingApi->get_targets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **target_id** | **int**| The identifier of a targeting clause. | 

### Return type

[**TargetingClause**](TargetingClause.md)

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

# **get_targets_ex**
> TargetingClauseEx get_targets_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)

Gets extended information for a targeting clause.

Gets a targeting clause object with extended fields. Note that this call returns the full set of targeting clause extended fields, but is less efficient than getTarget.

### Example


```python
import openapi_client
from openapi_client.models.targeting_clause_ex import TargetingClauseEx
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
    api_instance = openapi_client.TargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    target_id = 56 # int | The identifier of a targeting clause.

    try:
        # Gets extended information for a targeting clause.
        api_response = api_instance.get_targets_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, target_id)
        print("The response of TargetingApi->get_targets_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetingApi->get_targets_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **target_id** | **int**| The identifier of a targeting clause. | 

### Return type

[**TargetingClauseEx**](TargetingClauseEx.md)

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

# **list_targeting_clauses**
> List[TargetingClause] list_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)

Gets a list of targeting clauses.

Gets a list of targeting clauses objects for a requested set of Sponsored Display targets. Note that the Targeting Clause object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use the target operations that return the TargetingClauseEx object.

### Example


```python
import openapi_client
from openapi_client.models.targeting_clause import TargetingClause
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
    api_instance = openapi_client.TargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. 0-indexed record offset for the result set. Defaults to 0. (optional)
    count = 56 # int | Optional. Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. Restricts results to those with `state` set to values in the specified comma-separated list. (optional) (default to enabled, paused, archived)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional list of comma separated adGroupIds. Restricts results to targeting clauses with the specified `adGroupId`. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. Restricts results to targeting clauses within campaigns specified in comma-separated list. (optional)

    try:
        # Gets a list of targeting clauses.
        api_response = api_instance.list_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)
        print("The response of TargetingApi->list_targeting_clauses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetingApi->list_targeting_clauses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. 0-indexed record offset for the result set. Defaults to 0. | [optional] 
 **count** | **int**| Optional. Number of records to include in the paged response. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. Restricts results to those with &#x60;state&#x60; set to values in the specified comma-separated list. | [optional] [default to enabled, paused, archived]
 **ad_group_id_filter** | **str**| Optional list of comma separated adGroupIds. Restricts results to targeting clauses with the specified &#x60;adGroupId&#x60;. | [optional] 
 **campaign_id_filter** | **str**| Optional. Restricts results to targeting clauses within campaigns specified in comma-separated list. | [optional] 

### Return type

[**List[TargetingClause]**](TargetingClause.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_targeting_clauses_ex**
> List[TargetingClauseEx] list_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, target_id_filter=target_id_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)

Gets a list of targeting clause objects with extended fields.

Gets an array of TargetingClauseEx objects for a set of requested targets. Note that this call returns the full set of targeting clause extended fields, but is less efficient than getTargets.

### Example


```python
import openapi_client
from openapi_client.models.targeting_clause_ex import TargetingClauseEx
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
    api_instance = openapi_client.TargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. 0-indexed record offset for the result set. Defaults to 0. (optional)
    count = 56 # int | Optional. Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. Restricts results to keywords with state within the specified comma-separated list. Must be one of: `enabled`, `paused`, or `archived`. Default behavior is to include enabled, paused, and archived. (optional) (default to enabled, paused, archived)
    target_id_filter = 'target_id_filter_example' # str | Optional. Restricts results to ads with the specified `tagetId` specified in comma-separated list (optional)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional list of comma separated adGroupIds. Restricts results to targeting clauses with the specified `adGroupId`. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. Restricts results to ads within campaigns specified in comma-separated list. (optional)

    try:
        # Gets a list of targeting clause objects with extended fields.
        api_response = api_instance.list_targeting_clauses_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, target_id_filter=target_id_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)
        print("The response of TargetingApi->list_targeting_clauses_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetingApi->list_targeting_clauses_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. 0-indexed record offset for the result set. Defaults to 0. | [optional] 
 **count** | **int**| Optional. Number of records to include in the paged response. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. Restricts results to keywords with state within the specified comma-separated list. Must be one of: &#x60;enabled&#x60;, &#x60;paused&#x60;, or &#x60;archived&#x60;. Default behavior is to include enabled, paused, and archived. | [optional] [default to enabled, paused, archived]
 **target_id_filter** | **str**| Optional. Restricts results to ads with the specified &#x60;tagetId&#x60; specified in comma-separated list | [optional] 
 **ad_group_id_filter** | **str**| Optional list of comma separated adGroupIds. Restricts results to targeting clauses with the specified &#x60;adGroupId&#x60;. | [optional] 
 **campaign_id_filter** | **str**| Optional. Restricts results to ads within campaigns specified in comma-separated list. | [optional] 

### Return type

[**List[TargetingClauseEx]**](TargetingClauseEx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**404** | Not Found - Requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_targeting_clauses**
> List[TargetResponse] update_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_targeting_clause=update_targeting_clause)

Updates one or more targeting clauses.

Updates one or more targeting clauses. Targeting clauses are identified using their targetId. The mutable fields are `bid` and `state`. Maximum length of the array is 100 objects.

### Example


```python
import openapi_client
from openapi_client.models.target_response import TargetResponse
from openapi_client.models.update_targeting_clause import UpdateTargetingClause
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
    api_instance = openapi_client.TargetingApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_targeting_clause = [openapi_client.UpdateTargetingClause()] # List[UpdateTargetingClause] | A list of up to 1000 targeting clauses. Mutable fields: * `state` * `bid` (only mutable when the targeting clause's adGroup does not have any enabled optimization rule) (optional)

    try:
        # Updates one or more targeting clauses.
        api_response = api_instance.update_targeting_clauses(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_targeting_clause=update_targeting_clause)
        print("The response of TargetingApi->update_targeting_clauses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetingApi->update_targeting_clauses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **update_targeting_clause** | [**List[UpdateTargetingClause]**](UpdateTargetingClause.md)| A list of up to 1000 targeting clauses. Mutable fields: * &#x60;state&#x60; * &#x60;bid&#x60; (only mutable when the targeting clause&#39;s adGroup does not have any enabled optimization rule) | [optional] 

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

