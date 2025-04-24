# CashCallbackEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**user_id** | **str** |  | 
**type** | **str** |  | 
**transaction_id** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.cash_callback_event import CashCallbackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CashCallbackEvent from a JSON string
cash_callback_event_instance = CashCallbackEvent.from_json(json)
# print the JSON string representation of the object
print(CashCallbackEvent.to_json())

# convert the object into a dict
cash_callback_event_dict = cash_callback_event_instance.to_dict()
# create an instance of CashCallbackEvent from a dict
cash_callback_event_from_dict = CashCallbackEvent.from_dict(cash_callback_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


