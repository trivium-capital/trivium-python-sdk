# PaymentIncoming


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**product_id** | **str** |  | 
**quantity** | **float** |  | 
**currency_code** | **str** |  | 
**created_at** | **datetime** |  | 
**completed_at** | **datetime** |  | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**payment_reference** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.payment_incoming import PaymentIncoming

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIncoming from a JSON string
payment_incoming_instance = PaymentIncoming.from_json(json)
# print the JSON string representation of the object
print(PaymentIncoming.to_json())

# convert the object into a dict
payment_incoming_dict = payment_incoming_instance.to_dict()
# create an instance of PaymentIncoming from a dict
payment_incoming_from_dict = PaymentIncoming.from_dict(payment_incoming_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


