# Profile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** |  | [optional] 
**country_code** | [**CountryCode**](CountryCode.md) |  | [optional] 
**currency_code** | **str** | The currency used for all monetary values for entities under this profile. |Region|&#x60;countryCode&#x60;|Country Name|&#x60;currencyCode&#x60;| |-----|------|------|------| |NA|BR|Brazil|BRL| |NA|CA|Canada|CAD| |NA|MX|Mexico|MXN| |NA|US|United States|USD| |EU|AE|United Arab Emirates|AED| |EU|BE|Belgium|EUR| |EU|DE|Germany|EUR| |EU|EG|Egypt|EGP| |EU|ES|Spain|EUR| |EU|FR|France|EUR| |EU|IN|India|INR| |EU|IT|Italy|EUR| |EU|NL|The Netherlands|EUR| |EU|PL|Poland|PLN| |EU|SA|Saudi Arabia|SAR| |EU|SE|Sweden|SEK| |EU|TR|Turkey|TRY| |EU|UK|United Kingdom|GBP| |EU|ZA| South Africa | ZAR| |FE|AU|Australia|AUD| |FE|JP|Japan|JPY| |FE|SG|Singapore|SGD| | [optional] [readonly] 
**daily_budget** | **float** | Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts. | [optional] 
**timezone** | **str** | The time zone used for all date-based campaign management and reporting. |Region|&#x60;countryCode&#x60;|Country Name|&#x60;timezone&#x60;| |------|-----|-----|------| |NA|BR|Brazil|America/Sao_Paulo| |NA|CA|Canada|America/Los_Angeles| |NA|MX|Mexico|America/Los_Angeles| |NA|US|United States|America/Los_Angeles| |EU|AE|United Arab Emirates|Asia/Dubai| |EU|BE|Belgium|Europe/Brussels| |EU|DE|Germany|Europe/Paris| |EU|EG|Egypt|Africa/Cairo| |EU|ES|Spain|Europe/Paris| |EU|FR|France|Europe/Paris| |EU|IN|India|Asia/Kolkata| |EU|IT|Italy|Europe/Paris| |EU|NL|The Netherlands|Europe/Amsterdam| |EU|PL|Poland|Europe/Warsaw| |EU|SA|Saudi Arabia|Asia/Riyadh| |EU|SE|Sweden|Europe/Stockholm| |EU|TR|Turkey|Europe/Istanbul| |EU|UK|United Kingdom|Europe/London| |EU|ZA| South Africa | Africa/Johannesburg | |FE|AU|Australia|Australia/Sydney| |FE|JP|Japan|Asia/Tokyo| |FE|SG|Singapore|Asia/Singapore| | [optional] [readonly] 
**account_info** | [**AccountInfo**](AccountInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


