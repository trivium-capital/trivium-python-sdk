# trivium_python_sdk.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_transactions_userid**](TransactionsApi.md#get_api_v1_transactions_userid) | **GET** /api/v1/transactions/{userId} | 


# **get_api_v1_transactions_userid**
> PaginationResultUserTransaction get_api_v1_transactions_userid(user_id, limit=limit, offset=offset, transaction_id=transaction_id)

Get list of transactions for all products for user

### Example

* Api Key Authentication (apiKeyAuth):
* Bearer Authentication (httpAuth):

```python
import trivium_python_sdk
from trivium_python_sdk.models.pagination_result_user_transaction import PaginationResultUserTransaction
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
    api_instance = trivium_python_sdk.TransactionsApi(api_client)
    user_id = 'e63b255b-8ece-458b-ba26-d8e77188857a' # str | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    transaction_id = 'transaction_id_example' # str |  (optional)

    try:
        api_response = api_instance.get_api_v1_transactions_userid(user_id, limit=limit, offset=offset, transaction_id=transaction_id)
        print("The response of TransactionsApi->get_api_v1_transactions_userid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_api_v1_transactions_userid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **transaction_id** | **str**|  | [optional] 

### Return type

[**PaginationResultUserTransaction**](PaginationResultUserTransaction.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [httpAuth](../README.md#httpAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid value, Invalid value for: path parameter userId, Invalid value for: query parameter limit, Invalid value for: query parameter offset, Invalid value for: query parameter transactionId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

