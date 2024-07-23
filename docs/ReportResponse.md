# ReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | The identifier of the report. | [optional] 
**record_type** | **str** | The type of report requested. | [optional] 
**status** | **str** | The build status of the report. | [optional] 
**status_details** | **str** | A human-readable description of the current status. | [optional] 
**location** | **str** | The URI location of the report. | [optional] 
**file_size** | **int** | The size of the report file, in bytes. | [optional] 
**expiration** | **int** | Epoch date of the expiration of the URI in the &#x60;location&#x60; property. | [optional] 

## Example

```python
from openapi_client.models.report_response import ReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportResponse from a JSON string
report_response_instance = ReportResponse.from_json(json)
# print the JSON string representation of the object
print(ReportResponse.to_json())

# convert the object into a dict
report_response_dict = report_response_instance.to_dict()
# create an instance of ReportResponse from a dict
report_response_from_dict = ReportResponse.from_dict(report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


