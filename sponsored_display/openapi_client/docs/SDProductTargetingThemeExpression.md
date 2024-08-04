# SDProductTargetingThemeExpression

The expression used to define the contextual targeting theme.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The contextual targeting grammar used to define the targeting theme. Note asinAsBestSeller is currently not supported. | 

## Example

```python
from openapi_client.models.sd_product_targeting_theme_expression import SDProductTargetingThemeExpression

# TODO update the JSON string below
json = "{}"
# create an instance of SDProductTargetingThemeExpression from a JSON string
sd_product_targeting_theme_expression_instance = SDProductTargetingThemeExpression.from_json(json)
# print the JSON string representation of the object
print(SDProductTargetingThemeExpression.to_json())

# convert the object into a dict
sd_product_targeting_theme_expression_dict = sd_product_targeting_theme_expression_instance.to_dict()
# create an instance of SDProductTargetingThemeExpression from a dict
sd_product_targeting_theme_expression_from_dict = SDProductTargetingThemeExpression.from_dict(sd_product_targeting_theme_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


