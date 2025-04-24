# LockedFixedDeposit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_id** | **str** |  | 
**invested_quantity** | **float** |  | 
**current_value** | **float** |  | 
**currency_code** | **str** |  | 
**provider_details** | [**ProviderDetails**](ProviderDetails.md) |  | 
**term** | **str** | Serialized as P{period}, e.g. 2 weeks &#x3D; P14D, 3 months &#x3D; P3M, 1 year &#x3D; P1Y | 
**redemption_date** | **date** |  | 
**return_at_maturity** | **float** |  | 
**locked_rate** | **float** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.locked_fixed_deposit import LockedFixedDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of LockedFixedDeposit from a JSON string
locked_fixed_deposit_instance = LockedFixedDeposit.from_json(json)
# print the JSON string representation of the object
print(LockedFixedDeposit.to_json())

# convert the object into a dict
locked_fixed_deposit_dict = locked_fixed_deposit_instance.to_dict()
# create an instance of LockedFixedDeposit from a dict
locked_fixed_deposit_from_dict = LockedFixedDeposit.from_dict(locked_fixed_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


