# PortfolioPerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[PerformanceSnapshot]**](PerformanceSnapshot.md) |  | [optional] 

## Example

```python
from trivium_python_sdk.models.portfolio_performance import PortfolioPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioPerformance from a JSON string
portfolio_performance_instance = PortfolioPerformance.from_json(json)
# print the JSON string representation of the object
print(PortfolioPerformance.to_json())

# convert the object into a dict
portfolio_performance_dict = portfolio_performance_instance.to_dict()
# create an instance of PortfolioPerformance from a dict
portfolio_performance_from_dict = PortfolioPerformance.from_dict(portfolio_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


