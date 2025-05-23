# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**account_type** | [**AccountType**](AccountType.md) |  | 
**currency_code** | **str** |  | 
**status** | [**AccountStatus**](AccountStatus.md) |  | 
**provider** | [**ProviderDetails**](ProviderDetails.md) |  | 
**earnings_to_date** | [**EarningsToDate**](EarningsToDate.md) |  | 
**balance** | [**Balance**](Balance.md) |  | 
**deposit_instructions** | [**DepositInstructions**](DepositInstructions.md) |  | 

## Example

```python
from trivium_python_sdk.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


