# SubscribeCallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.subscribe_callback_response import SubscribeCallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeCallbackResponse from a JSON string
subscribe_callback_response_instance = SubscribeCallbackResponse.from_json(json)
# print the JSON string representation of the object
print(SubscribeCallbackResponse.to_json())

# convert the object into a dict
subscribe_callback_response_dict = subscribe_callback_response_instance.to_dict()
# create an instance of SubscribeCallbackResponse from a dict
subscribe_callback_response_from_dict = SubscribeCallbackResponse.from_dict(subscribe_callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


