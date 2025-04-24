# Swift


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
from trivium_python_sdk.models.swift import Swift

# TODO update the JSON string below
json = "{}"
# create an instance of Swift from a JSON string
swift_instance = Swift.from_json(json)
# print the JSON string representation of the object
print(Swift.to_json())

# convert the object into a dict
swift_dict = swift_instance.to_dict()
# create an instance of Swift from a dict
swift_from_dict = Swift.from_dict(swift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


