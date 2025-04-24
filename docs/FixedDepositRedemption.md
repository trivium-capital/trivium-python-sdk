# FixedDepositRedemption


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
from trivium_python_sdk.models.fixed_deposit_redemption import FixedDepositRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of FixedDepositRedemption from a JSON string
fixed_deposit_redemption_instance = FixedDepositRedemption.from_json(json)
# print the JSON string representation of the object
print(FixedDepositRedemption.to_json())

# convert the object into a dict
fixed_deposit_redemption_dict = fixed_deposit_redemption_instance.to_dict()
# create an instance of FixedDepositRedemption from a dict
fixed_deposit_redemption_from_dict = FixedDepositRedemption.from_dict(fixed_deposit_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


