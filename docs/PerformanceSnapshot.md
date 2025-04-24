# PerformanceSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**nav** | **float** |  | 
**twr** | **float** |  | 

## Example

```python
from trivium_python_sdk.models.performance_snapshot import PerformanceSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceSnapshot from a JSON string
performance_snapshot_instance = PerformanceSnapshot.from_json(json)
# print the JSON string representation of the object
print(PerformanceSnapshot.to_json())

# convert the object into a dict
performance_snapshot_dict = performance_snapshot_instance.to_dict()
# create an instance of PerformanceSnapshot from a dict
performance_snapshot_from_dict = PerformanceSnapshot.from_dict(performance_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


