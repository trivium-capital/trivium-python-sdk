# DepositSettled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.deposit_settled import DepositSettled

# TODO update the JSON string below
json = "{}"
# create an instance of DepositSettled from a JSON string
deposit_settled_instance = DepositSettled.from_json(json)
# print the JSON string representation of the object
print(DepositSettled.to_json())

# convert the object into a dict
deposit_settled_dict = deposit_settled_instance.to_dict()
# create an instance of DepositSettled from a dict
deposit_settled_from_dict = DepositSettled.from_dict(deposit_settled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


