# Layer1 SDK Python Digital - Usage Guide

This guide demonstrates how to use the Layer1 SDK Python Digital with the RFC 9421 authentication wrapper.

## Installation

```bash
pip install -e .
```

## Authentication

The SDK implements RFC 9421 HTTP Message Signatures for authentication. This is handled automatically by the `Layer1Client` wrapper class.

## Basic Usage

```python
from layer1_client import Layer1Client
from openapi_client.com_layer1_clients_digital_model.create_address_request import CreateAddressRequest

# Initialize the client with your credentials
client = Layer1Client(
    client_id="your-client-id",
    private_key="your-private-key-in-pem-format",
    host="https://api.layer1.com"  # Optional, defaults to staging environment
)

# Get the address API
address_api = client.get_address_api()

# Create a request
request = CreateAddressRequest(
    asset_pool_id="14a066e3-00d4-4b68-b8ee-37d385a32ad9",
    network="ETHEREUM",
    reference="my-user-id"
)

# Call the API
response = address_api.create_address(request)

# Print the response
print(f"Address created: {response.address}")
```

## Available APIs

The `Layer1Client` provides access to the following APIs:

- `get_address_api()`: For managing addresses
- `get_asset_pool_api()`: For managing asset pools
- `get_export_api()`: For exporting data
- `get_fee_api()`: For fee-related operations
- `get_key_pair_api()`: For managing key pairs
- `get_network_api()`: For network-related operations
- `get_return_api()`: For return-related operations
- `get_screening_api()`: For screening operations
- `get_transaction_api()`: For managing transactions
- `get_transaction_request_api()`: For managing transaction requests

## CLI Tool

A simple CLI tool is provided for testing purposes:

```bash
# Create an address
python example.py --client-id "your-client-id" --private-key-file "path/to/private_key.pem" create-address --payload-file "path/to/payload.json"
```

Example payload:

```json
{
    "assetPoolId": "14a066e3-00d4-4b68-b8ee-37d385a32ad9",
    "network": "ETHEREUM",
    "reference": "my-user-id"
}
```

## Authentication Details

The SDK implements RFC 9421 HTTP Message Signatures for authentication. This involves:

1. Creating a digest of the request body (if present)
2. Creating signature parameters
3. Creating a signature base string
4. Signing the base string with the private key
5. Adding the appropriate headers to the request:
   - `Content-Digest`: The digest of the request body (if present)
   - `Signature-Input`: The signature parameters
   - `Signature`: The signature itself

The `Layer1Digest` class in `layer1_auth.py` handles all of these steps automatically.

## Example: Creating an Address

```python
from layer1_client import Layer1Client
from openapi_client.com_layer1_clients_digital_model.create_address_request import CreateAddressRequest
from openapi_client.com_layer1_clients_digital_model.network import Network

# Read private key from file
with open('private_key.pem', 'r') as f:
    private_key = f.read()

# Initialize client
client = Layer1Client(
    client_id="20ff4e7d-8f1f-499f-8720-365a73e6f1f5",
    private_key=private_key
)

# Get address API
address_api = client.get_address_api()

# Create request
request = CreateAddressRequest(
    asset_pool_id="14a066e3-00d4-4b68-b8ee-37d385a32ad9",
    network="ETHEREUM",
    reference="my-user-id"
)

# Call API
try:
    response = address_api.create_address(request)
    print(f"Address created: {response.address}")
    print(f"ID: {response.id}")
    print(f"Network: {response.network}")
    print(f"Reference: {response.reference}")
except Exception as e:
    print(f"Error creating address: {e}")
```

## Example: Listing Addresses

```python
from layer1_client import Layer1Client

# Read private key from file
with open('private_key.pem', 'r') as f:
    private_key = f.read()

# Initialize client
client = Layer1Client(
    client_id="20ff4e7d-8f1f-499f-8720-365a73e6f1f5",
    private_key=private_key
)

# Get address API
address_api = client.get_address_api()

# List addresses
try:
    response = address_api.list_addresses()
    print(f"Total addresses: {response.total_elements}")
    
    for address in response.content:
        print(f"ID: {address.id}")
        print(f"Address: {address.address}")
        print(f"Network: {address.network}")
        print(f"Reference: {address.reference}")
        print("---")
except Exception as e:
    print(f"Error listing addresses: {e}")
```

## Example: Creating a Transaction

```python
from layer1_client import Layer1Client
from openapi_client.com_layer1_clients_digital_model.create_transaction_request import CreateTransactionRequest
from openapi_client.com_layer1_clients_digital_model.asset_value import AssetValue

# Read private key from file
with open('private_key.pem', 'r') as f:
    private_key = f.read()

# Initialize client
client = Layer1Client(
    client_id="20ff4e7d-8f1f-499f-8720-365a73e6f1f5",
    private_key=private_key
)

# Get transaction request API
transaction_api = client.get_transaction_request_api()

# Create request
request = CreateTransactionRequest(
    asset_pool_id="14a066e3-00d4-4b68-b8ee-37d385a32ad9",
    to_address="0x1234567890abcdef1234567890abcdef12345678",
    amount=AssetValue(
        amount="0.1",
        asset="ETH"
    ),
    reference="payment-123"
)

# Call API
try:
    response = transaction_api.create_transaction(request)
    print(f"Transaction created: {response.id}")
    print(f"Status: {response.status}")
except Exception as e:
    print(f"Error creating transaction: {e}")
```

## Error Handling

The SDK will raise exceptions for API errors. You should handle these exceptions in your code:

```python
from openapi_client.exceptions import ApiException

try:
    response = address_api.create_address(request)
    # Process response
except ApiException as e:
    if e.status == 400:
        print(f"Bad request: {e.body}")
    elif e.status == 401:
        print("Authentication failed")
    elif e.status == 404:
        print("Resource not found")
    else:
        print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```