# RecommendedHeadline

Recommended Headline in response object. Recommended headline will be locale specific, i.e. for an asin input in ES, Recommended headline will be in ES.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headline_id** | **str** | Unique Id of Recommended headline. | [optional] 
**headline** | **str** | String that contains Recommended headline. | [optional] 

## Example

```python
from openapi_client.models.recommended_headline import RecommendedHeadline

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendedHeadline from a JSON string
recommended_headline_instance = RecommendedHeadline.from_json(json)
# print the JSON string representation of the object
print(RecommendedHeadline.to_json())

# convert the object into a dict
recommended_headline_dict = recommended_headline_instance.to_dict()
# create an instance of RecommendedHeadline from a dict
recommended_headline_from_dict = RecommendedHeadline.from_dict(recommended_headline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


