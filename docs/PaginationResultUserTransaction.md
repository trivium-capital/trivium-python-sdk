# PaginationResultUserTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[UserTransaction]**](UserTransaction.md) |  | [optional] 
**total_count** | **int** |  | 
**has_next_page** | **bool** |  | 

## Example

```python
from trivium_python_sdk.models.pagination_result_user_transaction import PaginationResultUserTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResultUserTransaction from a JSON string
pagination_result_user_transaction_instance = PaginationResultUserTransaction.from_json(json)
# print the JSON string representation of the object
print(PaginationResultUserTransaction.to_json())

# convert the object into a dict
pagination_result_user_transaction_dict = pagination_result_user_transaction_instance.to_dict()
# create an instance of PaginationResultUserTransaction from a dict
pagination_result_user_transaction_from_dict = PaginationResultUserTransaction.from_dict(pagination_result_user_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


