# ApprovePayoutDeprecated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_intention_id** | **str** |  | 
**purpose_of_payment** | [**PaymentPurpose**](PaymentPurpose.md) |  | 
**unique_reference** | **str** |  | [optional] 

## Example

```python
from trivium_python_sdk.models.approve_payout_deprecated import ApprovePayoutDeprecated

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovePayoutDeprecated from a JSON string
approve_payout_deprecated_instance = ApprovePayoutDeprecated.from_json(json)
# print the JSON string representation of the object
print(ApprovePayoutDeprecated.to_json())

# convert the object into a dict
approve_payout_deprecated_dict = approve_payout_deprecated_instance.to_dict()
# create an instance of ApprovePayoutDeprecated from a dict
approve_payout_deprecated_from_dict = ApprovePayoutDeprecated.from_dict(approve_payout_deprecated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


