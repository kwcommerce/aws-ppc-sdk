# SnapshotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_filter** | **str** | Optional. Restricts results to entities with state within the specified comma-separated list. Default behavior is to include &#39;enabled&#39; and &#39;paused&#39;. You can include &#39;enabled&#39;, &#39;paused&#39;, and &#39;archived&#39; or any combination. | [optional] 
**tactic_filter** | [**TacticFilter**](TacticFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.snapshot_request import SnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotRequest from a JSON string
snapshot_request_instance = SnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(SnapshotRequest.to_json())

# convert the object into a dict
snapshot_request_dict = snapshot_request_instance.to_dict()
# create an instance of SnapshotRequest from a dict
snapshot_request_from_dict = SnapshotRequest.from_dict(snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


