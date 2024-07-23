# SDProductTargetingTheme

Contextual targeting theme definitions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the meaningful theme name which will be used as a unique identifier across various themes in the same request. This identifier will also be used to map the recommendations back to the theme in the response body. Note: the value for this field cannot be \&quot;default\&quot; as that&#39;s a reserved keyword in the system. | 
**expression** | [**List[SDProductTargetingThemeExpression]**](SDProductTargetingThemeExpression.md) | A list of expressions defining the contextual targeting theme. The list will define an AND operator on different expressions. For example, asinPriceGreaterThan and asinReviewRatingLessThan can be used to request product recommendations which are both with greater price and less review rating compared to the goal products. Note: Currently the service only supports one item in the array. | 

## Example

```python
from openapi_client.models.sd_product_targeting_theme import SDProductTargetingTheme

# TODO update the JSON string below
json = "{}"
# create an instance of SDProductTargetingTheme from a JSON string
sd_product_targeting_theme_instance = SDProductTargetingTheme.from_json(json)
# print the JSON string representation of the object
print(SDProductTargetingTheme.to_json())

# convert the object into a dict
sd_product_targeting_theme_dict = sd_product_targeting_theme_instance.to_dict()
# create an instance of SDProductTargetingTheme from a dict
sd_product_targeting_theme_from_dict = SDProductTargetingTheme.from_dict(sd_product_targeting_theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


