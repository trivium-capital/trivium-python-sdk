# AdHocPayoutIntention


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
from trivium_python_sdk.models.ad_hoc_payout_intention import AdHocPayoutIntention

# TODO update the JSON string below
json = "{}"
# create an instance of AdHocPayoutIntention from a JSON string
ad_hoc_payout_intention_instance = AdHocPayoutIntention.from_json(json)
# print the JSON string representation of the object
print(AdHocPayoutIntention.to_json())

# convert the object into a dict
ad_hoc_payout_intention_dict = ad_hoc_payout_intention_instance.to_dict()
# create an instance of AdHocPayoutIntention from a dict
ad_hoc_payout_intention_from_dict = AdHocPayoutIntention.from_dict(ad_hoc_payout_intention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


