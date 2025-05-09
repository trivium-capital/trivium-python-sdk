# PaymentBalances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[PaymentBalance]**](PaymentBalance.md) |  | [optional] 

## Example

```python
from trivium_python_sdk.models.payment_balances import PaymentBalances

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBalances from a JSON string
payment_balances_instance = PaymentBalances.from_json(json)
# print the JSON string representation of the object
print(PaymentBalances.to_json())

# convert the object into a dict
payment_balances_dict = payment_balances_instance.to_dict()
# create an instance of PaymentBalances from a dict
payment_balances_from_dict = PaymentBalances.from_dict(payment_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


