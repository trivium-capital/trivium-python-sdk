# BankAccountDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | [**PaymentType**](PaymentType.md) |  | 
**currency** | **str** |  | 
**bank_name** | **str** |  | 
**bank_account_holder_name** | **str** |  | 
**bank_account_number** | **str** |  | 
**bank_country** | **str** |  | 
**bank_swift** | **str** |  | 
**routing_code_type1** | [**RoutingCodeType**](RoutingCodeType.md) |  | [optional] 
**routing_code_value1** | **str** |  | [optional] 
**routing_code_type2** | [**RoutingCodeType**](RoutingCodeType.md) |  | [optional] 
**routing_code_value2** | **str** |  | [optional] 

## Example

```python
from trivium_python_sdk.models.bank_account_details import BankAccountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDetails from a JSON string
bank_account_details_instance = BankAccountDetails.from_json(json)
# print the JSON string representation of the object
print(BankAccountDetails.to_json())

# convert the object into a dict
bank_account_details_dict = bank_account_details_instance.to_dict()
# create an instance of BankAccountDetails from a dict
bank_account_details_from_dict = BankAccountDetails.from_dict(bank_account_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


