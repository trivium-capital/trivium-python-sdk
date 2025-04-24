# CashInboundCallbackEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**amount** | **float** |  | 
**currency_code** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.cash_inbound_callback_event import CashInboundCallbackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CashInboundCallbackEvent from a JSON string
cash_inbound_callback_event_instance = CashInboundCallbackEvent.from_json(json)
# print the JSON string representation of the object
print(CashInboundCallbackEvent.to_json())

# convert the object into a dict
cash_inbound_callback_event_dict = cash_inbound_callback_event_instance.to_dict()
# create an instance of CashInboundCallbackEvent from a dict
cash_inbound_callback_event_from_dict = CashInboundCallbackEvent.from_dict(cash_inbound_callback_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


