# Fast


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
from trivium_python_sdk.models.fast import Fast

# TODO update the JSON string below
json = "{}"
# create an instance of Fast from a JSON string
fast_instance = Fast.from_json(json)
# print the JSON string representation of the object
print(Fast.to_json())

# convert the object into a dict
fast_dict = fast_instance.to_dict()
# create an instance of Fast from a dict
fast_from_dict = Fast.from_dict(fast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


