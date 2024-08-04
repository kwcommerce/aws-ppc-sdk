# NegativeTargetingExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The intent type. See the [targeting topic](https://advertising.amazon.com/help#GQCBASRVERXSARL3) in the Amazon Ads support center for more information. | [optional] 
**value** | **str** | The value to be negatively targeted. Used only in manual expressions. | [optional] 

## Example

```python
from openapi_client.models.negative_targeting_expression import NegativeTargetingExpression

# TODO update the JSON string below
json = "{}"
# create an instance of NegativeTargetingExpression from a JSON string
negative_targeting_expression_instance = NegativeTargetingExpression.from_json(json)
# print the JSON string representation of the object
print(NegativeTargetingExpression.to_json())

# convert the object into a dict
negative_targeting_expression_dict = negative_targeting_expression_instance.to_dict()
# create an instance of NegativeTargetingExpression from a dict
negative_targeting_expression_from_dict = NegativeTargetingExpression.from_dict(negative_targeting_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


