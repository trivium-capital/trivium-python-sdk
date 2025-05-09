# QuoteDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sell_currency** | **str** |  | 
**buy_currency** | **str** |  | 
**fixed_side** | [**BuySell**](BuySell.md) |  | [optional] 
**amount** | **float** |  | 
**recipient_bank_country** | **str** |  | 
**charge_type** | [**ChargeType**](ChargeType.md) |  | 

## Example

```python
from trivium_python_sdk.models.quote_details import QuoteDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetails from a JSON string
quote_details_instance = QuoteDetails.from_json(json)
# print the JSON string representation of the object
print(QuoteDetails.to_json())

# convert the object into a dict
quote_details_dict = quote_details_instance.to_dict()
# create an instance of QuoteDetails from a dict
quote_details_from_dict = QuoteDetails.from_dict(quote_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


