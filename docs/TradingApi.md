# trivium_python_sdk.TradingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_trading_instrument_available_userid**](TradingApi.md#get_api_v1_trading_instrument_available_userid) | **GET** /api/v1/trading/instrument/available/{userId} | 
[**get_api_v1_trading_instrument_userid_symbol**](TradingApi.md#get_api_v1_trading_instrument_userid_symbol) | **GET** /api/v1/trading/instrument/{userId}/{symbol} | 
[**get_api_v1_trading_positions_userid**](TradingApi.md#get_api_v1_trading_positions_userid) | **GET** /api/v1/trading/positions/{userId} | 
[**post_api_v1_trading_order_userid**](TradingApi.md#post_api_v1_trading_order_userid) | **POST** /api/v1/trading/order/{userId} | 


# **get_api_v1_trading_instrument_available_userid**
> List[str] get_api_v1_trading_instrument_available_userid(user_id)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
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
    api_instance = trivium_python_sdk.TradingApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_api_v1_trading_instrument_available_userid(user_id)
        print("The response of TradingApi->get_api_v1_trading_instrument_available_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->get_api_v1_trading_instrument_available_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

**List[str]**

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

# **get_api_v1_trading_instrument_userid_symbol**
> InstrumentInformation get_api_v1_trading_instrument_userid_symbol(user_id, symbol)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.instrument_information import InstrumentInformation
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
    api_instance = trivium_python_sdk.TradingApi(api_client)
    user_id = 'user_id_example' # str | 
    symbol = 'symbol_example' # str | 

    try:
        api_response = api_instance.get_api_v1_trading_instrument_userid_symbol(user_id, symbol)
        print("The response of TradingApi->get_api_v1_trading_instrument_userid_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->get_api_v1_trading_instrument_userid_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **symbol** | **str**|  | 

### Return type

[**InstrumentInformation**](InstrumentInformation.md)

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

# **get_api_v1_trading_positions_userid**
> List[Position] get_api_v1_trading_positions_userid(user_id)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.position import Position
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
    api_instance = trivium_python_sdk.TradingApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_api_v1_trading_positions_userid(user_id)
        print("The response of TradingApi->get_api_v1_trading_positions_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->get_api_v1_trading_positions_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[Position]**](Position.md)

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

# **post_api_v1_trading_order_userid**
> CreateOrderResponse post_api_v1_trading_order_userid(user_id, create_order_request)

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.create_order_request import CreateOrderRequest
from trivium_python_sdk.models.create_order_response import CreateOrderResponse
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
    api_instance = trivium_python_sdk.TradingApi(api_client)
    user_id = 'user_id_example' # str | 
    create_order_request = {"action":"BUY","order":{"type":"MarketOrder","symbol":"NVDA","quantity":12}} # CreateOrderRequest | 

    try:
        api_response = api_instance.post_api_v1_trading_order_userid(user_id, create_order_request)
        print("The response of TradingApi->post_api_v1_trading_order_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingApi->post_api_v1_trading_order_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **create_order_request** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | 

### Return type

[**CreateOrderResponse**](CreateOrderResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

