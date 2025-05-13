# trivium_python_sdk.PaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_payments_account_accountid**](PaymentsApi.md#get_api_v1_payments_account_accountid) | **GET** /api/v1/payments/account/{accountId} | 
[**get_api_v1_payments_account_user_userid**](PaymentsApi.md#get_api_v1_payments_account_user_userid) | **GET** /api/v1/payments/account/user/{userId} | 
[**get_api_v1_payments_balances_userid**](PaymentsApi.md#get_api_v1_payments_balances_userid) | **GET** /api/v1/payments/balances/{userId} | 
[**post_api_v1_payments_account**](PaymentsApi.md#post_api_v1_payments_account) | **POST** /api/v1/payments/account | 
[**post_api_v1_payments_payout**](PaymentsApi.md#post_api_v1_payments_payout) | **POST** /api/v1/payments/payout | 
[**post_api_v1_payments_payout_approve**](PaymentsApi.md#post_api_v1_payments_payout_approve) | **POST** /api/v1/payments/payout/approve | 


# **get_api_v1_payments_account_accountid**
> PaymentsAccount get_api_v1_payments_account_accountid(account_id)



### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.payments_account import PaymentsAccount
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
    api_instance = trivium_python_sdk.PaymentsApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        api_response = api_instance.get_api_v1_payments_account_accountid(account_id)
        print("The response of PaymentsApi->get_api_v1_payments_account_accountid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_api_v1_payments_account_accountid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**PaymentsAccount**](PaymentsAccount.md)

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

# **get_api_v1_payments_account_user_userid**
> List[PaymentsAccount] get_api_v1_payments_account_user_userid(user_id)



### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.payments_account import PaymentsAccount
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
    api_instance = trivium_python_sdk.PaymentsApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_api_v1_payments_account_user_userid(user_id)
        print("The response of PaymentsApi->get_api_v1_payments_account_user_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_api_v1_payments_account_user_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[PaymentsAccount]**](PaymentsAccount.md)

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

# **get_api_v1_payments_balances_userid**
> PaymentBalances get_api_v1_payments_balances_userid(user_id)



### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.payment_balances import PaymentBalances
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
    api_instance = trivium_python_sdk.PaymentsApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_api_v1_payments_balances_userid(user_id)
        print("The response of PaymentsApi->get_api_v1_payments_balances_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_api_v1_payments_balances_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**PaymentBalances**](PaymentBalances.md)

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

# **post_api_v1_payments_account**
> PaymentsAccount post_api_v1_payments_account(create_payments_account_request)

Create payment account

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.create_payments_account_request import CreatePaymentsAccountRequest
from trivium_python_sdk.models.payments_account import PaymentsAccount
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
    api_instance = trivium_python_sdk.PaymentsApi(api_client)
    create_payments_account_request = {"userId":"22678710-8f43-4f85-8108-3d6eb87f31f9","currencyCode":"SGD","desiredBankCountry":"SG"} # CreatePaymentsAccountRequest | 

    try:
        api_response = api_instance.post_api_v1_payments_account(create_payments_account_request)
        print("The response of PaymentsApi->post_api_v1_payments_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->post_api_v1_payments_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payments_account_request** | [**CreatePaymentsAccountRequest**](CreatePaymentsAccountRequest.md)|  | 

### Return type

[**PaymentsAccount**](PaymentsAccount.md)

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

# **post_api_v1_payments_payout**
> PayoutResponse post_api_v1_payments_payout(payout_intention)

Create Payout Intention

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.payout_intention import PayoutIntention
from trivium_python_sdk.models.payout_response import PayoutResponse
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
    api_instance = trivium_python_sdk.PaymentsApi(api_client)
    payout_intention = {"type":"AdHocPayoutIntention","fromAccountId":"52ac3a7a-dc33-4ceb-b641-1a885833735e","quote":{"sellCurrency":"USD","buyCurrency":"SGD","fixedSide":"Buy","amount":721.8,"recipientBankCountry":"SG","chargeType":"OURS"},"beneficiary":{"type":"CorporateBeneficiaryDetails","companyName":"My Supplier Pte. Ltd.","address":"1 Lorong Satu, Singapore 110111","city":"Singapore","country":"SG","postalCode":"456789"},"bankAccountDetails":{"paymentType":"Swift","currency":"USD","bankName":"DBS Ltd","bankAccountHolderName":"My Supplier Pte. Ltd.","bankAccountNumber":"87654321","bankCountryCode":"SG","routingCodeType1":"BIC_SWIFT","routingCodeValue1":"DBSSSGSG"}} # PayoutIntention | 

    try:
        api_response = api_instance.post_api_v1_payments_payout(payout_intention)
        print("The response of PaymentsApi->post_api_v1_payments_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->post_api_v1_payments_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_intention** | [**PayoutIntention**](PayoutIntention.md)|  | 

### Return type

[**PayoutResponse**](PayoutResponse.md)

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

# **post_api_v1_payments_payout_approve**
> post_api_v1_payments_payout_approve(approve_payout)



### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.approve_payout import ApprovePayout
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
    api_instance = trivium_python_sdk.PaymentsApi(api_client)
    approve_payout = {"payoutIntentionId":"468c5434-5d06-4c14-893f-c7c26a6e27ca","purposeOfPayment":"GDDS","uniqueReference":"INV20240319-1192"} # ApprovePayout | 

    try:
        api_instance.post_api_v1_payments_payout_approve(approve_payout)
    except Exception as e:
        print("Exception when calling PaymentsApi->post_api_v1_payments_payout_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approve_payout** | [**ApprovePayout**](ApprovePayout.md)|  | 

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

