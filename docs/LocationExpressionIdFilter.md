# LocationExpressionIdFilter

Filter entities by the list of objectIds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[int]** | Array of Location Expression Ids | 

## Example

```python
from openapi_client.models.location_expression_id_filter import LocationExpressionIdFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LocationExpressionIdFilter from a JSON string
location_expression_id_filter_instance = LocationExpressionIdFilter.from_json(json)
# print the JSON string representation of the object
print(LocationExpressionIdFilter.to_json())

# convert the object into a dict
location_expression_id_filter_dict = location_expression_id_filter_instance.to_dict()
# create an instance of LocationExpressionIdFilter from a dict
location_expression_id_filter_from_dict = LocationExpressionIdFilter.from_dict(location_expression_id_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


