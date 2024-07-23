# AdGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The HTTP status code of the response. | [optional] 
**description** | **str** | A human-readable description of the response. | [optional] 
**ad_group_id** | **int** | The identifier of the ad group. | [optional] 

## Example

```python
from openapi_client.models.ad_group_response import AdGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdGroupResponse from a JSON string
ad_group_response_instance = AdGroupResponse.from_json(json)
# print the JSON string representation of the object
print(AdGroupResponse.to_json())

# convert the object into a dict
ad_group_response_dict = ad_group_response_instance.to_dict()
# create an instance of AdGroupResponse from a dict
ad_group_response_from_dict = AdGroupResponse.from_dict(ad_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


