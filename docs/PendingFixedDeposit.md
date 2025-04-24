# PendingFixedDeposit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_id** | **str** |  | 
**currency_code** | **str** |  | 
**provider_details** | [**ProviderDetails**](ProviderDetails.md) |  | 
**term** | **str** | Serialized as P{period}, e.g. 2 weeks &#x3D; P14D, 3 months &#x3D; P3M, 1 year &#x3D; P1Y | 
**deposit_instructions** | [**DepositInstructions**](DepositInstructions.md) |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.pending_fixed_deposit import PendingFixedDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of PendingFixedDeposit from a JSON string
pending_fixed_deposit_instance = PendingFixedDeposit.from_json(json)
# print the JSON string representation of the object
print(PendingFixedDeposit.to_json())

# convert the object into a dict
pending_fixed_deposit_dict = pending_fixed_deposit_instance.to_dict()
# create an instance of PendingFixedDeposit from a dict
pending_fixed_deposit_from_dict = PendingFixedDeposit.from_dict(pending_fixed_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


