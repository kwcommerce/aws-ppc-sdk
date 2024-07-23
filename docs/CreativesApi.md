# openapi_client.CreativesApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_creatives**](CreativesApi.md#create_creatives) | **POST** /sd/creatives | A POST request of one or more creatives.
[**list_creative_moderations**](CreativesApi.md#list_creative_moderations) | **GET** /sd/moderation/creatives | Gets a list of creative moderations
[**list_creatives**](CreativesApi.md#list_creatives) | **GET** /sd/creatives | Gets a list of creatives
[**post_creative_preview**](CreativesApi.md#post_creative_preview) | **POST** /sd/creatives/preview | Gets creative preview HTML.
[**update_creatives**](CreativesApi.md#update_creatives) | **PUT** /sd/creatives | Updates one or more creatives.


# **create_creatives**
> List[CreativeResponse] create_creatives(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_creative=create_creative)

A POST request of one or more creatives.



### Example


```python
import openapi_client
from openapi_client.models.create_creative import CreateCreative
from openapi_client.models.creative_response import CreativeResponse
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
    api_instance = openapi_client.CreativesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_creative = [openapi_client.CreateCreative()] # List[CreateCreative] | An array of Creative objects to create. Maximum length of the array is 100 objects. Note - when using productAds with landingPageUrl of OFF_AMAZON_LINK, STORE, or MOMENT, the following properties are required all together; 1) headline, 2) brandLogo, and 3) rectCustomImage, squareCustomImage. (optional)

    try:
        # A POST request of one or more creatives.
        api_response = api_instance.create_creatives(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_creative=create_creative)
        print("The response of CreativesApi->create_creatives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativesApi->create_creatives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **create_creative** | [**List[CreateCreative]**](CreateCreative.md)| An array of Creative objects to create. Maximum length of the array is 100 objects. Note - when using productAds with landingPageUrl of OFF_AMAZON_LINK, STORE, or MOMENT, the following properties are required all together; 1) headline, 2) brandLogo, and 3) rectCustomImage, squareCustomImage. | [optional] 

### Return type

[**List[CreativeResponse]**](CreativeResponse.md)

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
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_creative_moderations**
> List[CreativeModeration] list_creative_moderations(amazon_advertising_api_client_id, amazon_advertising_api_scope, language, start_index=start_index, count=count, ad_group_id_filter=ad_group_id_filter, creative_id_filter=creative_id_filter)

Gets a list of creative moderations



### Example


```python
import openapi_client
from openapi_client.models.creative_moderation import CreativeModeration
from openapi_client.models.locale import Locale
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
    api_instance = openapi_client.CreativesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    language = openapi_client.Locale() # Locale | The language of the returned creative moderation metadata.
    start_index = 0 # int | Sets a cursor into the requested set of creative moderations. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional) (default to 0)
    count = 100 # int | Sets the number of creative objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten creative moderations set `startIndex=0` and `count=10`. To return the next ten creative moderations, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional) (default to 100)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | The returned array includes only creative moderations associated with ad group identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `creativeIdFilter` parameter. (optional)
    creative_id_filter = 'creative_id_filter_example' # str | The returned array includes only creative moderations with creative identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `adGroupIdFilter` parameter. (optional)

    try:
        # Gets a list of creative moderations
        api_response = api_instance.list_creative_moderations(amazon_advertising_api_client_id, amazon_advertising_api_scope, language, start_index=start_index, count=count, ad_group_id_filter=ad_group_id_filter, creative_id_filter=creative_id_filter)
        print("The response of CreativesApi->list_creative_moderations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativesApi->list_creative_moderations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **language** | [**Locale**](.md)| The language of the returned creative moderation metadata. | 
 **start_index** | **int**| Sets a cursor into the requested set of creative moderations. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] [default to 0]
 **count** | **int**| Sets the number of creative objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten creative moderations set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten creative moderations, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] [default to 100]
 **ad_group_id_filter** | **str**| The returned array includes only creative moderations associated with ad group identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the &#x60;creativeIdFilter&#x60; parameter. | [optional] 
 **creative_id_filter** | **str**| The returned array includes only creative moderations with creative identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the &#x60;adGroupIdFilter&#x60; parameter. | [optional] 

### Return type

[**List[CreativeModeration]**](CreativeModeration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_creatives**
> List[Creative] list_creatives(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, ad_group_id_filter=ad_group_id_filter, creative_id_filter=creative_id_filter)

Gets a list of creatives



### Example


```python
import openapi_client
from openapi_client.models.creative import Creative
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
    api_instance = openapi_client.CreativesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # int | Sets a cursor into the requested set of creatives. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional) (default to 0)
    count = 100 # int | Sets the number of creative objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten creatives set `startIndex=0` and `count=10`. To return the next ten creatives, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional) (default to 100)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | The returned array includes only creatives associated with ad group identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `creativeIdFilter` parameter. (optional)
    creative_id_filter = 'creative_id_filter_example' # str | The returned array includes only creatives with identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the `adGroupIdFilter` parameter. (optional)

    try:
        # Gets a list of creatives
        api_response = api_instance.list_creatives(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, ad_group_id_filter=ad_group_id_filter, creative_id_filter=creative_id_filter)
        print("The response of CreativesApi->list_creatives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativesApi->list_creatives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Sets a cursor into the requested set of creatives. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] [default to 0]
 **count** | **int**| Sets the number of creative objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten creatives set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten creatives, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] [default to 100]
 **ad_group_id_filter** | **str**| The returned array includes only creatives associated with ad group identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the &#x60;creativeIdFilter&#x60; parameter. | [optional] 
 **creative_id_filter** | **str**| The returned array includes only creatives with identifiers matching those specified in the comma-delimited string. Cannot be used in conjunction with the &#x60;adGroupIdFilter&#x60; parameter. | [optional] 

### Return type

[**List[Creative]**](Creative.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_creative_preview**
> CreativePreviewResponse post_creative_preview(amazon_advertising_api_client_id, amazon_advertising_api_scope, creative_preview_request=creative_preview_request)

Gets creative preview HTML.



### Example


```python
import openapi_client
from openapi_client.models.creative_preview_request import CreativePreviewRequest
from openapi_client.models.creative_preview_response import CreativePreviewResponse
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
    api_instance = openapi_client.CreativesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    creative_preview_request = openapi_client.CreativePreviewRequest() # CreativePreviewRequest |  (optional)

    try:
        # Gets creative preview HTML.
        api_response = api_instance.post_creative_preview(amazon_advertising_api_client_id, amazon_advertising_api_scope, creative_preview_request=creative_preview_request)
        print("The response of CreativesApi->post_creative_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativesApi->post_creative_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **creative_preview_request** | [**CreativePreviewRequest**](CreativePreviewRequest.md)|  | [optional] 

### Return type

[**CreativePreviewResponse**](CreativePreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_creatives**
> List[CreativeResponse] update_creatives(amazon_advertising_api_client_id, amazon_advertising_api_scope, creative_update=creative_update)

Updates one or more creatives.



### Example


```python
import openapi_client
from openapi_client.models.creative_response import CreativeResponse
from openapi_client.models.creative_update import CreativeUpdate
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
    api_instance = openapi_client.CreativesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    creative_update = [openapi_client.CreativeUpdate()] # List[CreativeUpdate] | An array of creative objects to update. Maximum length of the array is 100 objects. (optional)

    try:
        # Updates one or more creatives.
        api_response = api_instance.update_creatives(amazon_advertising_api_client_id, amazon_advertising_api_scope, creative_update=creative_update)
        print("The response of CreativesApi->update_creatives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreativesApi->update_creatives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **creative_update** | [**List[CreativeUpdate]**](CreativeUpdate.md)| An array of creative objects to update. Maximum length of the array is 100 objects. | [optional] 

### Return type

[**List[CreativeResponse]**](CreativeResponse.md)

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
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

