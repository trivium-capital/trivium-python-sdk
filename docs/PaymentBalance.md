# PaymentBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_balance** | **float** |  | 
**pending_balance** | **float** |  | 
**currency_code** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.payment_balance import PaymentBalance

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBalance from a JSON string
payment_balance_instance = PaymentBalance.from_json(json)
# print the JSON string representation of the object
print(PaymentBalance.to_json())

# convert the object into a dict
payment_balance_dict = payment_balance_instance.to_dict()
# create an instance of PaymentBalance from a dict
payment_balance_from_dict = PaymentBalance.from_dict(payment_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


