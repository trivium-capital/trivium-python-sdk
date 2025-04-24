# InstrumentQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid** | **float** |  | 
**ask** | **float** |  | 
**high** | **float** |  | 
**low** | **float** |  | 

## Example

```python
from trivium_python_sdk.models.instrument_quote import InstrumentQuote

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentQuote from a JSON string
instrument_quote_instance = InstrumentQuote.from_json(json)
# print the JSON string representation of the object
print(InstrumentQuote.to_json())

# convert the object into a dict
instrument_quote_dict = instrument_quote_instance.to_dict()
# create an instance of InstrumentQuote from a dict
instrument_quote_from_dict = InstrumentQuote.from_dict(instrument_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


