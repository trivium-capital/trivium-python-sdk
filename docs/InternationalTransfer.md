# InternationalTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | 
**account_holder_name** | **str** |  | 
**account_holder_address** | **str** |  | [optional] 
**bank_name** | **str** |  | 
**bank_address** | **str** |  | [optional] 
**swift_code** | **str** |  | 
**reference** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.international_transfer import InternationalTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalTransfer from a JSON string
international_transfer_instance = InternationalTransfer.from_json(json)
# print the JSON string representation of the object
print(InternationalTransfer.to_json())

# convert the object into a dict
international_transfer_dict = international_transfer_instance.to_dict()
# create an instance of InternationalTransfer from a dict
international_transfer_from_dict = InternationalTransfer.from_dict(international_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


