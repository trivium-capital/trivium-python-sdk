# trivium_python_sdk.ManagedPortfoliosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_portfolio_available_userid**](ManagedPortfoliosApi.md#get_api_v1_portfolio_available_userid) | **GET** /api/v1/portfolio/available/{userId} | 
[**get_api_v1_portfolio_performance_investedportfolioid**](ManagedPortfoliosApi.md#get_api_v1_portfolio_performance_investedportfolioid) | **GET** /api/v1/portfolio/performance/{investedPortfolioId} | 
[**get_api_v1_portfolio_positions_userid**](ManagedPortfoliosApi.md#get_api_v1_portfolio_positions_userid) | **GET** /api/v1/portfolio/positions/{userId} | 
[**post_api_v1_portfolio_deposit**](ManagedPortfoliosApi.md#post_api_v1_portfolio_deposit) | **POST** /api/v1/portfolio/deposit | 
[**post_api_v1_portfolio_redemption**](ManagedPortfoliosApi.md#post_api_v1_portfolio_redemption) | **POST** /api/v1/portfolio/redemption | 


# **get_api_v1_portfolio_available_userid**
> List[PortfolioInformation] get_api_v1_portfolio_available_userid(user_id)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.portfolio_information import PortfolioInformation
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
    api_instance = trivium_python_sdk.ManagedPortfoliosApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_api_v1_portfolio_available_userid(user_id)
        print("The response of ManagedPortfoliosApi->get_api_v1_portfolio_available_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedPortfoliosApi->get_api_v1_portfolio_available_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[PortfolioInformation]**](PortfolioInformation.md)

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

# **get_api_v1_portfolio_performance_investedportfolioid**
> PortfolioPerformance get_api_v1_portfolio_performance_investedportfolioid(invested_portfolio_id)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.portfolio_performance import PortfolioPerformance
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
    api_instance = trivium_python_sdk.ManagedPortfoliosApi(api_client)
    invested_portfolio_id = 'invested_portfolio_id_example' # str | 

    try:
        api_response = api_instance.get_api_v1_portfolio_performance_investedportfolioid(invested_portfolio_id)
        print("The response of ManagedPortfoliosApi->get_api_v1_portfolio_performance_investedportfolioid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedPortfoliosApi->get_api_v1_portfolio_performance_investedportfolioid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invested_portfolio_id** | **str**|  | 

### Return type

[**PortfolioPerformance**](PortfolioPerformance.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: path parameter investedPortfolioId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_portfolio_positions_userid**
> List[InvestedPortfolio] get_api_v1_portfolio_positions_userid(user_id)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.invested_portfolio import InvestedPortfolio
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
    api_instance = trivium_python_sdk.ManagedPortfoliosApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_api_v1_portfolio_positions_userid(user_id)
        print("The response of ManagedPortfoliosApi->get_api_v1_portfolio_positions_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedPortfoliosApi->get_api_v1_portfolio_positions_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[InvestedPortfolio]**](InvestedPortfolio.md)

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

# **post_api_v1_portfolio_deposit**
> post_api_v1_portfolio_deposit(deposit_portfolio_request)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.deposit_portfolio_request import DepositPortfolioRequest
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
    api_instance = trivium_python_sdk.ManagedPortfoliosApi(api_client)
    deposit_portfolio_request = trivium_python_sdk.DepositPortfolioRequest() # DepositPortfolioRequest | 

    try:
        api_instance.post_api_v1_portfolio_deposit(deposit_portfolio_request)
    except Exception as e:
        print("Exception when calling ManagedPortfoliosApi->post_api_v1_portfolio_deposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_portfolio_request** | [**DepositPortfolioRequest**](DepositPortfolioRequest.md)|  | 

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
**400** | Invalid value, Invalid value for: body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_portfolio_redemption**
> post_api_v1_portfolio_redemption(redeem_portfolio_request)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.redeem_portfolio_request import RedeemPortfolioRequest
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
    api_instance = trivium_python_sdk.ManagedPortfoliosApi(api_client)
    redeem_portfolio_request = trivium_python_sdk.RedeemPortfolioRequest() # RedeemPortfolioRequest | 

    try:
        api_instance.post_api_v1_portfolio_redemption(redeem_portfolio_request)
    except Exception as e:
        print("Exception when calling ManagedPortfoliosApi->post_api_v1_portfolio_redemption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redeem_portfolio_request** | [**RedeemPortfolioRequest**](RedeemPortfolioRequest.md)|  | 

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
**400** | Invalid value, Invalid value for: body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

