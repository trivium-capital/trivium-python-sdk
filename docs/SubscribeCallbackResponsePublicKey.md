# SubscribeCallbackResponsePublicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.subscribe_callback_response_public_key import SubscribeCallbackResponsePublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeCallbackResponsePublicKey from a JSON string
subscribe_callback_response_public_key_instance = SubscribeCallbackResponsePublicKey.from_json(json)
# print the JSON string representation of the object
print(SubscribeCallbackResponsePublicKey.to_json())

# convert the object into a dict
subscribe_callback_response_public_key_dict = subscribe_callback_response_public_key_instance.to_dict()
# create an instance of SubscribeCallbackResponsePublicKey from a dict
subscribe_callback_response_public_key_from_dict = SubscribeCallbackResponsePublicKey.from_dict(subscribe_callback_response_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


