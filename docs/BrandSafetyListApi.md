# openapi_client.BrandSafetyListApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_brand_safety_deny_list_domains**](BrandSafetyListApi.md#create_brand_safety_deny_list_domains) | **POST** /sd/brandSafety/deny | Creates one or more domains to add to a Brand Safety Deny List. 
[**delete_brand_safety_deny_list**](BrandSafetyListApi.md#delete_brand_safety_deny_list) | **DELETE** /sd/brandSafety/deny | Archives all of the domains in the Brand Safety Deny List. 
[**get_request_results**](BrandSafetyListApi.md#get_request_results) | **GET** /sd/brandSafety/{requestId}/results | Gets the results for the given request
[**get_request_status**](BrandSafetyListApi.md#get_request_status) | **GET** /sd/brandSafety/{requestId}/status | Gets the status of the given request
[**list_domains**](BrandSafetyListApi.md#list_domains) | **GET** /sd/brandSafety/deny | Gets a list of websites/apps that are on the advertiser&#39;s Brand Safety Deny List.
[**list_request_status**](BrandSafetyListApi.md#list_request_status) | **GET** /sd/brandSafety/status | List status of all requests


# **create_brand_safety_deny_list_domains**
> BrandSafetyUpdateResponse create_brand_safety_deny_list_domains(amazon_advertising_api_client_id, amazon_advertising_api_scope, brand_safety_post_request)

Creates one or more domains to add to a Brand Safety Deny List. 

Creates one or more domains to add to a Brand Safety Deny List. The Brand Safety Deny List is at the advertiser level. It can take up to 15 minutes from the time a domain is added to the time it is reflected in the deny list. 

### Example


```python
import openapi_client
from openapi_client.models.brand_safety_post_request import BrandSafetyPostRequest
from openapi_client.models.brand_safety_update_response import BrandSafetyUpdateResponse
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
    api_instance = openapi_client.BrandSafetyListApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    brand_safety_post_request = openapi_client.BrandSafetyPostRequest() # BrandSafetyPostRequest | An array of Brand Safety List Domain objects. For each object, specify required fields and their values. Maximum length of the array is 10,000 objects. 

    try:
        # Creates one or more domains to add to a Brand Safety Deny List. 
        api_response = api_instance.create_brand_safety_deny_list_domains(amazon_advertising_api_client_id, amazon_advertising_api_scope, brand_safety_post_request)
        print("The response of BrandSafetyListApi->create_brand_safety_deny_list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandSafetyListApi->create_brand_safety_deny_list_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **brand_safety_post_request** | [**BrandSafetyPostRequest**](BrandSafetyPostRequest.md)| An array of Brand Safety List Domain objects. For each object, specify required fields and their values. Maximum length of the array is 10,000 objects.  | 

### Return type

[**BrandSafetyUpdateResponse**](BrandSafetyUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request has been accepted for processing. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brand_safety_deny_list**
> BrandSafetyUpdateResponse delete_brand_safety_deny_list(amazon_advertising_api_client_id, amazon_advertising_api_scope)

Archives all of the domains in the Brand Safety Deny List. 

Archives all of the domains in the Brand Safety Deny List. It can take several hours from the time a domain is deleted to the time it is reflected in the deny list. You can check the status of the delete request by calling GET /sd/brandSafety/{requestId}/status. If the status is \"COMPLETED\", you can call GET /sd/brandSafety/deny to validate that your deny list has been successfully deleted. 

### Example


```python
import openapi_client
from openapi_client.models.brand_safety_update_response import BrandSafetyUpdateResponse
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
    api_instance = openapi_client.BrandSafetyListApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.

    try:
        # Archives all of the domains in the Brand Safety Deny List. 
        api_response = api_instance.delete_brand_safety_deny_list(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        print("The response of BrandSafetyListApi->delete_brand_safety_deny_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandSafetyListApi->delete_brand_safety_deny_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 

### Return type

[**BrandSafetyUpdateResponse**](BrandSafetyUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request has been accepted for processing. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_results**
> BrandSafetyRequestResultsResponse get_request_results(amazon_advertising_api_client_id, amazon_advertising_api_scope, request_id, start_index=start_index, count=count)

Gets the results for the given request

When a user adds domains to their Brand Safety Deny List, the request is processed asynchronously, and a requestId is provided to the user. This requestId can be used to view the request results for up to 90 days from when the request was submitted. The results provide the status of each domain in the given request. Request results may contain multiple pages. This endpoint will only be available once the request has completed processing. To see the status of the request you can call GET /sd/brandSafety/{requestId}/status. Note that this endpoint only lists the results of POST requests to /sd/brandSafety/deny - it does not reflect the results of DELETE requests. 

### Example


```python
import openapi_client
from openapi_client.models.brand_safety_request_results_response import BrandSafetyRequestResultsResponse
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
    api_instance = openapi_client.BrandSafetyListApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    request_id = 'request_id_example' # str | The ID of the request previously submitted.
    start_index = 56 # int | Optional. Sets a cursor into the requested set of results. Use in conjunction with the count parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.  (optional)
    count = 56 # int | Optional. Sets the number of results in the returned array. Use in conjunction with the startIndex parameter to control pagination. For example, to return the first 1000 results set startIndex=0 and count=1000. To return the next 1000 results, set startIndex=1000 and count=1000, and so on. Defaults to max page size(1000).  (optional)

    try:
        # Gets the results for the given request
        api_response = api_instance.get_request_results(amazon_advertising_api_client_id, amazon_advertising_api_scope, request_id, start_index=start_index, count=count)
        print("The response of BrandSafetyListApi->get_request_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandSafetyListApi->get_request_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **request_id** | **str**| The ID of the request previously submitted. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of results. Use in conjunction with the count parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.  | [optional] 
 **count** | **int**| Optional. Sets the number of results in the returned array. Use in conjunction with the startIndex parameter to control pagination. For example, to return the first 1000 results set startIndex&#x3D;0 and count&#x3D;1000. To return the next 1000 results, set startIndex&#x3D;1000 and count&#x3D;1000, and so on. Defaults to max page size(1000).  | [optional] 

### Return type

[**BrandSafetyRequestResultsResponse**](BrandSafetyRequestResultsResponse.md)

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

# **get_request_status**
> BrandSafetyRequestStatusResponse get_request_status(amazon_advertising_api_client_id, amazon_advertising_api_scope, request_id)

Gets the status of the given request

When a user modifies their Brand Safety Deny List, the request is processed asynchronously, and a requestId is provided to the user. This requestId can be used to check the status of the request for up to 90 days from when the request was submitted. 

### Example


```python
import openapi_client
from openapi_client.models.brand_safety_request_status_response import BrandSafetyRequestStatusResponse
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
    api_instance = openapi_client.BrandSafetyListApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    request_id = 'request_id_example' # str | The ID of the request previously submitted.

    try:
        # Gets the status of the given request
        api_response = api_instance.get_request_status(amazon_advertising_api_client_id, amazon_advertising_api_scope, request_id)
        print("The response of BrandSafetyListApi->get_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandSafetyListApi->get_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **request_id** | **str**| The ID of the request previously submitted. | 

### Return type

[**BrandSafetyRequestStatusResponse**](BrandSafetyRequestStatusResponse.md)

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

# **list_domains**
> BrandSafetyGetResponse list_domains(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count)

Gets a list of websites/apps that are on the advertiser's Brand Safety Deny List.

Gets an array of websites/apps that are on the advertiser's Brand Safety Deny List. It can take up to 15 minutes from the time a domain is added/deleted to the time it is reflected in the deny list.

### Example


```python
import openapi_client
from openapi_client.models.brand_safety_get_response import BrandSafetyGetResponse
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
    api_instance = openapi_client.BrandSafetyListApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. Sets a cursor into the requested set of domains. Use in conjunction with the count parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.  (optional)
    count = 56 # int | Optional. Sets the number of domain objects in the returned array. Use in conjunction with the startIndex parameter to control pagination. For example, to return the first 1000 domains set startIndex=0 and count=1000. To return the next 1000 domains, set startIndex=1000 and count=1000, and so on. Defaults to max page size(1000).  (optional)

    try:
        # Gets a list of websites/apps that are on the advertiser's Brand Safety Deny List.
        api_response = api_instance.list_domains(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count)
        print("The response of BrandSafetyListApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandSafetyListApi->list_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of domains. Use in conjunction with the count parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.  | [optional] 
 **count** | **int**| Optional. Sets the number of domain objects in the returned array. Use in conjunction with the startIndex parameter to control pagination. For example, to return the first 1000 domains set startIndex&#x3D;0 and count&#x3D;1000. To return the next 1000 domains, set startIndex&#x3D;1000 and count&#x3D;1000, and so on. Defaults to max page size(1000).  | [optional] 

### Return type

[**BrandSafetyGetResponse**](BrandSafetyGetResponse.md)

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

# **list_request_status**
> BrandSafetyListRequestStatusResponse list_request_status(amazon_advertising_api_client_id, amazon_advertising_api_scope)

List status of all requests

List status of all Brand Safety List requests. The list will contain requests that were submitted in the past 90 days. 

### Example


```python
import openapi_client
from openapi_client.models.brand_safety_list_request_status_response import BrandSafetyListRequestStatusResponse
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
    api_instance = openapi_client.BrandSafetyListApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.

    try:
        # List status of all requests
        api_response = api_instance.list_request_status(amazon_advertising_api_client_id, amazon_advertising_api_scope)
        print("The response of BrandSafetyListApi->list_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandSafetyListApi->list_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 

### Return type

[**BrandSafetyListRequestStatusResponse**](BrandSafetyListRequestStatusResponse.md)

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

