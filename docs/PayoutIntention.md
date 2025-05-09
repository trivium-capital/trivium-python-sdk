# PayoutIntention


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account_id** | **str** |  | 
**quote** | [**QuoteDetails**](QuoteDetails.md) |  | 
**beneficiary** | [**BeneficiaryDetails**](BeneficiaryDetails.md) |  | 
**bank_account_details** | [**BankAccountDetails**](BankAccountDetails.md) |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.payout_intention import PayoutIntention

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutIntention from a JSON string
payout_intention_instance = PayoutIntention.from_json(json)
# print the JSON string representation of the object
print(PayoutIntention.to_json())

# convert the object into a dict
payout_intention_dict = payout_intention_instance.to_dict()
# create an instance of PayoutIntention from a dict
payout_intention_from_dict = PayoutIntention.from_dict(payout_intention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


