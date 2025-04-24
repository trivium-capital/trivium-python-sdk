# FixedDepositPlacement


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
**deposit_instructions** | [**DepositInstructions**](DepositInstructions.md) |  | 
**redeemed_value** | **float** |  | 

## Example

```python
from trivium_python_sdk.models.fixed_deposit_placement import FixedDepositPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of FixedDepositPlacement from a JSON string
fixed_deposit_placement_instance = FixedDepositPlacement.from_json(json)
# print the JSON string representation of the object
print(FixedDepositPlacement.to_json())

# convert the object into a dict
fixed_deposit_placement_dict = fixed_deposit_placement_instance.to_dict()
# create an instance of FixedDepositPlacement from a dict
fixed_deposit_placement_from_dict = FixedDepositPlacement.from_dict(fixed_deposit_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


