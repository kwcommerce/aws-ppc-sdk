# SDForecastRequest

Request payload for SD forecasting. Below are required and optional fields. Fields not listed will not impact forecast results. |Field              |Object            |Required| |-------------------|------------------|--------| |startDate          |Campaign          |required| |endDate            |Campaign          |optional| |costType           |Campaign          |optional| |bidOptimization    |AdGroup           |required| |creativeType       |AdGroup           |optional| |defaultBid         |AdGroup           |optional| |asin               |ProductAds        |required for vendors| |sku                |ProductAds        |required for sellers| |bid                |TargetingClauses  |required when defaultBid is not set| |expression         |TargetingClauses  |required| |ruleConditions     |OptimizationRules |optional|

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | [**Campaign**](Campaign.md) |  | 
**ad_group** | [**AdGroup**](AdGroup.md) |  | 
**optimization_rules** | [**List[OptimizationRule]**](OptimizationRule.md) | A list of SD optimization rules. Forecast will be affected by the optimization strategy rules.  Currently, supported rule metrics by forecast are &#x60;COST_PER_CLICK&#x60;, &#x60;COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS&#x60; and &#x60;COST_PER_ORDER&#x60;. | [optional] 
**product_ads** | [**List[ProductAd]**](ProductAd.md) |  | 
**targeting_clauses** | [**List[SDForecastRequestTargetingClause]**](SDForecastRequestTargetingClause.md) | A list of SD targeting clauses. | 
**negative_targeting_clauses** | [**List[NegativeTargetingClause]**](NegativeTargetingClause.md) | A list of SD negative targeting clauses. | [optional] 

## Example

```python
from openapi_client.models.sd_forecast_request import SDForecastRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SDForecastRequest from a JSON string
sd_forecast_request_instance = SDForecastRequest.from_json(json)
# print the JSON string representation of the object
print(SDForecastRequest.to_json())

# convert the object into a dict
sd_forecast_request_dict = sd_forecast_request_instance.to_dict()
# create an instance of SDForecastRequest from a dict
sd_forecast_request_from_dict = SDForecastRequest.from_dict(sd_forecast_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


