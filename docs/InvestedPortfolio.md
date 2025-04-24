# InvestedPortfolio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invested_portfolio_id** | **str** |  | 
**portfolio_information** | [**PortfolioInformation**](PortfolioInformation.md) |  | 
**nav** | **float** |  | 
**currency_code** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.invested_portfolio import InvestedPortfolio

# TODO update the JSON string below
json = "{}"
# create an instance of InvestedPortfolio from a JSON string
invested_portfolio_instance = InvestedPortfolio.from_json(json)
# print the JSON string representation of the object
print(InvestedPortfolio.to_json())

# convert the object into a dict
invested_portfolio_dict = invested_portfolio_instance.to_dict()
# create an instance of InvestedPortfolio from a dict
invested_portfolio_from_dict = InvestedPortfolio.from_dict(invested_portfolio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


