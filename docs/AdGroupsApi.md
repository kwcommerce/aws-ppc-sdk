# openapi_client.AdGroupsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_ad_group**](AdGroupsApi.md#archive_ad_group) | **DELETE** /sd/adGroups/{adGroupId} | Sets the ad group status to archived.
[**create_ad_groups**](AdGroupsApi.md#create_ad_groups) | **POST** /sd/adGroups | Creates one or more ad groups.
[**get_ad_group**](AdGroupsApi.md#get_ad_group) | **GET** /sd/adGroups/{adGroupId} | Gets a requested ad group.
[**get_ad_group_response_ex**](AdGroupsApi.md#get_ad_group_response_ex) | **GET** /sd/adGroups/extended/{adGroupId} | Gets extended information for a requested ad group.
[**list_ad_groups**](AdGroupsApi.md#list_ad_groups) | **GET** /sd/adGroups | Gets a list of ad groups.
[**list_ad_groups_ex**](AdGroupsApi.md#list_ad_groups_ex) | **GET** /sd/adGroups/extended | Gets a list of ad groups with extended fields.
[**update_ad_groups**](AdGroupsApi.md#update_ad_groups) | **PUT** /sd/adGroups | Updates on or more ad groups.


# **archive_ad_group**
> AdGroupResponse archive_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Sets the ad group status to archived.

This operation is equivalent to an update operation that sets the status field to 'archived'. Note that setting the status field to 'archived' is permanent and can't be undone. See [Developer Notes](https://advertising.amazon.com/API/docs/en-us/info/developer-notes#archiving) for more information.

### Example


```python
import openapi_client
from openapi_client.models.ad_group_response import AdGroupResponse
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
    api_instance = openapi_client.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 56 # int | The identifier of the requested ad group.

    try:
        # Sets the ad group status to archived.
        api_response = api_instance.archive_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        print("The response of AdGroupsApi->archive_ad_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdGroupsApi->archive_ad_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_group_id** | **int**| The identifier of the requested ad group. | 

### Return type

[**AdGroupResponse**](AdGroupResponse.md)

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

# **create_ad_groups**
> List[AdGroupResponse] create_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_ad_group=create_ad_group)

Creates one or more ad groups.

### Example


```python
import openapi_client
from openapi_client.models.ad_group_response import AdGroupResponse
from openapi_client.models.create_ad_group import CreateAdGroup
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
    api_instance = openapi_client.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_ad_group = [openapi_client.CreateAdGroup()] # List[CreateAdGroup] | An array of AdGroup objects. For each object, specify required fields and their values. Required fields are `campaignId`, `name`, `state`, and `defaultBid`. Maximum length of the array is 100 objects. Note - when using landingPageType of OFF_AMAZON_LINK or STORES within productAds, only 1 adGroup is supported. (optional)

    try:
        # Creates one or more ad groups.
        api_response = api_instance.create_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_ad_group=create_ad_group)
        print("The response of AdGroupsApi->create_ad_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdGroupsApi->create_ad_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **create_ad_group** | [**List[CreateAdGroup]**](CreateAdGroup.md)| An array of AdGroup objects. For each object, specify required fields and their values. Required fields are &#x60;campaignId&#x60;, &#x60;name&#x60;, &#x60;state&#x60;, and &#x60;defaultBid&#x60;. Maximum length of the array is 100 objects. Note - when using landingPageType of OFF_AMAZON_LINK or STORES within productAds, only 1 adGroup is supported. | [optional] 

### Return type

[**List[AdGroupResponse]**](AdGroupResponse.md)

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

# **get_ad_group**
> AdGroup get_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Gets a requested ad group.

Returns an AdGroup object for a requested campaign. Note that the AdGroup object is designed for performance, with a small set of commonly used ad group fields to reduce size. If the extended set of fields is required, use the campaign operations that return the AdGroupResponseEx object.

### Example


```python
import openapi_client
from openapi_client.models.ad_group import AdGroup
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
    api_instance = openapi_client.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 56 # int | The identifier of the requested ad group.

    try:
        # Gets a requested ad group.
        api_response = api_instance.get_ad_group(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        print("The response of AdGroupsApi->get_ad_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdGroupsApi->get_ad_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_group_id** | **int**| The identifier of the requested ad group. | 

### Return type

[**AdGroup**](AdGroup.md)

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

# **get_ad_group_response_ex**
> AdGroupResponseEx get_ad_group_response_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)

Gets extended information for a requested ad group.

### Example


```python
import openapi_client
from openapi_client.models.ad_group_response_ex import AdGroupResponseEx
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
    api_instance = openapi_client.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_group_id = 56 # int | The identifier of the requested ad group.

    try:
        # Gets extended information for a requested ad group.
        api_response = api_instance.get_ad_group_response_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_group_id)
        print("The response of AdGroupsApi->get_ad_group_response_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdGroupsApi->get_ad_group_response_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_group_id** | **int**| The identifier of the requested ad group. | 

### Return type

[**AdGroupResponseEx**](AdGroupResponseEx.md)

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

# **list_ad_groups**
> List[AdGroup] list_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, name=name)

Gets a list of ad groups.

Gets an array of AdGroup objects for a requested set of Sponsored Display ad groups. Note that the AdGroup object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use the ad group operations that return the AdGroupResponseEx object.

### Example


```python
import openapi_client
from openapi_client.models.ad_group import AdGroup
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
    api_instance = openapi_client.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. Sets a cursor into the requested set of campaigns. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional)
    count = 56 # int | Optional. Sets the number of AdGroup objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten ad groups set `startIndex=0` and `count=10`. To return the next ten ad groups, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. The returned array is filtered to include only ad groups with state set to one of the values in the specified comma-delimited list. (optional) (default to enabled, paused, archived)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. The returned array is filtered to include only ad groups associated with the campaign identifiers in the specified comma-delimited list. (optional)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional. The returned array is filtered to include only ad groups with an identifier specified in the comma-delimited list. (optional)
    name = 'name_example' # str | Optional. The returned array includes only ad groups with the specified name. (optional)

    try:
        # Gets a list of ad groups.
        api_response = api_instance.list_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, name=name)
        print("The response of AdGroupsApi->list_ad_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdGroupsApi->list_ad_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of campaigns. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] 
 **count** | **int**| Optional. Sets the number of AdGroup objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten ad groups set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten ad groups, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. The returned array is filtered to include only ad groups with state set to one of the values in the specified comma-delimited list. | [optional] [default to enabled, paused, archived]
 **campaign_id_filter** | **str**| Optional. The returned array is filtered to include only ad groups associated with the campaign identifiers in the specified comma-delimited list. | [optional] 
 **ad_group_id_filter** | **str**| Optional. The returned array is filtered to include only ad groups with an identifier specified in the comma-delimited list. | [optional] 
 **name** | **str**| Optional. The returned array includes only ad groups with the specified name. | [optional] 

### Return type

[**List[AdGroup]**](AdGroup.md)

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

# **list_ad_groups_ex**
> List[AdGroupResponseEx] list_ad_groups_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, name=name)

Gets a list of ad groups with extended fields.

Gets an array of AdGroupResponseEx objects for a set of requested ad groups.

### Example


```python
import openapi_client
from openapi_client.models.ad_group_response_ex import AdGroupResponseEx
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
    api_instance = openapi_client.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. Sets a cursor into the requested set of ad groups. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional)
    count = 56 # int | Optional. Sets the number of Campaign objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten campaigns set `startIndex=0` and `count=10`. To return the next ten campaigns, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. The returned array is filtered to include only campaigns with state set to one of the values in the comma-delimited list. (optional) (default to enabled, paused, archived)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. The returned array is filtered to include only ad groups associated with the campaign identifiers in the comma-delimited list. (optional)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional. The returned array is filtered to include only ad groups with an identifier specified in the comma-delimited list. (optional)
    name = 'name_example' # str | Optional. The returned array includes only ad groups with the specified name. (optional)

    try:
        # Gets a list of ad groups with extended fields.
        api_response = api_instance.list_ad_groups_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, campaign_id_filter=campaign_id_filter, ad_group_id_filter=ad_group_id_filter, name=name)
        print("The response of AdGroupsApi->list_ad_groups_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdGroupsApi->list_ad_groups_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of ad groups. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] 
 **count** | **int**| Optional. Sets the number of Campaign objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten campaigns set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten campaigns, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. The returned array is filtered to include only campaigns with state set to one of the values in the comma-delimited list. | [optional] [default to enabled, paused, archived]
 **campaign_id_filter** | **str**| Optional. The returned array is filtered to include only ad groups associated with the campaign identifiers in the comma-delimited list. | [optional] 
 **ad_group_id_filter** | **str**| Optional. The returned array is filtered to include only ad groups with an identifier specified in the comma-delimited list. | [optional] 
 **name** | **str**| Optional. The returned array includes only ad groups with the specified name. | [optional] 

### Return type

[**List[AdGroupResponseEx]**](AdGroupResponseEx.md)

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

# **update_ad_groups**
> List[AdGroupResponse] update_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_ad_group=update_ad_group)

Updates on or more ad groups.

### Example


```python
import openapi_client
from openapi_client.models.ad_group_response import AdGroupResponse
from openapi_client.models.update_ad_group import UpdateAdGroup
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
    api_instance = openapi_client.AdGroupsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_ad_group = [openapi_client.UpdateAdGroup()] # List[UpdateAdGroup] | An array of AdGroup objects. For each object, specify an ad group identifier and mutable fields with their updated values. The mutable fields are 'name', 'defaultBid', and 'state'. Maximum length of the array is 100 objects. (optional)

    try:
        # Updates on or more ad groups.
        api_response = api_instance.update_ad_groups(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_ad_group=update_ad_group)
        print("The response of AdGroupsApi->update_ad_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdGroupsApi->update_ad_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **update_ad_group** | [**List[UpdateAdGroup]**](UpdateAdGroup.md)| An array of AdGroup objects. For each object, specify an ad group identifier and mutable fields with their updated values. The mutable fields are &#39;name&#39;, &#39;defaultBid&#39;, and &#39;state&#39;. Maximum length of the array is 100 objects. | [optional] 

### Return type

[**List[AdGroupResponse]**](AdGroupResponse.md)

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

