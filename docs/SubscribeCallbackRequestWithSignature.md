# SubscribeCallbackRequestWithSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.subscribe_callback_request_with_signature import SubscribeCallbackRequestWithSignature

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeCallbackRequestWithSignature from a JSON string
subscribe_callback_request_with_signature_instance = SubscribeCallbackRequestWithSignature.from_json(json)
# print the JSON string representation of the object
print(SubscribeCallbackRequestWithSignature.to_json())

# convert the object into a dict
subscribe_callback_request_with_signature_dict = subscribe_callback_request_with_signature_instance.to_dict()
# create an instance of SubscribeCallbackRequestWithSignature from a dict
subscribe_callback_request_with_signature_from_dict = SubscribeCallbackRequestWithSignature.from_dict(subscribe_callback_request_with_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


