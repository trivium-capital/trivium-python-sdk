# LimitOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**quantity** | **float** |  | 
**limit_price** | **float** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.limit_order import LimitOrder

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOrder from a JSON string
limit_order_instance = LimitOrder.from_json(json)
# print the JSON string representation of the object
print(LimitOrder.to_json())

# convert the object into a dict
limit_order_dict = limit_order_instance.to_dict()
# create an instance of LimitOrder from a dict
limit_order_from_dict = LimitOrder.from_dict(limit_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


