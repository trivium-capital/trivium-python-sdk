# ApprovePayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_intention_id** | **str** |  | 
**recipient_ref_id** | **str** |  | 
**purpose_of_payment** | [**PaymentPurpose**](PaymentPurpose.md) |  | 
**unique_reference** | **str** |  | [optional] 
**payment_reference** | **str** |  | [optional] 

## Example

```python
from trivium_python_sdk.models.approve_payout import ApprovePayout

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovePayout from a JSON string
approve_payout_instance = ApprovePayout.from_json(json)
# print the JSON string representation of the object
print(ApprovePayout.to_json())

# convert the object into a dict
approve_payout_dict = approve_payout_instance.to_dict()
# create an instance of ApprovePayout from a dict
approve_payout_from_dict = ApprovePayout.from_dict(approve_payout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


