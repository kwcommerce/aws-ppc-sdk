# SnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | The identifier of the snapshot that was requested. | [optional] 
**record_type** | **str** | The record type of the snapshot file. | [optional] 
**status** | **str** | The status of the generation of the snapshot. | [optional] 
**status_details** | **str** | Optional description of the status. | [optional] 
**location** | **str** | The URI for the snapshot. It&#39;s only available if status is SUCCESS. | [optional] 
**file_size** | **float** | The size of the snapshot file in bytes. It&#39;s only available if status is SUCCESS. | [optional] 
**expiration** | **float** | The epoch time for expiration of the snapshot file and each snapshot file will be expired in 30 mins after generated. It&#39;s only available if status is SUCCESS. | [optional] 

## Example

```python
from openapi_client.models.snapshot_response import SnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotResponse from a JSON string
snapshot_response_instance = SnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotResponse.to_json())

# convert the object into a dict
snapshot_response_dict = snapshot_response_instance.to_dict()
# create an instance of SnapshotResponse from a dict
snapshot_response_from_dict = SnapshotResponse.from_dict(snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


