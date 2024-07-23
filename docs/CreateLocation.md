# CreateLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**ad_group_id** | **int** | The identifier of the ad group. | 
**expression** | [**List[LocationExpression]**](LocationExpression.md) | The location definition. | 

## Example

```python
from openapi_client.models.create_location import CreateLocation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLocation from a JSON string
create_location_instance = CreateLocation.from_json(json)
# print the JSON string representation of the object
print(CreateLocation.to_json())

# convert the object into a dict
create_location_dict = create_location_instance.to_dict()
# create an instance of CreateLocation from a dict
create_location_from_dict = CreateLocation.from_dict(create_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


