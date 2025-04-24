# CashRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**product_id** | **str** |  | 
**quantity** | **float** |  | 
**currency_code** | **str** |  | 
**received_at** | **datetime** |  | 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.cash_redemption import CashRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of CashRedemption from a JSON string
cash_redemption_instance = CashRedemption.from_json(json)
# print the JSON string representation of the object
print(CashRedemption.to_json())

# convert the object into a dict
cash_redemption_dict = cash_redemption_instance.to_dict()
# create an instance of CashRedemption from a dict
cash_redemption_from_dict = CashRedemption.from_dict(cash_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


