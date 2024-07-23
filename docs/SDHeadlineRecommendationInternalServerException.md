# SDHeadlineRecommendationInternalServerException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | InternalErrorCode. | [optional] 
**details** | **str** | A human-readable description of the error response. | [optional] 

## Example

```python
from openapi_client.models.sd_headline_recommendation_internal_server_exception import SDHeadlineRecommendationInternalServerException

# TODO update the JSON string below
json = "{}"
# create an instance of SDHeadlineRecommendationInternalServerException from a JSON string
sd_headline_recommendation_internal_server_exception_instance = SDHeadlineRecommendationInternalServerException.from_json(json)
# print the JSON string representation of the object
print(SDHeadlineRecommendationInternalServerException.to_json())

# convert the object into a dict
sd_headline_recommendation_internal_server_exception_dict = sd_headline_recommendation_internal_server_exception_instance.to_dict()
# create an instance of SDHeadlineRecommendationInternalServerException from a dict
sd_headline_recommendation_internal_server_exception_from_dict = SDHeadlineRecommendationInternalServerException.from_dict(sd_headline_recommendation_internal_server_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


