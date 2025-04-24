# DepositPortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | **str** |  | 
**amount** | **float** |  | 

## Example

```python
from trivium_python_sdk.models.deposit_portfolio_request import DepositPortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DepositPortfolioRequest from a JSON string
deposit_portfolio_request_instance = DepositPortfolioRequest.from_json(json)
# print the JSON string representation of the object
print(DepositPortfolioRequest.to_json())

# convert the object into a dict
deposit_portfolio_request_dict = deposit_portfolio_request_instance.to_dict()
# create an instance of DepositPortfolioRequest from a dict
deposit_portfolio_request_from_dict = DepositPortfolioRequest.from_dict(deposit_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


