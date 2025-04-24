# DepositInstructions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local** | [**List[LocalTransfer]**](LocalTransfer.md) |  | [optional] 
**var_global** | [**List[InternationalTransfer]**](InternationalTransfer.md) |  | [optional] 

## Example

```python
from trivium_python_sdk.models.deposit_instructions import DepositInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of DepositInstructions from a JSON string
deposit_instructions_instance = DepositInstructions.from_json(json)
# print the JSON string representation of the object
print(DepositInstructions.to_json())

# convert the object into a dict
deposit_instructions_dict = deposit_instructions_instance.to_dict()
# create an instance of DepositInstructions from a dict
deposit_instructions_from_dict = DepositInstructions.from_dict(deposit_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


