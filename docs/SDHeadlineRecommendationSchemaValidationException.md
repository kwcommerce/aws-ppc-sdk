# SDHeadlineRecommendationSchemaValidationException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | InvalidArgumentErrorCode. | [optional] 
**details** | **str** | A human-readable description of the error response. | [optional] 

## Example

```python
from openapi_client.models.sd_headline_recommendation_schema_validation_exception import SDHeadlineRecommendationSchemaValidationException

# TODO update the JSON string below
json = "{}"
# create an instance of SDHeadlineRecommendationSchemaValidationException from a JSON string
sd_headline_recommendation_schema_validation_exception_instance = SDHeadlineRecommendationSchemaValidationException.from_json(json)
# print the JSON string representation of the object
print(SDHeadlineRecommendationSchemaValidationException.to_json())

# convert the object into a dict
sd_headline_recommendation_schema_validation_exception_dict = sd_headline_recommendation_schema_validation_exception_instance.to_dict()
# create an instance of SDHeadlineRecommendationSchemaValidationException from a dict
sd_headline_recommendation_schema_validation_exception_from_dict = SDHeadlineRecommendationSchemaValidationException.from_dict(sd_headline_recommendation_schema_validation_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


