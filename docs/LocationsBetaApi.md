# openapi_client.LocationsBetaApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_locations**](LocationsBetaApi.md#archive_locations) | **POST** /sd/locations/delete | Sets the &#x60;state&#x60; of each Location clause given to &#x60;archived&#x60;.
[**create_locations**](LocationsBetaApi.md#create_locations) | **POST** /sd/locations | Creates one or more locations associated with an ad group.
[**list_locations**](LocationsBetaApi.md#list_locations) | **GET** /sd/locations | Gets a list of locations associated with ad groups.


# **archive_locations**
> List[ArchiveLocationResponse] archive_locations(amazon_advertising_api_client_id, amazon_advertising_api_scope, archive_location_request)

Sets the `state` of each Location clause given to `archived`.

This is a bulk operation that accepts up to a limit of 1000 Location Expression Ids at a time. This deletion operation is equivalent to using the `updateTargetingClauses` operation to set the `state` property of a Location clause to `archived`.

### Example


```python
import openapi_client
from openapi_client.models.archive_location_request import ArchiveLocationRequest
from openapi_client.models.archive_location_response import ArchiveLocationResponse
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
    api_instance = openapi_client.LocationsBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    archive_location_request = openapi_client.ArchiveLocationRequest() # ArchiveLocationRequest | A list of up to 1000 Location Expression Ids for archival.

    try:
        # Sets the `state` of each Location clause given to `archived`.
        api_response = api_instance.archive_locations(amazon_advertising_api_client_id, amazon_advertising_api_scope, archive_location_request)
        print("The response of LocationsBetaApi->archive_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsBetaApi->archive_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **archive_location_request** | [**ArchiveLocationRequest**](ArchiveLocationRequest.md)| A list of up to 1000 Location Expression Ids for archival. | 

### Return type

[**List[ArchiveLocationResponse]**](ArchiveLocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, a-pplication/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | An array response containing a response for each Location Expression |  -  |
**400** | Bad Request - Request failed because payload is empty, includes invalid types, or exceeds batch limit. |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_locations**
> List[Location] create_locations(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_location=create_location)

Creates one or more locations associated with an ad group.

This resource is not available when productAds have ASIN or SKU fields and only available for advertisers that do not sell products on Amazon.   See [Developer Guide](https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/non-amazon-sellers/get-started)  Locations optimize Ad Groups for delivery to users that have an association with those locations. For example, an Ad Group might contain the following:  - A Targeting Clause representing an audience of users that viewed a shoe  - A Location representing Seattle, Washington, USA. - A Location representing New York, New York, USA. In this case, delivery of the Targeting Clause will be optimized for New York and Seattle.   You can discover predefined Locations to use in your ad group by calling the GET /locations API. The table below lists  several example Locations. | Location | Description | |---------------------------|-------------| | location=amzn1.ad-geo.XHvCjcKHXsKUwos= | Optimize the ad group for the specified location (either a 'city', 'state', 'dma', 'postal code', or 'country').|  Using locations is optional. 

### Example


```python
import openapi_client
from openapi_client.models.create_location import CreateLocation
from openapi_client.models.location import Location
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
    api_instance = openapi_client.LocationsBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_location = [openapi_client.CreateLocation()] # List[CreateLocation] | A list of up to 100 Locations for creation for each call.  1000 locations can be added for each ad group. (optional)

    try:
        # Creates one or more locations associated with an ad group.
        api_response = api_instance.create_locations(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_location=create_location)
        print("The response of LocationsBetaApi->create_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsBetaApi->create_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **create_location** | [**List[CreateLocation]**](CreateLocation.md)| A list of up to 100 Locations for creation for each call.  1000 locations can be added for each ad group. | [optional] 

### Return type

[**List[Location]**](Location.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, a-pplication/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Locations. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**422** | Unprocessable Entity - Request was understood, but contained invalid parameters |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_locations**
> List[Location] list_locations(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)

Gets a list of locations associated with ad groups.

Gets a list of Sponsored Display Location objects. This resource is not available when productAds have ASIN or SKU fields and only available for advertisers that do not sell products on Amazon. See [Developer Guide](https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/non-amazon-sellers/get-started)

### Example


```python
import openapi_client
from openapi_client.models.location import Location
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
    api_instance = openapi_client.LocationsBetaApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. 0-indexed record offset for the result set. Defaults to 0. (optional)
    count = 56 # int | Optional. Number of records to include in the paged response. Defaults to max page size. (optional)
    state_filter = enabled # str | Optional. Restricts results to those with state within the specified comma-separated list. Must be one of: `enabled`. (optional) (default to enabled)
    ad_group_id_filter = 'ad_group_id_filter_example' # str | Optional list of comma separated adGroupIds. Restricts results to locations with the specified `adGroupId`. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional list of comma separated campaignIds. Restricts results to locations with the specified `campaignId`. (optional)

    try:
        # Gets a list of locations associated with ad groups.
        api_response = api_instance.list_locations(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, ad_group_id_filter=ad_group_id_filter, campaign_id_filter=campaign_id_filter)
        print("The response of LocationsBetaApi->list_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsBetaApi->list_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. 0-indexed record offset for the result set. Defaults to 0. | [optional] 
 **count** | **int**| Optional. Number of records to include in the paged response. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. Restricts results to those with state within the specified comma-separated list. Must be one of: &#x60;enabled&#x60;. | [optional] [default to enabled]
 **ad_group_id_filter** | **str**| Optional list of comma separated adGroupIds. Restricts results to locations with the specified &#x60;adGroupId&#x60;. | [optional] 
 **campaign_id_filter** | **str**| Optional list of comma separated campaignIds. Restricts results to locations with the specified &#x60;campaignId&#x60;. | [optional] 

### Return type

[**List[Location]**](Location.md)

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

