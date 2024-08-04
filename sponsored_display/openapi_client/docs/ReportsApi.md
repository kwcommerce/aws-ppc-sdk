# openapi_client.ReportsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_report**](ReportsApi.md#download_report) | **GET** /v2/reports/{reportId}/download | Downloads a previously requested report identified by reportId.
[**get_report_status**](ReportsApi.md#get_report_status) | **GET** /v2/reports/{reportId} | Gets the status of a report previously requested.
[**request_report**](ReportsApi.md#request_report) | **POST** /sd/{recordType}/report | Creates a report request.


# **download_report**
> download_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, report_id)

Downloads a previously requested report identified by reportId.

Gets a `307 Temporary Redirect` response that includes a `location` header with the value set to an AWS S3 path where the report is located. The path expires after 30 seconds. If the path expires before the report is downloaded, a new report request must be created.  **To understand the call flow for asynchronous reports, see [Getting started with sponsored ads reports](/API/docs/en-us/guides/reporting/v2/sponsored-ads-reports).**

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
    api_instance = openapi_client.ReportsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    report_id = 'report_id_example' # str | The identifier of the requested report.

    try:
        # Downloads a previously requested report identified by reportId.
        api_instance.download_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, report_id)
    except Exception as e:
        print("Exception when calling ReportsApi->download_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **report_id** | **str**| The identifier of the requested report. | 

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

# **get_report_status**
> ReportResponse get_report_status(amazon_advertising_api_client_id, amazon_advertising_api_scope, report_id)

Gets the status of a report previously requested.

Uses the `reportId` value from the response of a report previously requested via `POST` method of the `/sd/{recordType}/report` operation.  **To understand the call flow for asynchronous reports, see [Getting started with sponsored ads reports](/API/docs/en-us/guides/reporting/v2/sponsored-ads-reports).**

### Example


```python
import openapi_client
from openapi_client.models.report_response import ReportResponse
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
    api_instance = openapi_client.ReportsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    report_id = 'report_id_example' # str | The identifier of the requested report.

    try:
        # Gets the status of a report previously requested.
        api_response = api_instance.get_report_status(amazon_advertising_api_client_id, amazon_advertising_api_scope, report_id)
        print("The response of ReportsApi->get_report_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_report_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **report_id** | **str**| The identifier of the requested report. | 

### Return type

[**ReportResponse**](ReportResponse.md)

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

# **request_report**
> ReportResponse request_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type, report_request=report_request)

Creates a report request.

**To understand the call flow for asynchronous reports, see [Getting started with sponsored ads reports](/API/docs/en-us/guides/reporting/v2/sponsored-ads-reports).**  The Sponsored Display API supports creation of reports for campaigns, ad groups, product ads, targets, and asins. Create a ReportRequest object specifying the fields corresponding to performance data metrics to include in the report.

### Example


```python
import openapi_client
from openapi_client.models.report_request import ReportRequest
from openapi_client.models.report_response import ReportResponse
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
    api_instance = openapi_client.ReportsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    record_type = 'record_type_example' # str | The type of report to generate, either `campaigns`, `adGroups`, `productAds`, `targets`, or `asins`. The 'asins' report, also known as the Purchased products report, is only available for seller brand owners.
    report_request = openapi_client.ReportRequest() # ReportRequest |  (optional)

    try:
        # Creates a report request.
        api_response = api_instance.request_report(amazon_advertising_api_client_id, amazon_advertising_api_scope, record_type, report_request=report_request)
        print("The response of ReportsApi->request_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->request_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **record_type** | **str**| The type of report to generate, either &#x60;campaigns&#x60;, &#x60;adGroups&#x60;, &#x60;productAds&#x60;, &#x60;targets&#x60;, or &#x60;asins&#x60;. The &#39;asins&#39; report, also known as the Purchased products report, is only available for seller brand owners. | 
 **report_request** | [**ReportRequest**](ReportRequest.md)|  | [optional] 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized - Request failed because user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden - Request failed because user does not have access to a specified resource |  -  |
**406** | Not acceptable - Failed due to report date being too far in the past. |  -  |
**422** | Unprocessable entity - Failed due to invalid parameters. |  -  |
**429** | Too Many Requests - Request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error - Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

