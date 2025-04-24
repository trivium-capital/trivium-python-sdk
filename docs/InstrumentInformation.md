# InstrumentInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**description** | **str** |  | 
**quote** | [**InstrumentQuote**](InstrumentQuote.md) |  | 
**currency_code** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.instrument_information import InstrumentInformation

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentInformation from a JSON string
instrument_information_instance = InstrumentInformation.from_json(json)
# print the JSON string representation of the object
print(InstrumentInformation.to_json())

# convert the object into a dict
instrument_information_dict = instrument_information_instance.to_dict()
# create an instance of InstrumentInformation from a dict
instrument_information_from_dict = InstrumentInformation.from_dict(instrument_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


