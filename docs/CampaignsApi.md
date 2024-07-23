# openapi_client.CampaignsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_campaign**](CampaignsApi.md#archive_campaign) | **DELETE** /sd/campaigns/{campaignId} | Sets the campaign status to archived.
[**create_campaigns**](CampaignsApi.md#create_campaigns) | **POST** /sd/campaigns | Creates one or more campaigns.
[**get_campaign**](CampaignsApi.md#get_campaign) | **GET** /sd/campaigns/{campaignId} | Gets a requested campaign.
[**get_campaign_response_ex**](CampaignsApi.md#get_campaign_response_ex) | **GET** /sd/campaigns/extended/{campaignId} | Gets extended information for a requested campaign.
[**list_campaigns**](CampaignsApi.md#list_campaigns) | **GET** /sd/campaigns | Gets a list of campaigns.
[**list_campaigns_ex**](CampaignsApi.md#list_campaigns_ex) | **GET** /sd/campaigns/extended | Gets a list of campaigns with extended fields.
[**update_campaigns**](CampaignsApi.md#update_campaigns) | **PUT** /sd/campaigns | Updates one or more campaigns.


# **archive_campaign**
> CampaignResponse archive_campaign(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)

Sets the campaign status to archived.

This operation is equivalent to an update operation that sets the status field to 'archived'. Note that setting the status field to 'archived' is permanent and can't be undone. See [Developer Notes](https://advertising.amazon.com/API/docs/en-us/info/developer-notes#archiving) for more information.

### Example


```python
import openapi_client
from openapi_client.models.campaign_response import CampaignResponse
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
    api_instance = openapi_client.CampaignsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    campaign_id = 56 # int | The identifier of the campaign.

    try:
        # Sets the campaign status to archived.
        api_response = api_instance.archive_campaign(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)
        print("The response of CampaignsApi->archive_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->archive_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **campaign_id** | **int**| The identifier of the campaign. | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

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

# **create_campaigns**
> List[CampaignResponse] create_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_campaign=create_campaign)

Creates one or more campaigns.

### Example


```python
import openapi_client
from openapi_client.models.campaign_response import CampaignResponse
from openapi_client.models.create_campaign import CreateCampaign
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
    api_instance = openapi_client.CampaignsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    create_campaign = [openapi_client.CreateCampaign()] # List[CreateCampaign] | An array of Campaign objects. For each object, specify required fields and their values. Required fields are `name`, `tactic`, `state`, and `startDate`. Maximum length of the array is 100 objects. If you don't specify a `budget`, it will be set as the [default budget for your region](https://advertising.amazon.com/API/docs/en-us/concepts/limits#default-budgets). Campaign names must be unique across SD, SB, and SP.   If you are using Optimization rules, the following campaign budget must be at least:   - 5x the value of any COST_PER_ORDER threshold.   - 10x the value of any COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS threshold.   - 20x the value of any COST_PER_CLICK threshold.  (optional)

    try:
        # Creates one or more campaigns.
        api_response = api_instance.create_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, create_campaign=create_campaign)
        print("The response of CampaignsApi->create_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->create_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **create_campaign** | [**List[CreateCampaign]**](CreateCampaign.md)| An array of Campaign objects. For each object, specify required fields and their values. Required fields are &#x60;name&#x60;, &#x60;tactic&#x60;, &#x60;state&#x60;, and &#x60;startDate&#x60;. Maximum length of the array is 100 objects. If you don&#39;t specify a &#x60;budget&#x60;, it will be set as the [default budget for your region](https://advertising.amazon.com/API/docs/en-us/concepts/limits#default-budgets). Campaign names must be unique across SD, SB, and SP.   If you are using Optimization rules, the following campaign budget must be at least:   - 5x the value of any COST_PER_ORDER threshold.   - 10x the value of any COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS threshold.   - 20x the value of any COST_PER_CLICK threshold.  | [optional] 

### Return type

[**List[CampaignResponse]**](CampaignResponse.md)

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

# **get_campaign**
> Campaign get_campaign(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)

Gets a requested campaign.

Returns a Campaign object for a requested campaign. Note that the Campaign object is designed for performance, with a small set of commonly used campaign fields to reduce size. If the extended set of fields is required, use the campaign operations that return the CampaignResponseEx object.

### Example


```python
import openapi_client
from openapi_client.models.campaign import Campaign
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
    api_instance = openapi_client.CampaignsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    campaign_id = 56 # int | The identifier of the requested campaign.

    try:
        # Gets a requested campaign.
        api_response = api_instance.get_campaign(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)
        print("The response of CampaignsApi->get_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **campaign_id** | **int**| The identifier of the requested campaign. | 

### Return type

[**Campaign**](Campaign.md)

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

# **get_campaign_response_ex**
> CampaignResponseEx get_campaign_response_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)

Gets extended information for a requested campaign.

Returns a CampaignResponseEx object for a requested campaign. The CampaignResponseEx includes the extended set of available fields.

### Example


```python
import openapi_client
from openapi_client.models.campaign_response_ex import CampaignResponseEx
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
    api_instance = openapi_client.CampaignsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    campaign_id = 56 # int | The identifier of the requested campaign.

    try:
        # Gets extended information for a requested campaign.
        api_response = api_instance.get_campaign_response_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, campaign_id)
        print("The response of CampaignsApi->get_campaign_response_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign_response_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **campaign_id** | **int**| The identifier of the requested campaign. | 

### Return type

[**CampaignResponseEx**](CampaignResponseEx.md)

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

# **list_campaigns**
> List[Campaign] list_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, name=name, campaign_id_filter=campaign_id_filter, portfolio_id_filter=portfolio_id_filter)

Gets a list of campaigns.

Gets an array of Campaign objects for a requested set of Sponsored Display campaigns. Note that the Campaign object is designed for performance, and includes a small set of commonly used fields to reduce size. If the extended set of fields is required, use the campaign operations that return the CampaignResponseEx object.

### Example


```python
import openapi_client
from openapi_client.models.campaign import Campaign
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
    api_instance = openapi_client.CampaignsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 0 # int | Optional. Sets a cursor into the requested set of campaigns. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional) (default to 0)
    count = 56 # int | Optional. Sets the number of Campaign objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten campaigns set `startIndex=0` and `count=10`. To return the next ten campaigns, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. The returned array is filtered to include only campaigns with state set to one of the values in the specified comma-delimited list. (optional) (default to enabled, paused, archived)
    name = 'name_example' # str | Optional. The returned array includes only campaign with the specified name using an exact string match. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. The returned array includes only campaigns with identifiers matching those specified in the comma-delimited string. (optional)
    portfolio_id_filter = 'portfolio_id_filter_example' # str | Optional. The returned array includes only campaigns associated with Portfolio identifiers matching those specified in the comma-delimited string. (optional)

    try:
        # Gets a list of campaigns.
        api_response = api_instance.list_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, name=name, campaign_id_filter=campaign_id_filter, portfolio_id_filter=portfolio_id_filter)
        print("The response of CampaignsApi->list_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->list_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of campaigns. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] [default to 0]
 **count** | **int**| Optional. Sets the number of Campaign objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten campaigns set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten campaigns, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. The returned array is filtered to include only campaigns with state set to one of the values in the specified comma-delimited list. | [optional] [default to enabled, paused, archived]
 **name** | **str**| Optional. The returned array includes only campaign with the specified name using an exact string match. | [optional] 
 **campaign_id_filter** | **str**| Optional. The returned array includes only campaigns with identifiers matching those specified in the comma-delimited string. | [optional] 
 **portfolio_id_filter** | **str**| Optional. The returned array includes only campaigns associated with Portfolio identifiers matching those specified in the comma-delimited string. | [optional] 

### Return type

[**List[Campaign]**](Campaign.md)

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

# **list_campaigns_ex**
> List[CampaignResponseEx] list_campaigns_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, name=name, campaign_id_filter=campaign_id_filter, portfolio_id_filter=portfolio_id_filter)

Gets a list of campaigns with extended fields.

Gets an array of CampaignResponseEx objects for a set of requested campaigns.

### Example


```python
import openapi_client
from openapi_client.models.campaign_response_ex import CampaignResponseEx
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
    api_instance = openapi_client.CampaignsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    start_index = 56 # int | Optional. Sets a cursor into the requested set of campaigns. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. (optional)
    count = 56 # int | Optional. Sets the number of Campaign objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten campaigns set `startIndex=0` and `count=10`. To return the next ten campaigns, set `startIndex=10` and `count=10`, and so on. Defaults to max page size. (optional)
    state_filter = enabled, paused, archived # str | Optional. The returned array is filtered to include only campaigns with state set to one of the values in the specified comma-delimited list. (optional) (default to enabled, paused, archived)
    name = 'name_example' # str | Optional. The returned array includes only campaign with the specified name using an exact string match. (optional)
    campaign_id_filter = 'campaign_id_filter_example' # str | Optional. The returned array includes only campaigns with identifiers matching those specified in the comma-delimited string. (optional)
    portfolio_id_filter = 'portfolio_id_filter_example' # str | Optional. The returned array includes only campaigns associated with Portfolio identifiers matching those specified in the comma-delimited string. (optional)

    try:
        # Gets a list of campaigns with extended fields.
        api_response = api_instance.list_campaigns_ex(amazon_advertising_api_client_id, amazon_advertising_api_scope, start_index=start_index, count=count, state_filter=state_filter, name=name, campaign_id_filter=campaign_id_filter, portfolio_id_filter=portfolio_id_filter)
        print("The response of CampaignsApi->list_campaigns_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->list_campaigns_ex: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **start_index** | **int**| Optional. Sets a cursor into the requested set of campaigns. Use in conjunction with the &#x60;count&#x60; parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0. | [optional] 
 **count** | **int**| Optional. Sets the number of Campaign objects in the returned array. Use in conjunction with the &#x60;startIndex&#x60; parameter to control pagination. For example, to return the first ten campaigns set &#x60;startIndex&#x3D;0&#x60; and &#x60;count&#x3D;10&#x60;. To return the next ten campaigns, set &#x60;startIndex&#x3D;10&#x60; and &#x60;count&#x3D;10&#x60;, and so on. Defaults to max page size. | [optional] 
 **state_filter** | **str**| Optional. The returned array is filtered to include only campaigns with state set to one of the values in the specified comma-delimited list. | [optional] [default to enabled, paused, archived]
 **name** | **str**| Optional. The returned array includes only campaign with the specified name using an exact string match. | [optional] 
 **campaign_id_filter** | **str**| Optional. The returned array includes only campaigns with identifiers matching those specified in the comma-delimited string. | [optional] 
 **portfolio_id_filter** | **str**| Optional. The returned array includes only campaigns associated with Portfolio identifiers matching those specified in the comma-delimited string. | [optional] 

### Return type

[**List[CampaignResponseEx]**](CampaignResponseEx.md)

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

# **update_campaigns**
> List[CampaignResponse] update_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_campaign=update_campaign)

Updates one or more campaigns.

### Example


```python
import openapi_client
from openapi_client.models.campaign_response import CampaignResponse
from openapi_client.models.update_campaign import UpdateCampaign
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
    api_instance = openapi_client.CampaignsApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    amazon_advertising_api_scope = 'amazon_advertising_api_scope_example' # str | The identifier of a profile associated with the advertiser account. Use `GET` method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header.
    update_campaign = [openapi_client.UpdateCampaign()] # List[UpdateCampaign] | An array of Campaign objects. For each object, specify a campaign identifier and mutable fields with their updated values. The mutable fields are `name`, `state`, `budget`, `startDate`, and `endDate`. Maximum length of the array is 100 objects. (optional)

    try:
        # Updates one or more campaigns.
        api_response = api_instance.update_campaigns(amazon_advertising_api_client_id, amazon_advertising_api_scope, update_campaign=update_campaign)
        print("The response of CampaignsApi->update_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->update_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **amazon_advertising_api_scope** | **str**| The identifier of a profile associated with the advertiser account. Use &#x60;GET&#x60; method on Profiles resource to list profiles associated with the access token passed in the HTTP Authorization header. | 
 **update_campaign** | [**List[UpdateCampaign]**](UpdateCampaign.md)| An array of Campaign objects. For each object, specify a campaign identifier and mutable fields with their updated values. The mutable fields are &#x60;name&#x60;, &#x60;state&#x60;, &#x60;budget&#x60;, &#x60;startDate&#x60;, and &#x60;endDate&#x60;. Maximum length of the array is 100 objects. | [optional] 

### Return type

[**List[CampaignResponse]**](CampaignResponse.md)

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

