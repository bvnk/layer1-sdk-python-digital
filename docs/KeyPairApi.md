# openapi_client.KeyPairApi

All URIs are relative to *https://api.staging.layer1.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_pair**](KeyPairApi.md#create_key_pair) | **POST** /digital/v1/key-pairs | Create key pair
[**get_key_pair**](KeyPairApi.md#get_key_pair) | **GET** /digital/v1/key-pairs/{keyPairId} | Get key pair
[**list_key_pairs**](KeyPairApi.md#list_key_pairs) | **GET** /digital/v1/key-pairs | List key pairs


# **create_key_pair**
> KeyPair create_key_pair(create_key_pair_request)

Create key pair

Creates a new key pair from which different addresses can be created

### Example

* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.create_key_pair_request import CreateKeyPairRequest
from openapi_client.models.key_pair import KeyPair
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
    api_instance = openapi_client.KeyPairApi(api_client)
    create_key_pair_request = openapi_client.CreateKeyPairRequest() # CreateKeyPairRequest | 

    try:
        # Create key pair
        api_response = api_instance.create_key_pair(create_key_pair_request)
        print("The response of KeyPairApi->create_key_pair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyPairApi->create_key_pair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_key_pair_request** | [**CreateKeyPairRequest**](CreateKeyPairRequest.md)|  | 

### Return type

[**KeyPair**](KeyPair.md)

### Authorization

[httpSignature](../README.md#httpSignature), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Service Unavailable |  -  |
**400** | Standard error response |  -  |
**201** | Created |  -  |
**0** | Request invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_pair**
> KeyPair get_key_pair(key_pair_id)

Get key pair

Retrieve a key pair given id

### Example

* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.key_pair import KeyPair
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
    api_instance = openapi_client.KeyPairApi(api_client)
    key_pair_id = 'key_pair_id_example' # str | 

    try:
        # Get key pair
        api_response = api_instance.get_key_pair(key_pair_id)
        print("The response of KeyPairApi->get_key_pair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyPairApi->get_key_pair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_pair_id** | **str**|  | 

### Return type

[**KeyPair**](KeyPair.md)

### Authorization

[httpSignature](../README.md#httpSignature), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Service Unavailable |  -  |
**400** | Standard error response |  -  |
**200** | Created |  -  |
**0** | Request invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key_pairs**
> PaginatedResultKeyPair list_key_pairs(asset_pool_id, page_number, page_size)

List key pairs

Retrieve paginated list of key-pairs belonging to a asset pool

### Example

* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.paginated_result_key_pair import PaginatedResultKeyPair
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
    api_instance = openapi_client.KeyPairApi(api_client)
    asset_pool_id = 'asset_pool_id_example' # str | 
    page_number = 0 # int |  (default to 0)
    page_size = 64 # int |  (default to 64)

    try:
        # List key pairs
        api_response = api_instance.list_key_pairs(asset_pool_id, page_number, page_size)
        print("The response of KeyPairApi->list_key_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyPairApi->list_key_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_pool_id** | **str**|  | 
 **page_number** | **int**|  | [default to 0]
 **page_size** | **int**|  | [default to 64]

### Return type

[**PaginatedResultKeyPair**](PaginatedResultKeyPair.md)

### Authorization

[httpSignature](../README.md#httpSignature), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | Service Unavailable |  -  |
**400** | Standard error response |  -  |
**200** | Created |  -  |
**0** | Request invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

