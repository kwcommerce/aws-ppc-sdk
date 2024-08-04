# openapi_client.SnapshotsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot**](SnapshotsApi.md#create_snapshot) | **POST** /sd/{recordType}/snapshot | Request a file-based snapshot of all entities of the specified type in the account satisfying the filtering criteria
[**download_snapshot**](SnapshotsApi.md#download_snapshot) | **GET** /sd/snapshots/{snapshotId}/download | Download previously requested snapshot
[**get_snapshot**](SnapshotsApi.md#get_snapshot) | **GET** /sd/snapshots/{snapshotId} | Retrieve status, metadata, and location of previously requested snapshot


# **create_snapshot**
> SnapshotResponse create_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type, snapshot_request=snapshot_request)

Request a file-based snapshot of all entities of the specified type in the account satisfying the filtering criteria

**Note: Snapshots APIs are deprecated and will be shut off on October 15, 2024. For replacement functionality, see the [exports](guides/exports/overview) API. To learn more, view the [migration guide](reference/migration-guides/snapshots-exports).**  To understand the call flow for asynchronous snapshots, see [Getting started with sponsored ads snapshots](/API/docs/en-us/guides/snapshots/get-started).

### Example


```python
import openapi_client
from openapi_client.models.snapshot_request import SnapshotRequest
from openapi_client.models.snapshot_response import SnapshotResponse
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
    api_instance = openapi_client.SnapshotsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    record_type = 'record_type_example' # str | **Note: Snapshots APIs are deprecated and will be shut off on October 15, 2024. For replacement functionality, see the [exports](guides/exports/overview) API. To learn more, view the [migration guide](reference/migration-guides/snapshots-exports).**  The type of entity for which the snapshot should be generated. Must be one of: `campaigns`, `adgroups`, `productAds`, or `targets`.
    snapshot_request = openapi_client.SnapshotRequest() # SnapshotRequest | Request a snapshot file for all entities of a single record type. (optional)

    try:
        # Request a file-based snapshot of all entities of the specified type in the account satisfying the filtering criteria
        api_response = api_instance.create_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type, snapshot_request=snapshot_request)
        print("The response of SnapshotsApi->create_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **record_type** | **str**| **Note: Snapshots APIs are deprecated and will be shut off on October 15, 2024. For replacement functionality, see the [exports](guides/exports/overview) API. To learn more, view the [migration guide](reference/migration-guides/snapshots-exports).**  The type of entity for which the snapshot should be generated. Must be one of: &#x60;campaigns&#x60;, &#x60;adgroups&#x60;, &#x60;productAds&#x60;, or &#x60;targets&#x60;. | 
 **snapshot_request** | [**SnapshotRequest**](SnapshotRequest.md)| Request a snapshot file for all entities of a single record type. | [optional] 

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_snapshot**
> download_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, snapshot_id)

Download previously requested snapshot

**Note: Snapshots APIs are deprecated and will be shut off on October 15, 2024. For replacement functionality, see the [exports](guides/exports/overview) API. To learn more, view the [migration guide](reference/migration-guides/snapshots-exports).**   To understand the call flow for asynchronous snapshots, see [Getting started with sponsored ads snapshots](/API/docs/en-us/guides/snapshots/overview).

### Example


```python
import openapi_client
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
    api_instance = openapi_client.SnapshotsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    snapshot_id = 'snapshot_id_example' # str | The Snapshot identifier.

    try:
        # Download previously requested snapshot
        api_instance.download_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, snapshot_id)
    except Exception as e:
        print("Exception when calling SnapshotsApi->download_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **snapshot_id** | **str**| The Snapshot identifier. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**307** | Successful operation. |  * Location - Redirect URI with S3 file location containing snapshot data <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**404** | Not Found - Requested resource does not exist or is not visible for the authenticated user. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot**
> SnapshotResponse get_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, snapshot_id)

Retrieve status, metadata, and location of previously requested snapshot

**Note: Snapshots APIs are deprecated and will be shut off on October 15, 2024. For replacement functionality, see the [exports](guides/exports/overview) API. To learn more, view the [migration guide](reference/migration-guides/snapshots-exports).**   To understand the call flow for asynchronous snapshots, see [Getting started with sponsored ads snapshots](/API/docs/en-us/guides/snapshots/get-started).

### Example


```python
import openapi_client
from openapi_client.models.snapshot_response import SnapshotResponse
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
    api_instance = openapi_client.SnapshotsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    snapshot_id = 'snapshot_id_example' # str | The Snapshot identifier.

    try:
        # Retrieve status, metadata, and location of previously requested snapshot
        api_response = api_instance.get_snapshot(amazon_advertising_api_client_id, amazon_advertising_api_scope, snapshot_id)
        print("The response of SnapshotsApi->get_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **snapshot_id** | **str**| The Snapshot identifier. | 

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified   resource |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

