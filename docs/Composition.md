# Composition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classes** | [**List[AssetClassProportion]**](AssetClassProportion.md) |  | [optional] 
**funds** | [**List[Fund]**](Fund.md) |  | [optional] 
**countries** | [**List[CountryProportion]**](CountryProportion.md) |  | [optional] 

## Example

```python
from trivium_python_sdk.models.composition import Composition

# TODO update the JSON string below
json = "{}"
# create an instance of Composition from a JSON string
composition_instance = Composition.from_json(json)
# print the JSON string representation of the object
print(Composition.to_json())

# convert the object into a dict
composition_dict = composition_instance.to_dict()
# create an instance of Composition from a dict
composition_from_dict = Composition.from_dict(composition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


