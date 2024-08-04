# ReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_date** | **str** | Date in YYYYMMDD format. The report contains only metrics generated on the specified date. Note that the time zone used for date calculation is the one associated with the profile used to make the request. | [optional] 
**tactic** | [**TacticReport**](TacticReport.md) |  | [optional] 
**segment** | [**Segment**](Segment.md) |  | [optional] 
**metrics** | **str** | A comma-separated list of the metrics to be included in the report.  Each report type supports different metrics. **To understand supported metrics for each report type, see [Report types](/API/docs/en-us/guides/reporting/v2/report-types).**  **Note**: Campaigns with vCPM costType should use view+click based metrics (viewAttributedConversions14d, viewAttributedDetailPageView14d, viewAttributedSales14d, viewAttributedUnitsOrdered14d, viewImpressions).  **Note**: Detail page view metrics (attributedDetailPageView14d, viewAttributedDetailPageView14d) have an SLA of 3 days.  **Tip**: Use new-to-brand (NTB) metrics to calculate how efficient your campaigns are at driving new shoppers:    1. Percentage of NTB orders &#x3D; attributedOrdersNewToBrand14d / attributedConversions14d   2. Percentage NTB sales &#x3D; attributedSalesNewToBrand14d / attributedSales14d   3. Percentage NTB units &#x3D; attributedUnitsOrderedNewToBrand14d / attributedUnitsOrdered14d   4. NTB order rate &#x3D; attributedOrdersNewToBrand14 / impressions | [optional] 

## Example

```python
from openapi_client.models.report_request import ReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportRequest from a JSON string
report_request_instance = ReportRequest.from_json(json)
# print the JSON string representation of the object
print(ReportRequest.to_json())

# convert the object into a dict
report_request_dict = report_request_instance.to_dict()
# create an instance of ReportRequest from a dict
report_request_from_dict = ReportRequest.from_dict(report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


