# CreateOnboardingDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**upload_link** | **str** | To upload document, perform a PUT request to this link with the file as the body. | 

## Example

```python
from trivium_python_sdk.models.create_onboarding_document_response import CreateOnboardingDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOnboardingDocumentResponse from a JSON string
create_onboarding_document_response_instance = CreateOnboardingDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOnboardingDocumentResponse.to_json())

# convert the object into a dict
create_onboarding_document_response_dict = create_onboarding_document_response_instance.to_dict()
# create an instance of CreateOnboardingDocumentResponse from a dict
create_onboarding_document_response_from_dict = CreateOnboardingDocumentResponse.from_dict(create_onboarding_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


