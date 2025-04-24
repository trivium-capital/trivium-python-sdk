# MonthlyStatementMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**month** | **int** | Month of year, from 1 (January) to 12 (December) | 
**download_link** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.monthly_statement_metadata import MonthlyStatementMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyStatementMetadata from a JSON string
monthly_statement_metadata_instance = MonthlyStatementMetadata.from_json(json)
# print the JSON string representation of the object
print(MonthlyStatementMetadata.to_json())

# convert the object into a dict
monthly_statement_metadata_dict = monthly_statement_metadata_instance.to_dict()
# create an instance of MonthlyStatementMetadata from a dict
monthly_statement_metadata_from_dict = MonthlyStatementMetadata.from_dict(monthly_statement_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


