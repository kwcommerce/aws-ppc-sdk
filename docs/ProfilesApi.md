# openapi_client.ProfilesApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_profile_by_id**](ProfilesApi.md#get_profile_by_id) | **GET** /v2/profiles/{profileId} | Gets a profile specified by identifier.
[**list_profiles**](ProfilesApi.md#list_profiles) | **GET** /v2/profiles | Gets a list of profiles.
[**update_profiles**](ProfilesApi.md#update_profiles) | **PUT** /v2/profiles | Update the daily budget for one or more profiles.


# **get_profile_by_id**
> Profile get_profile_by_id(amazon_advertising_api_client_id, profile_id)

Gets a profile specified by identifier.

This operation does not return a response unless the current account has created at least one campaign using the advertising console.

### Example


```python
import openapi_client
from openapi_client.models.profile import Profile
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
    api_instance = openapi_client.ProfilesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    profile_id = 56 # int | 

    try:
        # Gets a profile specified by identifier.
        api_response = api_instance.get_profile_by_id(amazon_advertising_api_client_id, profile_id)
        print("The response of ProfilesApi->get_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **profile_id** | **int**|  | 

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_profiles**
> List[Profile] list_profiles(amazon_advertising_api_client_id, api_program=api_program, access_level=access_level, profile_type_filter=profile_type_filter, valid_payment_method_filter=valid_payment_method_filter)

Gets a list of profiles.

Note that this operation does not return a response unless the current account has created at least one campaign using the advertising console.

### Example


```python
import openapi_client
from openapi_client.models.profile import Profile
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
    api_instance = openapi_client.ProfilesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    api_program = campaign # str | Filters response to include profiles that have permissions for the specified Advertising API program only. Setting `apiProgram=billing` filters the response to include only profiles to which the user and application associated with the access token have permission to view or edit billing information. (optional) (default to campaign)
    access_level = edit # str | Filters response to include profiles that have specified permissions for the specified Advertising API program only. Currently, the only supported access level is `view` and `edit`. Setting `accessLevel=view` filters the response to include only profiles to which the user and application associated with the access token have view permission to the provided api program. (optional) (default to edit)
    profile_type_filter = 'profile_type_filter_example' # str | Filters response to include profiles that are of the specified types in the comma-delimited list. Default is all types. Note that this filter performs an inclusive AND operation on the types. (optional)
    valid_payment_method_filter = 'valid_payment_method_filter_example' # str | Filter response to include profiles that have valid payment methods. Default is to include all profiles. Setting this filter to `true` returns only profiles with either no `validPaymentMethod` field, or the `validPaymentMethod` field set to `true`.  Setting this to `false` returns profiles with the `validPaymentMethod` field set to `false` only. (optional)

    try:
        # Gets a list of profiles.
        api_response = api_instance.list_profiles(amazon_advertising_api_client_id, api_program=api_program, access_level=access_level, profile_type_filter=profile_type_filter, valid_payment_method_filter=valid_payment_method_filter)
        print("The response of ProfilesApi->list_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->list_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **api_program** | **str**| Filters response to include profiles that have permissions for the specified Advertising API program only. Setting &#x60;apiProgram&#x3D;billing&#x60; filters the response to include only profiles to which the user and application associated with the access token have permission to view or edit billing information. | [optional] [default to campaign]
 **access_level** | **str**| Filters response to include profiles that have specified permissions for the specified Advertising API program only. Currently, the only supported access level is &#x60;view&#x60; and &#x60;edit&#x60;. Setting &#x60;accessLevel&#x3D;view&#x60; filters the response to include only profiles to which the user and application associated with the access token have view permission to the provided api program. | [optional] [default to edit]
 **profile_type_filter** | **str**| Filters response to include profiles that are of the specified types in the comma-delimited list. Default is all types. Note that this filter performs an inclusive AND operation on the types. | [optional] 
 **valid_payment_method_filter** | **str**| Filter response to include profiles that have valid payment methods. Default is to include all profiles. Setting this filter to &#x60;true&#x60; returns only profiles with either no &#x60;validPaymentMethod&#x60; field, or the &#x60;validPaymentMethod&#x60; field set to &#x60;true&#x60;.  Setting this to &#x60;false&#x60; returns profiles with the &#x60;validPaymentMethod&#x60; field set to &#x60;false&#x60; only. | [optional] 

### Return type

[**List[Profile]**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profiles**
> List[ProfileResponse] update_profiles(amazon_advertising_api_client_id, profile=profile)

Update the daily budget for one or more profiles.

Note that this operation is only used for Sellers using Sponsored Products. This operation is not enabled for vendor type accounts.

### Example


```python
import openapi_client
from openapi_client.models.profile import Profile
from openapi_client.models.profile_response import ProfileResponse
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
    api_instance = openapi_client.ProfilesApi(api_client)
    amazon_advertising_api_client_id = 'amazon_advertising_api_client_id_example' # str | The identifier of a client associated with a \"Login with Amazon\" account.
    profile = [openapi_client.Profile()] # List[Profile] |  (optional)

    try:
        # Update the daily budget for one or more profiles.
        api_response = api_instance.update_profiles(amazon_advertising_api_client_id, profile=profile)
        print("The response of ProfilesApi->update_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_advertising_api_client_id** | **str**| The identifier of a client associated with a \&quot;Login with Amazon\&quot; account. | 
 **profile** | [**List[Profile]**](Profile.md)|  | [optional] 

### Return type

[**List[ProfileResponse]**](ProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

