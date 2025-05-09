# PaymentOutgoing


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
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.payment_outgoing import PaymentOutgoing

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOutgoing from a JSON string
payment_outgoing_instance = PaymentOutgoing.from_json(json)
# print the JSON string representation of the object
print(PaymentOutgoing.to_json())

# convert the object into a dict
payment_outgoing_dict = payment_outgoing_instance.to_dict()
# create an instance of PaymentOutgoing from a dict
payment_outgoing_from_dict = PaymentOutgoing.from_dict(payment_outgoing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


