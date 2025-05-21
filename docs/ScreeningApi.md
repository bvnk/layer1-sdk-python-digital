# openapi_client.ScreeningApi

All URIs are relative to *https://api.staging.layer1.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_screenings**](ScreeningApi.md#list_screenings) | **GET** /digital/v1/screenings | List screening results
[**manually_action_held_transfer**](ScreeningApi.md#manually_action_held_transfer) | **PUT** /digital/v1/screenings/action | Approve or reject a held transfer


# **list_screenings**
> PaginatedScreenings list_screenings(page_number, page_size, hash=hash, operation=operation, state=state, start_date=start_date, end_date=end_date, sort=sort, q=q)

List screening results

Retrieves a paginated list of the most recent transfers along with their screening results.

### Example

* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.paginated_screenings import PaginatedScreenings
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.staging.layer1.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.staging.layer1.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP message signature: httpSignature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See openapi_client.signing for a list of all supported parameters.
from openapi_client import signing
import datetime

configuration = openapi_client.Configuration(
    host = "https://api.staging.layer1.com",
    signing_info = openapi_client.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = openapi_client.signing.SCHEME_HS2019,
        signing_algorithm = openapi_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = openapi_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            openapi_client.signing.HEADER_REQUEST_TARGET,
                            openapi_client.signing.HEADER_CREATED,
                            openapi_client.signing.HEADER_EXPIRES,
                            openapi_client.signing.HEADER_HOST,
                            openapi_client.signing.HEADER_DATE,
                            openapi_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScreeningApi(api_client)
    page_number = 0 # int |  (default to 0)
    page_size = 16 # int |  (default to 16)
    hash = 'hash_example' # str | Filter by transaction hash (optional)
    operation = ['operation_example'] # List[str] | Set of operations to filter by (optional)
    state = ['state_example'] # List[str] | Set of screening states to filter by (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date for filtering by transfer creation date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date for filtering by transfer creation date (optional)
    sort = 'screeningId.transfer.id.createdAt,desc' # str |  (optional) (default to 'screeningId.transfer.id.createdAt,desc')
    q = 'notReasonCode:DUST_AMOUNT' # str | Query using Lucene-like syntax. Supported properties: notReasonCode, reasonCode, reason, hash, state, operation, from, to (optional)

    try:
        # List screening results
        api_response = api_instance.list_screenings(page_number, page_size, hash=hash, operation=operation, state=state, start_date=start_date, end_date=end_date, sort=sort, q=q)
        print("The response of ScreeningApi->list_screenings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScreeningApi->list_screenings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [default to 0]
 **page_size** | **int**|  | [default to 16]
 **hash** | **str**| Filter by transaction hash | [optional] 
 **operation** | [**List[str]**](str.md)| Set of operations to filter by | [optional] 
 **state** | [**List[str]**](str.md)| Set of screening states to filter by | [optional] 
 **start_date** | **datetime**| Start date for filtering by transfer creation date | [optional] 
 **end_date** | **datetime**| End date for filtering by transfer creation date | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;screeningId.transfer.id.createdAt,desc&#39;]
 **q** | **str**| Query using Lucene-like syntax. Supported properties: notReasonCode, reasonCode, reason, hash, state, operation, from, to | [optional] 

### Return type

[**PaginatedScreenings**](PaginatedScreenings.md)

### Authorization

[httpSignature](../README.md#httpSignature), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Service Unavailable |  -  |
**400** | Bad Request |  -  |
**200** | List screenings successfully |  -  |
**0** | Request invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manually_action_held_transfer**
> manually_action_held_transfer(manual_action_request)

Approve or reject a held transfer

Approves or rejects a held transfer based on the provided transfer ID and the destination address ID. Deposits can be only approved.

### Example

* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.manual_action_request import ManualActionRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.staging.layer1.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.staging.layer1.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP message signature: httpSignature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See openapi_client.signing for a list of all supported parameters.
from openapi_client import signing
import datetime

configuration = openapi_client.Configuration(
    host = "https://api.staging.layer1.com",
    signing_info = openapi_client.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = openapi_client.signing.SCHEME_HS2019,
        signing_algorithm = openapi_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = openapi_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            openapi_client.signing.HEADER_REQUEST_TARGET,
                            openapi_client.signing.HEADER_CREATED,
                            openapi_client.signing.HEADER_EXPIRES,
                            openapi_client.signing.HEADER_HOST,
                            openapi_client.signing.HEADER_DATE,
                            openapi_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScreeningApi(api_client)
    manual_action_request = openapi_client.ManualActionRequest() # ManualActionRequest | 

    try:
        # Approve or reject a held transfer
        api_instance.manually_action_held_transfer(manual_action_request)
    except Exception as e:
        print("Exception when calling ScreeningApi->manually_action_held_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_action_request** | [**ManualActionRequest**](ManualActionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[httpSignature](../README.md#httpSignature), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Service Unavailable |  -  |
**400** | Invalid request |  -  |
**200** | Transfer reviewed successfully |  -  |
**410** | Withdrawal not found or has already been completed |  -  |
**0** | Request invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

