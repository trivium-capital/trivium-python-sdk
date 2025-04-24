# trivium_python_sdk.FixedDepositApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_fixeddeposit_placement_placementid**](FixedDepositApi.md#get_api_v1_fixeddeposit_placement_placementid) | **GET** /api/v1/fixedDeposit/placement/{placementId} | 
[**get_api_v1_fixeddeposit_user_userid**](FixedDepositApi.md#get_api_v1_fixeddeposit_user_userid) | **GET** /api/v1/fixedDeposit/user/{userId} | 
[**put_api_v1_fixeddeposit_placement_placementid**](FixedDepositApi.md#put_api_v1_fixeddeposit_placement_placementid) | **PUT** /api/v1/fixedDeposit/placement/{placementId} | 


# **get_api_v1_fixeddeposit_placement_placementid**
> FixedDepositPlacement get_api_v1_fixeddeposit_placement_placementid(placement_id)

Get fixed deposit placement

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.fixed_deposit_placement import FixedDepositPlacement
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
    api_instance = trivium_python_sdk.FixedDepositApi(api_client)
    placement_id = 'f5d15e38-c21b-4295-95fc-87233edf7069' # str | 

    try:
        api_response = api_instance.get_api_v1_fixeddeposit_placement_placementid(placement_id)
        print("The response of FixedDepositApi->get_api_v1_fixeddeposit_placement_placementid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositApi->get_api_v1_fixeddeposit_placement_placementid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_id** | **str**|  | 

### Return type

[**FixedDepositPlacement**](FixedDepositPlacement.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: path parameter placementId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_fixeddeposit_user_userid**
> List[FixedDepositPlacement] get_api_v1_fixeddeposit_user_userid(user_id)

Get fixed deposit placement

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.fixed_deposit_placement import FixedDepositPlacement
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
    api_instance = trivium_python_sdk.FixedDepositApi(api_client)
    user_id = 'e63b255b-8ece-458b-ba26-d8e77188857a' # str | 

    try:
        api_response = api_instance.get_api_v1_fixeddeposit_user_userid(user_id)
        print("The response of FixedDepositApi->get_api_v1_fixeddeposit_user_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedDepositApi->get_api_v1_fixeddeposit_user_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[FixedDepositPlacement]**](FixedDepositPlacement.md)

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

# **put_api_v1_fixeddeposit_placement_placementid**
> put_api_v1_fixeddeposit_placement_placementid(placement_id, process_fixed_deposit_placement_request)

Start processing fixed deposit placement

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.process_fixed_deposit_placement_request import ProcessFixedDepositPlacementRequest
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
    api_instance = trivium_python_sdk.FixedDepositApi(api_client)
    placement_id = 'f5d15e38-c21b-4295-95fc-87233edf7069' # str | 
    process_fixed_deposit_placement_request = {"quantity":100.0,"transfer":{"from":{"type":"Fast","accountNumber":"222222","recipientName":"Corporate Pte. Ltd.","bank":"HSBC_CORP"},"to":{"type":"Fast","accountNumber":"111111","recipientName":"Corporate Pte. Ltd.","bank":"HSBC_CORP"}}} # ProcessFixedDepositPlacementRequest | 

    try:
        api_instance.put_api_v1_fixeddeposit_placement_placementid(placement_id, process_fixed_deposit_placement_request)
    except Exception as e:
        print("Exception when calling FixedDepositApi->put_api_v1_fixeddeposit_placement_placementid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_id** | **str**|  | 
 **process_fixed_deposit_placement_request** | [**ProcessFixedDepositPlacementRequest**](ProcessFixedDepositPlacementRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: path parameter placementId, Invalid value for: body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

