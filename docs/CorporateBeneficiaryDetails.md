# CorporateBeneficiaryDetails


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

## Example

```python
from trivium_python_sdk.models.corporate_beneficiary_details import CorporateBeneficiaryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateBeneficiaryDetails from a JSON string
corporate_beneficiary_details_instance = CorporateBeneficiaryDetails.from_json(json)
# print the JSON string representation of the object
print(CorporateBeneficiaryDetails.to_json())

# convert the object into a dict
corporate_beneficiary_details_dict = corporate_beneficiary_details_instance.to_dict()
# create an instance of CorporateBeneficiaryDetails from a dict
corporate_beneficiary_details_from_dict = CorporateBeneficiaryDetails.from_dict(corporate_beneficiary_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


