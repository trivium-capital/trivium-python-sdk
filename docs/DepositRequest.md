# DepositRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** |  | 
**currency_code** | **str** |  | 
**transfer** | [**Transfer**](Transfer.md) |  | 

## Example

```python
from trivium_python_sdk.models.deposit_request import DepositRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DepositRequest from a JSON string
deposit_request_instance = DepositRequest.from_json(json)
# print the JSON string representation of the object
print(DepositRequest.to_json())

# convert the object into a dict
deposit_request_dict = deposit_request_instance.to_dict()
# create an instance of DepositRequest from a dict
deposit_request_from_dict = DepositRequest.from_dict(deposit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


