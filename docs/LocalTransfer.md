# LocalTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | 
**recipient_name** | **str** |  | 
**bank** | [**FastParticipant**](FastParticipant.md) |  | 
**reference** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.local_transfer import LocalTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of LocalTransfer from a JSON string
local_transfer_instance = LocalTransfer.from_json(json)
# print the JSON string representation of the object
print(LocalTransfer.to_json())

# convert the object into a dict
local_transfer_dict = local_transfer_instance.to_dict()
# create an instance of LocalTransfer from a dict
local_transfer_from_dict = LocalTransfer.from_dict(local_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


