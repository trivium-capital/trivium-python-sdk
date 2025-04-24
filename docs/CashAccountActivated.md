# CashAccountActivated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**user_id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.cash_account_activated import CashAccountActivated

# TODO update the JSON string below
json = "{}"
# create an instance of CashAccountActivated from a JSON string
cash_account_activated_instance = CashAccountActivated.from_json(json)
# print the JSON string representation of the object
print(CashAccountActivated.to_json())

# convert the object into a dict
cash_account_activated_dict = cash_account_activated_instance.to_dict()
# create an instance of CashAccountActivated from a dict
cash_account_activated_from_dict = CashAccountActivated.from_dict(cash_account_activated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


