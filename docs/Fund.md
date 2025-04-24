# Fund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**fund_id** | **str** |  | 
**description** | **str** |  | 
**proportion** | **float** |  | 
**asset_class** | [**AssetClass**](AssetClass.md) |  | 

## Example

```python
from trivium_python_sdk.models.fund import Fund

# TODO update the JSON string below
json = "{}"
# create an instance of Fund from a JSON string
fund_instance = Fund.from_json(json)
# print the JSON string representation of the object
print(Fund.to_json())

# convert the object into a dict
fund_dict = fund_instance.to_dict()
# create an instance of Fund from a dict
fund_from_dict = Fund.from_dict(fund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


