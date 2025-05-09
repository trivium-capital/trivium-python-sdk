# IndividualBeneficiaryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**address** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | [optional] 
**country** | **str** |  | 
**postal_code** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.individual_beneficiary_details import IndividualBeneficiaryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualBeneficiaryDetails from a JSON string
individual_beneficiary_details_instance = IndividualBeneficiaryDetails.from_json(json)
# print the JSON string representation of the object
print(IndividualBeneficiaryDetails.to_json())

# convert the object into a dict
individual_beneficiary_details_dict = individual_beneficiary_details_instance.to_dict()
# create an instance of IndividualBeneficiaryDetails from a dict
individual_beneficiary_details_from_dict = IndividualBeneficiaryDetails.from_dict(individual_beneficiary_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


