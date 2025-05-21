"""
Layer1 Client Wrapper

This module provides a wrapper for the Layer1 API client that handles authentication.
"""

from typing import Dict, Optional, Any, Type, TypeVar, Union
import urllib.parse

from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.com_layer1_clients_digital_api.address_api import AddressApi
from openapi_client.com_layer1_clients_digital_api.asset_pool_api import AssetPoolApi
from openapi_client.com_layer1_clients_digital_api.export_api import ExportApi
from openapi_client.com_layer1_clients_digital_api.fee_api import FeeApi
from openapi_client.com_layer1_clients_digital_api.key_pair_api import KeyPairApi
from openapi_client.com_layer1_clients_digital_api.network_api import NetworkApi
from openapi_client.com_layer1_clients_digital_api.return_api import ReturnApi
from openapi_client.com_layer1_clients_digital_api.screening_api import ScreeningApi
from openapi_client.com_layer1_clients_digital_api.transaction_api import TransactionApi
from openapi_client.com_layer1_clients_digital_api.transaction_request_api import TransactionRequestApi

from layer1_auth import Layer1Digest

T = TypeVar('T')


class Layer1Client:
    """
    Layer1Client is a wrapper for the Layer1 API client that handles authentication.
    """

    def __init__(self, client_id: str, private_key: str, host: Optional[str] = None):
        """
        Initialize Layer1Client with authentication credentials.

        Args:
            client_id: OAuth2 Client ID
            private_key: Private key in PEM format
            host: API host URL (optional, defaults to staging environment)
        """
        self.client_id = client_id
        self.private_key = private_key
        self.digest = Layer1Digest(private_key, client_id)
        
        # Create configuration
        self.configuration = Configuration()
        if host:
            self.configuration.host = host
            
        # Create API client
        self.api_client = ApiClient(self.configuration)
        
        # Override the call_api method to add authentication headers
        self._original_call_api = self.api_client.call_api
        self.api_client.call_api = self._call_api_with_auth
        
    def _call_api_with_auth(self, method, url, header_params=None, body=None, 
                           post_params=None, _request_timeout=None) -> Any:
        """
        Wrapper for call_api that adds authentication headers.

        Args:
            method: HTTP method
            url: URL to call
            header_params: HTTP headers
            body: Request body
            post_params: POST parameters
            _request_timeout: Request timeout

        Returns:
            API response
        """
        if header_params is None:
            header_params = {}
            
        # Convert body to string if it exists
        body_str = None
        if body is not None:
            body_str = str(body)
            
        # Build authentication headers
        auth_headers = self.digest.build_headers(url, body_str, method)
        
        # Add authentication headers to request
        header_params.update(auth_headers)
        
        # Call original method
        return self._original_call_api(
            method, url, header_params, body, post_params, _request_timeout
        )
        
    def get_address_api(self) -> AddressApi:
        """Get AddressApi instance with authentication."""
        return AddressApi(self.api_client)
        
    def get_asset_pool_api(self) -> AssetPoolApi:
        """Get AssetPoolApi instance with authentication."""
        return AssetPoolApi(self.api_client)
        
    def get_export_api(self) -> ExportApi:
        """Get ExportApi instance with authentication."""
        return ExportApi(self.api_client)
        
    def get_fee_api(self) -> FeeApi:
        """Get FeeApi instance with authentication."""
        return FeeApi(self.api_client)
        
    def get_key_pair_api(self) -> KeyPairApi:
        """Get KeyPairApi instance with authentication."""
        return KeyPairApi(self.api_client)
        
    def get_network_api(self) -> NetworkApi:
        """Get NetworkApi instance with authentication."""
        return NetworkApi(self.api_client)
        
    def get_return_api(self) -> ReturnApi:
        """Get ReturnApi instance with authentication."""
        return ReturnApi(self.api_client)
        
    def get_screening_api(self) -> ScreeningApi:
        """Get ScreeningApi instance with authentication."""
        return ScreeningApi(self.api_client)
        
    def get_transaction_api(self) -> TransactionApi:
        """Get TransactionApi instance with authentication."""
        return TransactionApi(self.api_client)
        
    def get_transaction_request_api(self) -> TransactionRequestApi:
        """Get TransactionRequestApi instance with authentication."""
        return TransactionRequestApi(self.api_client)