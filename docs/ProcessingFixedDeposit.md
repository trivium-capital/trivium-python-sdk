# ProcessingFixedDeposit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_id** | **str** |  | 
**invested_quantity** | **float** |  | 
**currency_code** | **str** |  | 
**provider_details** | [**ProviderDetails**](ProviderDetails.md) |  | 
**term** | **str** | Serialized as P{period}, e.g. 2 weeks &#x3D; P14D, 3 months &#x3D; P3M, 1 year &#x3D; P1Y | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.processing_fixed_deposit import ProcessingFixedDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingFixedDeposit from a JSON string
processing_fixed_deposit_instance = ProcessingFixedDeposit.from_json(json)
# print the JSON string representation of the object
print(ProcessingFixedDeposit.to_json())

# convert the object into a dict
processing_fixed_deposit_dict = processing_fixed_deposit_instance.to_dict()
# create an instance of ProcessingFixedDeposit from a dict
processing_fixed_deposit_from_dict = ProcessingFixedDeposit.from_dict(processing_fixed_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


