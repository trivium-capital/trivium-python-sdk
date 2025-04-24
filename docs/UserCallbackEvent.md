# UserCallbackEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.user_callback_event import UserCallbackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UserCallbackEvent from a JSON string
user_callback_event_instance = UserCallbackEvent.from_json(json)
# print the JSON string representation of the object
print(UserCallbackEvent.to_json())

# convert the object into a dict
user_callback_event_dict = user_callback_event_instance.to_dict()
# create an instance of UserCallbackEvent from a dict
user_callback_event_from_dict = UserCallbackEvent.from_dict(user_callback_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


