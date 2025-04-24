# PortfolioInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**past_returns** | [**List[PastReturn]**](PastReturn.md) |  | [optional] 
**composition** | [**Composition**](Composition.md) |  | 

## Example

```python
from trivium_python_sdk.models.portfolio_information import PortfolioInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioInformation from a JSON string
portfolio_information_instance = PortfolioInformation.from_json(json)
# print the JSON string representation of the object
print(PortfolioInformation.to_json())

# convert the object into a dict
portfolio_information_dict = portfolio_information_instance.to_dict()
# create an instance of PortfolioInformation from a dict
portfolio_information_from_dict = PortfolioInformation.from_dict(portfolio_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


