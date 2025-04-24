# TransferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | 
**recipient_name** | **str** |  | 
**bank** | [**FastParticipant**](FastParticipant.md) |  | 
**reference** | **str** |  | [optional] 
**type** | **str** |  | 
**account_holder_name** | **str** |  | 
**account_holder_address** | **str** |  | [optional] 
**bank_name** | **str** |  | 
**bank_address** | **str** |  | [optional] 
**swift_code** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.transfer_details import TransferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDetails from a JSON string
transfer_details_instance = TransferDetails.from_json(json)
# print the JSON string representation of the object
print(TransferDetails.to_json())

# convert the object into a dict
transfer_details_dict = transfer_details_instance.to_dict()
# create an instance of TransferDetails from a dict
transfer_details_from_dict = TransferDetails.from_dict(transfer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


