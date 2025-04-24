# DepositResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.deposit_response import DepositResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DepositResponse from a JSON string
deposit_response_instance = DepositResponse.from_json(json)
# print the JSON string representation of the object
print(DepositResponse.to_json())

# convert the object into a dict
deposit_response_dict = deposit_response_instance.to_dict()
# create an instance of DepositResponse from a dict
deposit_response_from_dict = DepositResponse.from_dict(deposit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


