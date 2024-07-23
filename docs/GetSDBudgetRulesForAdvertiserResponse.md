# GetSDBudgetRulesForAdvertiserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_rules_for_advertiser_response** | [**List[SDBudgetRule]**](SDBudgetRule.md) | A list of rules created by the advertiser. | [optional] 
**next_token** | **str** | To retrieve the next page of results, call the same operation and specify this token in the request. If the &#x60;nextToken&#x60; field is empty, there are no further results. | [optional] 

## Example

```python
from openapi_client.models.get_sd_budget_rules_for_advertiser_response import GetSDBudgetRulesForAdvertiserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSDBudgetRulesForAdvertiserResponse from a JSON string
get_sd_budget_rules_for_advertiser_response_instance = GetSDBudgetRulesForAdvertiserResponse.from_json(json)
# print the JSON string representation of the object
print(GetSDBudgetRulesForAdvertiserResponse.to_json())

# convert the object into a dict
get_sd_budget_rules_for_advertiser_response_dict = get_sd_budget_rules_for_advertiser_response_instance.to_dict()
# create an instance of GetSDBudgetRulesForAdvertiserResponse from a dict
get_sd_budget_rules_for_advertiser_response_from_dict = GetSDBudgetRulesForAdvertiserResponse.from_dict(get_sd_budget_rules_for_advertiser_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


