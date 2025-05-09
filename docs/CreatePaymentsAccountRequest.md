# CreatePaymentsAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**currency_code** | **str** |  | 
**desired_bank_country** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.create_payments_account_request import CreatePaymentsAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentsAccountRequest from a JSON string
create_payments_account_request_instance = CreatePaymentsAccountRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentsAccountRequest.to_json())

# convert the object into a dict
create_payments_account_request_dict = create_payments_account_request_instance.to_dict()
# create an instance of CreatePaymentsAccountRequest from a dict
create_payments_account_request_from_dict = CreatePaymentsAccountRequest.from_dict(create_payments_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


