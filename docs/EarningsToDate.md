# EarningsToDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings** | **float** |  | 
**time_weighted_return_decimal** | **float** |  | 

## Example

```python
from trivium_python_sdk.models.earnings_to_date import EarningsToDate

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsToDate from a JSON string
earnings_to_date_instance = EarningsToDate.from_json(json)
# print the JSON string representation of the object
print(EarningsToDate.to_json())

# convert the object into a dict
earnings_to_date_dict = earnings_to_date_instance.to_dict()
# create an instance of EarningsToDate from a dict
earnings_to_date_from_dict = EarningsToDate.from_dict(earnings_to_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


