# Deposit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**quantity** | **float** |  | 
**currency_code** | **str** |  | 
**received_at** | **datetime** |  | 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.deposit import Deposit

# TODO update the JSON string below
json = "{}"
# create an instance of Deposit from a JSON string
deposit_instance = Deposit.from_json(json)
# print the JSON string representation of the object
print(Deposit.to_json())

# convert the object into a dict
deposit_dict = deposit_instance.to_dict()
# create an instance of Deposit from a dict
deposit_from_dict = Deposit.from_dict(deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


