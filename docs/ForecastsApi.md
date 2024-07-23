# openapi_client.ForecastsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sd_forecast**](ForecastsApi.md#create_sd_forecast) | **POST** /sd/forecasts | Return forecasts for an ad group that may or may not exist.


# **create_sd_forecast**
> SDForecastResponse create_sd_forecast(amazon_advertising_api_client_id, amazon_advertising_api_scope, sd_forecast_request=sd_forecast_request)

Return forecasts for an ad group that may or may not exist.

Returns forecasts for a given ad group specified in SD forecast request.

### Example


```python
import openapi_client
from openapi_client.models.sd_forecast_request import SDForecastRequest
from openapi_client.models.sd_forecast_response import SDForecastResponse
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
    api_instance = openapi_client.ForecastsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    sd_forecast_request = openapi_client.SDForecastRequest() # SDForecastRequest |  (optional)

    try:
        # Return forecasts for an ad group that may or may not exist.
        api_response = api_instance.create_sd_forecast(amazon_advertising_api_client_id, amazon_advertising_api_scope, sd_forecast_request=sd_forecast_request)
        print("The response of ForecastsApi->create_sd_forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForecastsApi->create_sd_forecast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **sd_forecast_request** | [**SDForecastRequest**](SDForecastRequest.md)|  | [optional] 

### Return type

[**SDForecastResponse**](SDForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.sdforecasts.v3.1+json
 - **Accept**: application/vnd.sdforecasts.v3.1+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized. The request failed because the user is not authenticated or is not allowed to invoke the operation. |  -  |
**403** | Forbidden. The request failed because user does not have access to a specified resource. |  -  |
**429** | Too Many Requests. The request was rate-limited. Retry later. |  -  |
**500** | Internal Server Error. Something went wrong on the server. Retry later and report an error if unresolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

