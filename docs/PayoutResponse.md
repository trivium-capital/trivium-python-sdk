# PayoutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_intention_id** | **str** |  | 
**recipient_ref_id** | **str** |  | 
**sell_amount** | **float** |  | 
**sell_currency** | **str** |  | 
**buy_amount** | **float** |  | 
**buy_currency** | **str** |  | 
**rate** | **float** |  | 
**total_fees** | **float** |  | 
**total_amount** | **float** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from trivium_python_sdk.models.payout_response import PayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutResponse from a JSON string
payout_response_instance = PayoutResponse.from_json(json)
# print the JSON string representation of the object
print(PayoutResponse.to_json())

# convert the object into a dict
payout_response_dict = payout_response_instance.to_dict()
# create an instance of PayoutResponse from a dict
payout_response_from_dict = PayoutResponse.from_dict(payout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


