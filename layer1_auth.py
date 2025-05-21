"""
Layer1 Authentication Module

This module provides authentication functionality for Layer1 API using RFC 9421 HTTP Message Signatures.
"""

import base64
import hashlib
import re
import time
from typing import Dict, Optional, Union
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa, utils


class Layer1Digest:
    """
    Layer1Digest provides authentication functionality for Layer1 API using RFC 9421 HTTP Message Signatures.
    """

    SIGNATURE_ALGORITHM = "rsa-v1_5-sha256"
    DIGEST_ALGORITHM = "sha-256"

    def __init__(self, signing_private_key: str, client_id: str):
        """
        Initialize Layer1Digest with a private key and client ID.

        Args:
            signing_private_key: Base64 encoded private key in PEM format
            client_id: OAuth2 Client ID
        """
        self.client_id = client_id
        
        try:
            prepared_key = self._prepare_key(signing_private_key)
            self.signing_key = serialization.load_pem_private_key(
                prepared_key.encode(),
                password=None
            )
            if not isinstance(self.signing_key, rsa.RSAPrivateKey):
                raise ValueError("Only RSA private keys are supported")
        except Exception as e:
            raise RuntimeError(f"Failed to load private key: {e}")

    def build_headers(self, url: str, payload: Optional[str], method: str) -> Dict[str, str]:
        """
        Build the necessary signature headers for RFC 9421 authentication.

        Args:
            url: The full URL of the request
            payload: The body of the request (if any)
            method: The HTTP method of the request

        Returns:
            A dictionary of headers to be added to the request
        """
        header_params = {}

        content_digest = None
        if payload:
            content_digest = self._create_digest(self.DIGEST_ALGORITHM, payload)
            header_params["Content-Digest"] = content_digest

        signature_parameters = self._create_signature_parameters(content_digest)
        header_params["Signature-Input"] = f"sig={signature_parameters}"

        signature_base = self._create_signature_base(method, url, content_digest, signature_parameters)
        signature = self._sign(signature_base)
        
        header_params["Signature"] = f"sig=:{signature}:"

        return header_params

    def _prepare_key(self, raw_key: str) -> str:
        """
        Remove the header and footer from the private key if generated via openssl etc.

        Args:
            raw_key: The raw private key string

        Returns:
            Cleaned private key string
        """
        if "-----BEGIN PRIVATE KEY-----" not in raw_key:
            return raw_key
            
        new_key = raw_key.replace("-----BEGIN PRIVATE KEY-----", "")
        new_key = new_key.replace("-----END PRIVATE KEY-----", "")
        new_key = re.sub(r"\s+", "", new_key)
        
        return f"-----BEGIN PRIVATE KEY-----\n{new_key}\n-----END PRIVATE KEY-----"

    def _create_signature_parameters(self, content_digest: Optional[str]) -> str:
        """
        Assemble the RFC 9421 signature parameters.

        Args:
            content_digest: The content digest if available

        Returns:
            Formatted signature parameters string
        """
        components = ["@method", "@target-uri"]
        if content_digest:
            components.append("content-digest")
            
        components_str = " ".join(f'"{component}"' for component in components)
        
        return f"({components_str});created={int(time.time())};keyid=\"{self.client_id}\";alg=\"{self.SIGNATURE_ALGORITHM}\""

    def _create_signature_base(self, method: str, url: str, content_digest: Optional[str], 
                              signature_parameters: str) -> str:
        """
        Create the signature base string according to RFC 9421.

        Args:
            method: HTTP method
            url: Target URL
            content_digest: Content digest if available
            signature_parameters: Signature parameters string

        Returns:
            The signature base string
        """
        lines = [
            f'"@method": {method.upper()}',
            f'"@target-uri": {url}'
        ]
        
        if content_digest:
            lines.append(f'"content-digest": {content_digest}')
            
        lines.append(f'"@signature-params": {signature_parameters}')
        
        return "\n".join(lines)

    def _create_digest(self, digest_algorithm: str, data: str) -> str:
        """
        Create and prepare the digest for the request for the content-digest header.

        Args:
            digest_algorithm: The digest algorithm to use
            data: The data to digest

        Returns:
            Formatted digest string
        """
        digest_value = self._get_digest(digest_algorithm, data)
        return f"{digest_algorithm}=:{digest_value}:"

    def _get_digest(self, algorithm: str, data: str) -> str:
        """
        Calculate the digest of the data.

        Args:
            algorithm: The digest algorithm to use
            data: The data to digest

        Returns:
            Base64 encoded digest
        """
        if algorithm == "sha-256":
            digest = hashlib.sha256(data.encode()).digest()
        else:
            raise ValueError(f"Unsupported digest algorithm: {algorithm}")
            
        return base64.b64encode(digest).decode('ascii')

    def _sign(self, signature_base: str) -> str:
        """
        Sign the request using SHA256withRSA.

        Args:
            signature_base: The base string to sign

        Returns:
            Base64 encoded signature
        """
        signature = self.signing_key.sign(
            signature_base.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature).decode('ascii')