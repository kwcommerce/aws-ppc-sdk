# SDHeadlineRecommendationAccessDeniedException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | AccessDeniedErrorCode. | [optional] 
**details** | **str** | A human-readable description of the error response. | [optional] 

## Example

```python
from openapi_client.models.sd_headline_recommendation_access_denied_exception import SDHeadlineRecommendationAccessDeniedException

# TODO update the JSON string below
json = "{}"
# create an instance of SDHeadlineRecommendationAccessDeniedException from a JSON string
sd_headline_recommendation_access_denied_exception_instance = SDHeadlineRecommendationAccessDeniedException.from_json(json)
# print the JSON string representation of the object
print(SDHeadlineRecommendationAccessDeniedException.to_json())

# convert the object into a dict
sd_headline_recommendation_access_denied_exception_dict = sd_headline_recommendation_access_denied_exception_instance.to_dict()
# create an instance of SDHeadlineRecommendationAccessDeniedException from a dict
sd_headline_recommendation_access_denied_exception_from_dict = SDHeadlineRecommendationAccessDeniedException.from_dict(sd_headline_recommendation_access_denied_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


