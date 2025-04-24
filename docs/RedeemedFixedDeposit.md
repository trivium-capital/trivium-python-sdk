# RedeemedFixedDeposit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_id** | **str** |  | 
**invested_quantity** | **float** |  | 
**redeemed_value** | **float** |  | 
**currency_code** | **str** |  | 
**provider_details** | [**ProviderDetails**](ProviderDetails.md) |  | 
**term** | **str** | Serialized as P{period}, e.g. 2 weeks &#x3D; P14D, 3 months &#x3D; P3M, 1 year &#x3D; P1Y | 
**redemption_date** | **date** |  | 
**return_at_maturity** | **float** |  | 
**locked_rate** | **float** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.redeemed_fixed_deposit import RedeemedFixedDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemedFixedDeposit from a JSON string
redeemed_fixed_deposit_instance = RedeemedFixedDeposit.from_json(json)
# print the JSON string representation of the object
print(RedeemedFixedDeposit.to_json())

# convert the object into a dict
redeemed_fixed_deposit_dict = redeemed_fixed_deposit_instance.to_dict()
# create an instance of RedeemedFixedDeposit from a dict
redeemed_fixed_deposit_from_dict = RedeemedFixedDeposit.from_dict(redeemed_fixed_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


