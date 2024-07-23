# SDHeadlineRecommendationRequest

Request structure of SD headline recommendation API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asins** | **List[str]** | An array of ASINs associated with the creative. | [optional] 
**max_num_recommendations** | **float** | Maximum number of recommendations that API should return. Response will [0, maxNumRecommendations] recommendations (recommendations are not guaranteed as there can be instances where the ML model can not generate policy compliant headlines for the given set of asins). | [optional] 
**ad_format** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sd_headline_recommendation_request import SDHeadlineRecommendationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SDHeadlineRecommendationRequest from a JSON string
sd_headline_recommendation_request_instance = SDHeadlineRecommendationRequest.from_json(json)
# print the JSON string representation of the object
print(SDHeadlineRecommendationRequest.to_json())

# convert the object into a dict
sd_headline_recommendation_request_dict = sd_headline_recommendation_request_instance.to_dict()
# create an instance of SDHeadlineRecommendationRequest from a dict
sd_headline_recommendation_request_from_dict = SDHeadlineRecommendationRequest.from_dict(sd_headline_recommendation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


