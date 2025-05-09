# PaymentsAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**currency_code** | **str** |  | 
**status** | [**AccountStatus**](AccountStatus.md) |  | 
**provider** | [**ProviderDetails**](ProviderDetails.md) |  | 
**deposit_instructions** | [**List[BankAccountDetails]**](BankAccountDetails.md) |  | [optional] 

## Example

```python
from trivium_python_sdk.models.payments_account import PaymentsAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsAccount from a JSON string
payments_account_instance = PaymentsAccount.from_json(json)
# print the JSON string representation of the object
print(PaymentsAccount.to_json())

# convert the object into a dict
payments_account_dict = payments_account_instance.to_dict()
# create an instance of PaymentsAccount from a dict
payments_account_from_dict = PaymentsAccount.from_dict(payments_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


