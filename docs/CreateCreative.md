# CreateCreative

Creative create model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_group_id** | **float** | Unqiue identifier for the ad group associated with the creative. | 
**creative_type** | [**CreativeTypeInCreativeRequest**](CreativeTypeInCreativeRequest.md) |  | [optional] 
**properties** | [**CreativeProperties**](CreativeProperties.md) |  | 

## Example

```python
from openapi_client.models.create_creative import CreateCreative

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreative from a JSON string
create_creative_instance = CreateCreative.from_json(json)
# print the JSON string representation of the object
print(CreateCreative.to_json())

# convert the object into a dict
create_creative_dict = create_creative_instance.to_dict()
# create an instance of CreateCreative from a dict
create_creative_from_dict = CreateCreative.from_dict(create_creative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


