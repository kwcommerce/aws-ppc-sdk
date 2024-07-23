# BrandSafetyRequestResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BrandSafetyRequestResult]**](BrandSafetyRequestResult.md) | A list of results for the given requestId | [optional] 

## Example

```python
from openapi_client.models.brand_safety_request_results_response import BrandSafetyRequestResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSafetyRequestResultsResponse from a JSON string
brand_safety_request_results_response_instance = BrandSafetyRequestResultsResponse.from_json(json)
# print the JSON string representation of the object
print(BrandSafetyRequestResultsResponse.to_json())

# convert the object into a dict
brand_safety_request_results_response_dict = brand_safety_request_results_response_instance.to_dict()
# create an instance of BrandSafetyRequestResultsResponse from a dict
brand_safety_request_results_response_from_dict = BrandSafetyRequestResultsResponse.from_dict(brand_safety_request_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


