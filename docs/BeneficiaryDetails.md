# BeneficiaryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | 
**address** | **str** |  | 
**city** | **str** |  | 
**country** | **str** |  | 
**state** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**type** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.beneficiary_details import BeneficiaryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiaryDetails from a JSON string
beneficiary_details_instance = BeneficiaryDetails.from_json(json)
# print the JSON string representation of the object
print(BeneficiaryDetails.to_json())

# convert the object into a dict
beneficiary_details_dict = beneficiary_details_instance.to_dict()
# create an instance of BeneficiaryDetails from a dict
beneficiary_details_from_dict = BeneficiaryDetails.from_dict(beneficiary_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


