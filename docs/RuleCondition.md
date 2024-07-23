# RuleCondition

A rule condition that defines the advertiser's intent for the outcome of the rule. Certain actions are performed by the product to achieve and maintain the rule condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** | The name of the metric. Supported rule metrics and corresponding supported comparisonOperators: |      MetricName      |ComparisonOperator  |Description| |------------------|--------------------|-------------------| |COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS     |              LESS_THAN_OR_EQUAL_TO             |Maximize viewable impressions while cost per 1000 views less than or equal to &#x60;threshold&#x60;| |COST_PER_CLICK    |              LESS_THAN_OR_EQUAL_TO            |Maximize page visits while cost per click less than or equal to &#x60;threshold&#x60;| |COST_PER_ORDER    |              LESS_THAN_OR_EQUAL_TO            |Maximize viewable impressions/page visits/conversion while cost per order less than or equal to &#x60;threshold&#x60;| | 
**comparison_operator** | **str** | The comparison operator. | 
**threshold** | **float** | The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table: |                  MetricName            | Minimum of &#x60;threshold&#x60; Value  | |----------------------------------------|-----------------------------------| |COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS  | 1                                 | |COST_PER_CLICK                          | 0.5                               | |COST_PER_ORDER                          | 5                                 | | 

## Example

```python
from openapi_client.models.rule_condition import RuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RuleCondition from a JSON string
rule_condition_instance = RuleCondition.from_json(json)
# print the JSON string representation of the object
print(RuleCondition.to_json())

# convert the object into a dict
rule_condition_dict = rule_condition_instance.to_dict()
# create an instance of RuleCondition from a dict
rule_condition_from_dict = RuleCondition.from_dict(rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


