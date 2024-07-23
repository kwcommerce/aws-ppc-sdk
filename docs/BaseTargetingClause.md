# BaseTargetingClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**bid** | **float** | The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign&#39;s marketplace; for a list of maximum allowable bids, find the [\&quot;Bid constraints by marketplace\&quot; table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause&#39;s adGroup has an enabled optimization rule. | [optional] 

## Example

```python
from openapi_client.models.base_targeting_clause import BaseTargetingClause

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTargetingClause from a JSON string
base_targeting_clause_instance = BaseTargetingClause.from_json(json)
# print the JSON string representation of the object
print(BaseTargetingClause.to_json())

# convert the object into a dict
base_targeting_clause_dict = base_targeting_clause_instance.to_dict()
# create an instance of BaseTargetingClause from a dict
base_targeting_clause_from_dict = BaseTargetingClause.from_dict(base_targeting_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


