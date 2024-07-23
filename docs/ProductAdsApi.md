# openapi_client.ProductAdsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_product_ad**](ProductAdsApi.md#archive_product_ad) | **DELETE** /sd/productAds/{adId} | Sets the status of a sproduct ad to archived.
[**create_product_ads**](ProductAdsApi.md#create_product_ads) | **POST** /sd/productAds | Creates one or more product ads.
[**get_product_ad**](ProductAdsApi.md#get_product_ad) | **GET** /sd/productAds/{adId} | Gets a requested product ad.
[**get_product_ad_response_ex**](ProductAdsApi.md#get_product_ad_response_ex) | **GET** /sd/productAds/extended/{adId} | Gets extended information for a product ad.
[**list_product_ads**](ProductAdsApi.md#list_product_ads) | **GET** /sd/productAds | Gets a list of product ads.
[**list_product_ads_ex**](ProductAdsApi.md#list_product_ads_ex) | **GET** /sd/productAds/extended | Gets a list of product ads with extended fields.
[**update_product_ads**](ProductAdsApi.md#update_product_ads) | **PUT** /sd/productAds | Updates one or more product ads.


# **archive_product_ad**
> ProductAdResponse archive_product_ad(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)

Sets the status of a sproduct ad to archived.

This operation is equivalent to an update operation that sets the status field to 'archived'. Note that setting the status field to 'archived' is permanent and can't be undone. See [Developer Notes](https://advertising.amazon.com/API/docs/en-us/info/developer-notes#archiving) for more information.

### Example


```python
import openapi_client
from openapi_client.models.product_ad_response import ProductAdResponse
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
    api_instance = openapi_client.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_id = 56 # int | The identifier of the produce ad.

    try:
        # Sets the status of a sproduct ad to archived.
        api_response = api_instance.archive_product_ad(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)
        print("The response of ProductAdsApi->archive_product_ad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAdsApi->archive_product_ad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_id** | **int**| The identifier of the produce ad. | 

### Return type

[**ProductAdResponse**](ProductAdResponse.md)

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

# **create_product_ads**
> List[ProductAdResponse] create_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_product_ad=create_product_ad)

Creates one or more product ads.

### Example


```python
import openapi_client
from openapi_client.models.create_product_ad import CreateProductAd
from openapi_client.models.product_ad_response import ProductAdResponse
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
    api_instance = openapi_client.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_product_ad = [{state=enabled, adGroupId=0, campaignId=0, asin=B081FGSWTJ}] # List[CreateProductAd] | An array of ProductAd objects. For each object, specify required fields and their values. Required fields are `adGroupId` and `state`. Within any campaign, you must pass consistent fields of either `asin` (for vendors), `sku` (for sellers), or `landingPageUrl` (when linking to other pages), these cannot be mixed for any given campaign. Maximum length of the array is 100 objects. (optional)

    try:
        # Creates one or more product ads.
        api_response = api_instance.create_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_product_ad=create_product_ad)
        print("The response of ProductAdsApi->create_product_ads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAdsApi->create_product_ads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **create_product_ad** | [**List[CreateProductAd]**](CreateProductAd.md)| An array of ProductAd objects. For each object, specify required fields and their values. Required fields are &#x60;adGroupId&#x60; and &#x60;state&#x60;. Within any campaign, you must pass consistent fields of either &#x60;asin&#x60; (for vendors), &#x60;sku&#x60; (for sellers), or &#x60;landingPageUrl&#x60; (when linking to other pages), these cannot be mixed for any given campaign. Maximum length of the array is 100 objects. | [optional] 

### Return type

[**List[ProductAdResponse]**](ProductAdResponse.md)

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

# **get_product_ad**
> ProductAd get_product_ad(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)

Gets a requested product ad.

Note that the ProductAd object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use a product ad operations that returns the ProductAdResponseEx object.

### Example


```python
import openapi_client
from openapi_client.models.product_ad import ProductAd
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
    api_instance = openapi_client.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_id = 56 # int | The identifier of the requested product ad.

    try:
        # Gets a requested product ad.
        api_response = api_instance.get_product_ad(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)
        print("The response of ProductAdsApi->get_product_ad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAdsApi->get_product_ad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_id** | **int**| The identifier of the requested product ad. | 

### Return type

[**ProductAd**](ProductAd.md)

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

# **get_product_ad_response_ex**
> ProductAdResponseEx get_product_ad_response_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)

Gets extended information for a product ad.

### Example


```python
import openapi_client
from openapi_client.models.product_ad_response_ex import ProductAdResponseEx
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
    api_instance = openapi_client.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    ad_id = 56 # int | The identifier of the requested product ad.

    try:
        # Gets extended information for a product ad.
        api_response = api_instance.get_product_ad_response_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, ad_id)
        print("The response of ProductAdsApi->get_product_ad_response_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAdsApi->get_product_ad_response_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **ad_id** | **int**| The identifier of the requested product ad. | 

### Return type

[**ProductAdResponseEx**](ProductAdResponseEx.md)

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

# **list_product_ads**
> List[ProductAd] list_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_id_filter=ad_id_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)

Gets a list of product ads.

Gets an array of ProductAd objects for a requested set of Sponsored Display product ads. Note that the ProductAd object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use a product ad operation that returns the ProductAdResponseEx object.

### Example


```python
import openapi_client
from openapi_client.models.product_ad import ProductAd
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
    api_instance = openapi_client.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. Sets a cursor into the requested set of product ads. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional)
    count = 56 # int | Optional. Sets the number of ProductAd objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten product ad set `startIndex=0` and `count=10`. To return the next ten product ads, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. The returned array is filtered to include only products ads associated with campaigns that have state set to one of the values in the comma-delimited list. (optional) (default to enabled, paused, archived)
    ad_id_filter = 'ad_id_filter_example' # str | Optional. The returned array includes only product ads with identifiers matching those in the comma-delimited string. (optional)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional. The returned array is filtered to include only products ads associated with ad groups identifiers in the comma-delimited list. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. The returned array is filtered to include only product ads associated with the campaign identifiers in the comma-delimited list. (optional)

    try:
        # Gets a list of product ads.
        api_response = api_instance.list_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_id_filter=ad_id_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)
        print("The response of ProductAdsApi->list_product_ads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAdsApi->list_product_ads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of product ads. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] 
 **count** | **int**| Optional. Sets the number of ProductAd objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten product ad set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten product ads, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. The returned array is filtered to include only products ads associated with campaigns that have state set to one of the values in the comma-delimited list. | [optional] [default to enabled, paused, archived]
 **ad_id_filter** | **str**| Optional. The returned array includes only product ads with identifiers matching those in the comma-delimited string. | [optional] 
 **ad_group_id_filter** | **str**| Optional. The returned array is filtered to include only products ads associated with ad groups identifiers in the comma-delimited list. | [optional] 
 **campaign_id_filter** | **str**| Optional. The returned array is filtered to include only product ads associated with the campaign identifiers in the comma-delimited list. | [optional] 

### Return type

[**List[ProductAd]**](ProductAd.md)

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

# **list_product_ads_ex**
> List[ProductAdResponseEx] list_product_ads_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_id_filter=ad_id_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)

Gets a list of product ads with extended fields.

Gets an array of ProductAdResponseEx objects for a set of requested ad groups. The ProductAdResponseEx object includes the extended set of available fields.

### Example


```python
import openapi_client
from openapi_client.models.product_ad_response_ex import ProductAdResponseEx
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
    api_instance = openapi_client.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. Sets a cursor into the requested set of product ads. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional)
    count = 56 # int | Optional. Sets the number of ProduceAdEx objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten product ads set `startIndex=0` and `count=10`. To return the next ten campaigns, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. The returned array is filtered to include only campaigns with state set to one of the values in the specified comma-delimited list. (optional) (default to enabled, paused, archived)
    ad_id_filter = 'ad_id_filter_example' # str | Optional. The returned array includes only product ads with identifiers matching those in the comma-delimited string. (optional)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional. The returned array is filtered to include only products ads associated with ad groups identifiers in the comma-delimited list. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. The returned array is filtered to include only product ads associated with the campaign identifiers in the comma-delimited list. (optional)

    try:
        # Gets a list of product ads with extended fields.
        api_response = api_instance.list_product_ads_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_id_filter=ad_id_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)
        print("The response of ProductAdsApi->list_product_ads_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAdsApi->list_product_ads_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of product ads. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] 
 **count** | **int**| Optional. Sets the number of ProduceAdEx objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten product ads set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten campaigns, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. The returned array is filtered to include only campaigns with state set to one of the values in the specified comma-delimited list. | [optional] [default to enabled, paused, archived]
 **ad_id_filter** | **str**| Optional. The returned array includes only product ads with identifiers matching those in the comma-delimited string. | [optional] 
 **ad_group_id_filter** | **str**| Optional. The returned array is filtered to include only products ads associated with ad groups identifiers in the comma-delimited list. | [optional] 
 **campaign_id_filter** | **str**| Optional. The returned array is filtered to include only product ads associated with the campaign identifiers in the comma-delimited list. | [optional] 

### Return type

[**List[ProductAdResponseEx]**](ProductAdResponseEx.md)

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

# **update_product_ads**
> List[ProductAdResponse] update_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_product_ad=update_product_ad)

Updates one or more product ads.

### Example


```python
import openapi_client
from openapi_client.models.product_ad_response import ProductAdResponse
from openapi_client.models.update_product_ad import UpdateProductAd
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
    api_instance = openapi_client.ProductAdsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_product_ad = [openapi_client.UpdateProductAd()] # List[UpdateProductAd] | An array of ProductAd objects. For each object, specify a product ad identifier and the only mutable field, `state`. Maximum length of the array is 100 objects. (optional)

    try:
        # Updates one or more product ads.
        api_response = api_instance.update_product_ads(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_product_ad=update_product_ad)
        print("The response of ProductAdsApi->update_product_ads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAdsApi->update_product_ads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **update_product_ad** | [**List[UpdateProductAd]**](UpdateProductAd.md)| An array of ProductAd objects. For each object, specify a product ad identifier and the only mutable field, &#x60;state&#x60;. Maximum length of the array is 100 objects. | [optional] 

### Return type

[**List[ProductAdResponse]**](ProductAdResponse.md)

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

