# AssetClassProportion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_class** | [**AssetClass**](AssetClass.md) |  | 
**proportion** | **float** |  | 

## Example

```python
from trivium_python_sdk.models.asset_class_proportion import AssetClassProportion

# TODO update the JSON string below
json = "{}"
# create an instance of AssetClassProportion from a JSON string
asset_class_proportion_instance = AssetClassProportion.from_json(json)
# print the JSON string representation of the object
print(AssetClassProportion.to_json())

# convert the object into a dict
asset_class_proportion_dict = asset_class_proportion_instance.to_dict()
# create an instance of AssetClassProportion from a dict
asset_class_proportion_from_dict = AssetClassProportion.from_dict(asset_class_proportion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


