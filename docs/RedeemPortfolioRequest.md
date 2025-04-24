# RedeemPortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | **str** |  | 
**amount** | **float** |  | 

## Example

```python
from trivium_python_sdk.models.redeem_portfolio_request import RedeemPortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemPortfolioRequest from a JSON string
redeem_portfolio_request_instance = RedeemPortfolioRequest.from_json(json)
# print the JSON string representation of the object
print(RedeemPortfolioRequest.to_json())

# convert the object into a dict
redeem_portfolio_request_dict = redeem_portfolio_request_instance.to_dict()
# create an instance of RedeemPortfolioRequest from a dict
redeem_portfolio_request_from_dict = RedeemPortfolioRequest.from_dict(redeem_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


