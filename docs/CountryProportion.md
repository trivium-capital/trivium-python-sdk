# CountryProportion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**proportion** | **float** |  | 

## Example

```python
from trivium_python_sdk.models.country_proportion import CountryProportion

# TODO update the JSON string below
json = "{}"
# create an instance of CountryProportion from a JSON string
country_proportion_instance = CountryProportion.from_json(json)
# print the JSON string representation of the object
print(CountryProportion.to_json())

# convert the object into a dict
country_proportion_dict = country_proportion_instance.to_dict()
# create an instance of CountryProportion from a dict
country_proportion_from_dict = CountryProportion.from_dict(country_proportion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


