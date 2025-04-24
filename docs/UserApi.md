# trivium_python_sdk.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_user_userid**](UserApi.md#get_api_v1_user_userid) | **GET** /api/v1/user/{userId} | 
[**get_api_v1_user_userid_sign_embedded**](UserApi.md#get_api_v1_user_userid_sign_embedded) | **GET** /api/v1/user/{userId}/sign/embedded | 
[**post_api_v1_user**](UserApi.md#post_api_v1_user) | **POST** /api/v1/user | 
[**post_api_v1_user_events**](UserApi.md#post_api_v1_user_events) | **POST** /api/v1/user/events | 
[**post_api_v1_user_userid_documents**](UserApi.md#post_api_v1_user_userid_documents) | **POST** /api/v1/user/{userId}/documents | 


# **get_api_v1_user_userid**
> User get_api_v1_user_userid(user_id)

Returns user that has zero or more accounts

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.user import User
from trivium_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trivium_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: httpAuth
configuration = trivium_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with trivium_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trivium_python_sdk.UserApi(api_client)
    user_id = 'e63b255b-8ece-458b-ba26-d8e77188857a' # str | 

    try:
        api_response = api_instance.get_api_v1_user_userid(user_id)
        print("The response of UserApi->get_api_v1_user_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_api_v1_user_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: path parameter userId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_user_userid_sign_embedded**
> RetrieveDocumentSigningLinkResponse get_api_v1_user_userid_sign_embedded(user_id)

Returns link to be embedded in iframe like: <iframe src=https://app.boldsign.com/document/sign/?documentId=17882f5a... style=width:100%;height:100%/> 

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.retrieve_document_signing_link_response import RetrieveDocumentSigningLinkResponse
from trivium_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trivium_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: httpAuth
configuration = trivium_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with trivium_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trivium_python_sdk.UserApi(api_client)
    user_id = 'e63b255b-8ece-458b-ba26-d8e77188857a' # str | 

    try:
        api_response = api_instance.get_api_v1_user_userid_sign_embedded(user_id)
        print("The response of UserApi->get_api_v1_user_userid_sign_embedded:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_api_v1_user_userid_sign_embedded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**RetrieveDocumentSigningLinkResponse**](RetrieveDocumentSigningLinkResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** | Invalid value for X-Api-Key or Authorization HTTP header |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_user**
> User post_api_v1_user(user_details)

Create new user

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.user import User
from trivium_python_sdk.models.user_details import UserDetails
from trivium_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trivium_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: httpAuth
configuration = trivium_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with trivium_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trivium_python_sdk.UserApi(api_client)
    user_details = {"type":"CompanyDetails","taxId":"2024112233D","companyName":"Heavy Metal Industry Pte. Ltd.","email":"cfo@heavymetalindustry.com.sg","fullName":"Jonathan Tan Ah Kow","preferredName":"Jonathan","countryOfIncorporation":"SG"} # UserDetails | 

    try:
        api_response = api_instance.post_api_v1_user(user_details)
        print("The response of UserApi->post_api_v1_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->post_api_v1_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_details** | [**UserDetails**](UserDetails.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_user_events**
> SubscribeCallbackResponse post_api_v1_user_events(subscribe_callback_request)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.subscribe_callback_request import SubscribeCallbackRequest
from trivium_python_sdk.models.subscribe_callback_response import SubscribeCallbackResponse
from trivium_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trivium_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: httpAuth
configuration = trivium_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with trivium_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trivium_python_sdk.UserApi(api_client)
    subscribe_callback_request = {"type":"SubscribeCallbackRequestWithSignature","callbackUrl":"https://myserver.com/send/callback/here"} # SubscribeCallbackRequest | 

    try:
        api_response = api_instance.post_api_v1_user_events(subscribe_callback_request)
        print("The response of UserApi->post_api_v1_user_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->post_api_v1_user_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscribe_callback_request** | [**SubscribeCallbackRequest**](SubscribeCallbackRequest.md)|  | 

### Return type

[**SubscribeCallbackResponse**](SubscribeCallbackResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid value, Invalid value for: body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_user_userid_documents**
> CreateOnboardingDocumentResponse post_api_v1_user_userid_documents(user_id, create_onboarding_document_request)

Retrieve upload link for user documents

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.create_onboarding_document_request import CreateOnboardingDocumentRequest
from trivium_python_sdk.models.create_onboarding_document_response import CreateOnboardingDocumentResponse
from trivium_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = trivium_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: httpAuth
configuration = trivium_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with trivium_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trivium_python_sdk.UserApi(api_client)
    user_id = 'e63b255b-8ece-458b-ba26-d8e77188857a' # str | 
    create_onboarding_document_request = {"documentType":"PROOF_OF_COMPANY_REGISTRATION","documentName":"Company Registration.pdf"} # CreateOnboardingDocumentRequest | 

    try:
        api_response = api_instance.post_api_v1_user_userid_documents(user_id, create_onboarding_document_request)
        print("The response of UserApi->post_api_v1_user_userid_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->post_api_v1_user_userid_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **create_onboarding_document_request** | [**CreateOnboardingDocumentRequest**](CreateOnboardingDocumentRequest.md)|  | 

### Return type

[**CreateOnboardingDocumentResponse**](CreateOnboardingDocumentResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: path parameter userId, Invalid value for: body |  -  |
**401** | Invalid value for X-Api-Key or Authorization HTTP header |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

