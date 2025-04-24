# RedemptionSettled

Confirmation that redemption amount has arrived in redemption bank account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**amount** | **float** |  | 
**currency_code** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.redemption_settled import RedemptionSettled

# TODO update the JSON string below
json = "{}"
# create an instance of RedemptionSettled from a JSON string
redemption_settled_instance = RedemptionSettled.from_json(json)
# print the JSON string representation of the object
print(RedemptionSettled.to_json())

# convert the object into a dict
redemption_settled_dict = redemption_settled_instance.to_dict()
# create an instance of RedemptionSettled from a dict
redemption_settled_from_dict = RedemptionSettled.from_dict(redemption_settled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


