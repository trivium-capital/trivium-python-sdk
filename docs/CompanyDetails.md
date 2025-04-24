# CompanyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** |  | 
**company_name** | **str** |  | 
**email** | **str** |  | 
**full_name** | **str** | Name of Authorised Person | 
**preferred_name** | **str** |  | 
**country_of_incorporation** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.company_details import CompanyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyDetails from a JSON string
company_details_instance = CompanyDetails.from_json(json)
# print the JSON string representation of the object
print(CompanyDetails.to_json())

# convert the object into a dict
company_details_dict = company_details_instance.to_dict()
# create an instance of CompanyDetails from a dict
company_details_from_dict = CompanyDetails.from_dict(company_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


