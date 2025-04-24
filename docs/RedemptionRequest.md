# RedemptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** |  | 
**currency_code** | **str** |  | 
**transfer_details** | [**TransferDetails**](TransferDetails.md) |  | 

## Example

```python
from trivium_python_sdk.models.redemption_request import RedemptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedemptionRequest from a JSON string
redemption_request_instance = RedemptionRequest.from_json(json)
# print the JSON string representation of the object
print(RedemptionRequest.to_json())

# convert the object into a dict
redemption_request_dict = redemption_request_instance.to_dict()
# create an instance of RedemptionRequest from a dict
redemption_request_from_dict = RedemptionRequest.from_dict(redemption_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


