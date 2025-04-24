# Redemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**quantity** | **float** |  | 
**currency_code** | **str** |  | 
**received_at** | **datetime** |  | 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.redemption import Redemption

# TODO update the JSON string below
json = "{}"
# create an instance of Redemption from a JSON string
redemption_instance = Redemption.from_json(json)
# print the JSON string representation of the object
print(Redemption.to_json())

# convert the object into a dict
redemption_dict = redemption_instance.to_dict()
# create an instance of Redemption from a dict
redemption_from_dict = Redemption.from_dict(redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


