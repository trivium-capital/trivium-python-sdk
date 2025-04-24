# ProcessFixedDepositPlacementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** |  | 
**transfer** | [**Transfer**](Transfer.md) |  | 

## Example

```python
from trivium_python_sdk.models.process_fixed_deposit_placement_request import ProcessFixedDepositPlacementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessFixedDepositPlacementRequest from a JSON string
process_fixed_deposit_placement_request_instance = ProcessFixedDepositPlacementRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessFixedDepositPlacementRequest.to_json())

# convert the object into a dict
process_fixed_deposit_placement_request_dict = process_fixed_deposit_placement_request_instance.to_dict()
# create an instance of ProcessFixedDepositPlacementRequest from a dict
process_fixed_deposit_placement_request_from_dict = ProcessFixedDepositPlacementRequest.from_dict(process_fixed_deposit_placement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


