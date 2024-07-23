# SDSevenDaysMissedOpportunities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the missed opportunities date range (YYYY-MM-DD). | [optional] 
**end_date** | **date** | End date of the missed opportunities date range (YYYY-MM-DD). | [optional] 
**percent_time_in_budget** | **float** | Percentage of time the campaign is active with a budget. | [optional] 
**estimated_missed_sales_lower** | **float** | Lower bound of the estimated missed sales. This will be in local currency. | [optional] 
**estimated_missed_sales_upper** | **float** | Upper bound of the estimated missed sales. This will be in local currency. | [optional] 
**estimated_missed_clicks_lower** | **int** | Lower bound of the estimated missed clicks. | [optional] 
**estimated_missed_clicks_upper** | **int** | Upper bound of the estimated missed clicks. | [optional] 
**estimated_missed_impressions_lower** | **int** | Lower bound of the estimated missed impressions. | [optional] 
**estimated_missed_impressions_upper** | **int** | Upper bound of the estimated missed impressions. | [optional] 
**estimated_missed_viewable_impressions_lower** | **int** | Lower bound of the estimated missed viewable impressions for vCPM campaigns. | [optional] 
**estimated_missed_viewable_impressions_upper** | **int** | Upper bound of the estimated missed viewable impressions for vCPM campaigns. | [optional] 

## Example

```python
from openapi_client.models.sd_seven_days_missed_opportunities import SDSevenDaysMissedOpportunities

# TODO update the JSON string below
json = "{}"
# create an instance of SDSevenDaysMissedOpportunities from a JSON string
sd_seven_days_missed_opportunities_instance = SDSevenDaysMissedOpportunities.from_json(json)
# print the JSON string representation of the object
print(SDSevenDaysMissedOpportunities.to_json())

# convert the object into a dict
sd_seven_days_missed_opportunities_dict = sd_seven_days_missed_opportunities_instance.to_dict()
# create an instance of SDSevenDaysMissedOpportunities from a dict
sd_seven_days_missed_opportunities_from_dict = SDSevenDaysMissedOpportunities.from_dict(sd_seven_days_missed_opportunities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


