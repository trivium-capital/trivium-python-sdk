# CreateOnboardingDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | [**OnboardingDocumentType**](OnboardingDocumentType.md) |  | 
**document_name** | **str** |  | 

## Example

```python
from trivium_python_sdk.models.create_onboarding_document_request import CreateOnboardingDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOnboardingDocumentRequest from a JSON string
create_onboarding_document_request_instance = CreateOnboardingDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOnboardingDocumentRequest.to_json())

# convert the object into a dict
create_onboarding_document_request_dict = create_onboarding_document_request_instance.to_dict()
# create an instance of CreateOnboardingDocumentRequest from a dict
create_onboarding_document_request_from_dict = CreateOnboardingDocumentRequest.from_dict(create_onboarding_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


