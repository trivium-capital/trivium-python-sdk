# IndividualDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_number** | **str** |  | 
**full_name** | **str** |  | 
**nationality** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.individual_details import IndividualDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualDetails from a JSON string
individual_details_instance = IndividualDetails.from_json(json)
# print the JSON string representation of the object
print(IndividualDetails.to_json())

# convert the object into a dict
individual_details_dict = individual_details_instance.to_dict()
# create an instance of IndividualDetails from a dict
individual_details_from_dict = IndividualDetails.from_dict(individual_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


