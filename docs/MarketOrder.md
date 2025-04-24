# MarketOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**quantity** | **float** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.market_order import MarketOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MarketOrder from a JSON string
market_order_instance = MarketOrder.from_json(json)
# print the JSON string representation of the object
print(MarketOrder.to_json())

# convert the object into a dict
market_order_dict = market_order_instance.to_dict()
# create an instance of MarketOrder from a dict
market_order_from_dict = MarketOrder.from_dict(market_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


