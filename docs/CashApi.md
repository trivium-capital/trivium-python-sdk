# trivium_python_sdk.CashApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_cash_account_accountid**](CashApi.md#get_api_v1_cash_account_accountid) | **GET** /api/v1/cash/account/{accountId} | 
[**get_api_v1_cash_account_user_userid**](CashApi.md#get_api_v1_cash_account_user_userid) | **GET** /api/v1/cash/account/user/{userId} | 
[**get_api_v1_cash_balance_userid**](CashApi.md#get_api_v1_cash_balance_userid) | **GET** /api/v1/cash/balance/{userId} | 
[**get_api_v1_cash_rates**](CashApi.md#get_api_v1_cash_rates) | **GET** /api/v1/cash/rates | 
[**get_api_v1_cash_transactions_accountid**](CashApi.md#get_api_v1_cash_transactions_accountid) | **GET** /api/v1/cash/transactions/{accountId} | 
[**get_api_v1_cash_transactions_redemption_info**](CashApi.md#get_api_v1_cash_transactions_redemption_info) | **GET** /api/v1/cash/transactions/redemption/info | 
[**post_api_v1_cash_account**](CashApi.md#post_api_v1_cash_account) | **POST** /api/v1/cash/account | 
[**post_api_v1_cash_events**](CashApi.md#post_api_v1_cash_events) | **POST** /api/v1/cash/events | 
[**post_api_v1_cash_request_deposit_accountid**](CashApi.md#post_api_v1_cash_request_deposit_accountid) | **POST** /api/v1/cash/request/deposit/{accountId} | 
[**post_api_v1_cash_request_redemption_accountid**](CashApi.md#post_api_v1_cash_request_redemption_accountid) | **POST** /api/v1/cash/request/redemption/{accountId} | 
[**put_api_v1_cash_callback**](CashApi.md#put_api_v1_cash_callback) | **PUT** /api/v1/cash/callback | 


# **get_api_v1_cash_account_accountid**
> Account get_api_v1_cash_account_accountid(account_id)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.account import Account
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    account_id = '40117016-ac89-4690-9986-01102be1ac9b' # str | 

    try:
        api_response = api_instance.get_api_v1_cash_account_accountid(account_id)
        print("The response of CashApi->get_api_v1_cash_account_accountid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->get_api_v1_cash_account_accountid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: path parameter accountId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_cash_account_user_userid**
> List[Account] get_api_v1_cash_account_user_userid(user_id)

Returns cash accounts for given user id

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.account import Account
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    user_id = 'e63b255b-8ece-458b-ba26-d8e77188857a' # str | 

    try:
        api_response = api_instance.get_api_v1_cash_account_user_userid(user_id)
        print("The response of CashApi->get_api_v1_cash_account_user_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->get_api_v1_cash_account_user_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[Account]**](Account.md)

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

# **get_api_v1_cash_balance_userid**
> Balances get_api_v1_cash_balance_userid(user_id)

Returns balance according to currency

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.balances import Balances
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    user_id = 'e63b255b-8ece-458b-ba26-d8e77188857a' # str | 

    try:
        api_response = api_instance.get_api_v1_cash_balance_userid(user_id)
        print("The response of CashApi->get_api_v1_cash_balance_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->get_api_v1_cash_balance_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**Balances**](Balances.md)

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

# **get_api_v1_cash_rates**
> Rates get_api_v1_cash_rates(user_country=user_country)

Returns rates according to currency in decimal format. Multiply by 100 for percentage points.

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.rates import Rates
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    user_country = 'user_country_example' # str |  (optional)

    try:
        api_response = api_instance.get_api_v1_cash_rates(user_country=user_country)
        print("The response of CashApi->get_api_v1_cash_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->get_api_v1_cash_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_country** | **str**|  | [optional] 

### Return type

[**Rates**](Rates.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: query parameter userCountry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_cash_transactions_accountid**
> Transactions get_api_v1_cash_transactions_accountid(account_id, limit=limit, offset=offset, paginate=paginate)

Get list of deposit and transaction requests

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.transactions import Transactions
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    account_id = '40117016-ac89-4690-9986-01102be1ac9b' # str | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    paginate = True # bool |  (optional)

    try:
        api_response = api_instance.get_api_v1_cash_transactions_accountid(account_id, limit=limit, offset=offset, paginate=paginate)
        print("The response of CashApi->get_api_v1_cash_transactions_accountid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->get_api_v1_cash_transactions_accountid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **paginate** | **bool**|  | [optional] 

### Return type

[**Transactions**](Transactions.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: path parameter accountId, Invalid value for: query parameter limit, Invalid value for: query parameter offset, Invalid value for: query parameter paginate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_cash_transactions_redemption_info**
> RedemptionInfo get_api_v1_cash_transactions_redemption_info()

Get redemption information

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.redemption_info import RedemptionInfo
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
    api_instance = trivium_python_sdk.CashApi(api_client)

    try:
        api_response = api_instance.get_api_v1_cash_transactions_redemption_info()
        print("The response of CashApi->get_api_v1_cash_transactions_redemption_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->get_api_v1_cash_transactions_redemption_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RedemptionInfo**](RedemptionInfo.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_cash_account**
> Account post_api_v1_cash_account(create_account_request)

Create cash account

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.account import Account
from trivium_python_sdk.models.create_account_request import CreateAccountRequest
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    create_account_request = {"userId":"952338f4-2681-4751-b8b1-82261906cd0a","accountType":"CASH","currencyCode":"SGD"} # CreateAccountRequest | Create account for this userId

    try:
        api_response = api_instance.post_api_v1_cash_account(create_account_request)
        print("The response of CashApi->post_api_v1_cash_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->post_api_v1_cash_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_account_request** | [**CreateAccountRequest**](CreateAccountRequest.md)| Create account for this userId | 

### Return type

[**Account**](Account.md)

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

# **post_api_v1_cash_events**
> SubscribeCallbackResponse post_api_v1_cash_events(subscribe_callback_request)

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
    api_instance = trivium_python_sdk.CashApi(api_client)
    subscribe_callback_request = {type=SubscribeCallbackRequestWithSignature, callbackUrl=https://myserver.com/send/callback/here} # SubscribeCallbackRequest | 

    try:
        api_response = api_instance.post_api_v1_cash_events(subscribe_callback_request)
        print("The response of CashApi->post_api_v1_cash_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->post_api_v1_cash_events: %s\n" % e)
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

# **post_api_v1_cash_request_deposit_accountid**
> DepositResponse post_api_v1_cash_request_deposit_accountid(account_id, deposit_request, x_deduplication_id=x_deduplication_id)

Create deposit request

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.deposit_request import DepositRequest
from trivium_python_sdk.models.deposit_response import DepositResponse
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    account_id = '40117016-ac89-4690-9986-01102be1ac9b' # str | 
    deposit_request = {"quantity":1007.33,"currencyCode":"SGD","transfer":{"from":{"type":"Fast","accountNumber":"111111","recipientName":"Corporate Pte. Ltd.","bank":"DBS"},"to":{"type":"Fast","accountNumber":"87654321","recipientName":"CLIENT SGD ACC","bank":"HSBC_CORP","reference":"C123456"}}} # DepositRequest | 
    x_deduplication_id = 'x_deduplication_id_example' # str | Unique value to be used for deduplication in case of network failure. Valid length is 1-64 characters. (optional)

    try:
        api_response = api_instance.post_api_v1_cash_request_deposit_accountid(account_id, deposit_request, x_deduplication_id=x_deduplication_id)
        print("The response of CashApi->post_api_v1_cash_request_deposit_accountid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->post_api_v1_cash_request_deposit_accountid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **deposit_request** | [**DepositRequest**](DepositRequest.md)|  | 
 **x_deduplication_id** | **str**| Unique value to be used for deduplication in case of network failure. Valid length is 1-64 characters. | [optional] 

### Return type

[**DepositResponse**](DepositResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** | Invalid value for X-Api-Key or Authorization HTTP header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_cash_request_redemption_accountid**
> RedemptionResponse post_api_v1_cash_request_redemption_accountid(account_id, redemption_request, x_deduplication_id=x_deduplication_id)

Create redemption request

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.redemption_request import RedemptionRequest
from trivium_python_sdk.models.redemption_response import RedemptionResponse
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    account_id = '40117016-ac89-4690-9986-01102be1ac9b' # str | 
    redemption_request = {"quantity":50.45,"currencyCode":"SGD","transferDetails":{"type":"Fast","accountNumber":"111111","recipientName":"Corporate Pte. Ltd.","bank":"DBS"}} # RedemptionRequest | 
    x_deduplication_id = 'x_deduplication_id_example' # str | Unique value to be used for deduplication in case of network failure. Valid length is 1-64 characters. (optional)

    try:
        api_response = api_instance.post_api_v1_cash_request_redemption_accountid(account_id, redemption_request, x_deduplication_id=x_deduplication_id)
        print("The response of CashApi->post_api_v1_cash_request_redemption_accountid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashApi->post_api_v1_cash_request_redemption_accountid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **redemption_request** | [**RedemptionRequest**](RedemptionRequest.md)|  | 
 **x_deduplication_id** | **str**| Unique value to be used for deduplication in case of network failure. Valid length is 1-64 characters. | [optional] 

### Return type

[**RedemptionResponse**](RedemptionResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** | Invalid value for X-Api-Key or Authorization HTTP header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v1_cash_callback**
> put_api_v1_cash_callback(cash_inbound_callback_event, x_deduplication_id=x_deduplication_id)

Cash-related callback events to be sent to Trivium

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.cash_inbound_callback_event import CashInboundCallbackEvent
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
    api_instance = trivium_python_sdk.CashApi(api_client)
    cash_inbound_callback_event = {"type":"RedemptionSettled","userId":"e63b255b-8ece-458b-ba26-d8e77188857a","amount":102.23,"currencyCode":"SGD"} # CashInboundCallbackEvent | 
    x_deduplication_id = 'x_deduplication_id_example' # str | Unique value to be used for deduplication in case of network failure. Valid length is 1-64 characters. (optional)

    try:
        api_instance.put_api_v1_cash_callback(cash_inbound_callback_event, x_deduplication_id=x_deduplication_id)
    except Exception as e:
        print("Exception when calling CashApi->put_api_v1_cash_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_inbound_callback_event** | [**CashInboundCallbackEvent**](CashInboundCallbackEvent.md)|  | 
 **x_deduplication_id** | **str**| Unique value to be used for deduplication in case of network failure. Valid length is 1-64 characters. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** | Invalid value for X-Api-Key or Authorization HTTP header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

