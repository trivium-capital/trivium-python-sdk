# UserTransaction


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
from trivium_python_sdk.models.user_transaction import UserTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of UserTransaction from a JSON string
user_transaction_instance = UserTransaction.from_json(json)
# print the JSON string representation of the object
print(UserTransaction.to_json())

# convert the object into a dict
user_transaction_dict = user_transaction_instance.to_dict()
# create an instance of UserTransaction from a dict
user_transaction_from_dict = UserTransaction.from_dict(user_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


