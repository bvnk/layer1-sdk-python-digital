# coding: utf-8

"""
    Digital Asset

    Layer1 API making management of crypto assets simple and easy

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Balance(BaseModel):
    """
    Balance
    """ # noqa: E501
    network: Optional[StrictStr] = Field(default=None, description="network")
    asset: Optional[StrictStr] = Field(default=None, description="asset")
    available: Optional[Any] = None
    reserved: Optional[Any] = None
    blockchain: Optional[Any] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["network", "asset", "available", "reserved", "blockchain"]

    @field_validator('network')
    def network_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BASE', 'BINANCE', 'BITCOIN', 'BITCOIN_CASH', 'DOGECOIN', 'ETHEREUM', 'LITECOIN', 'POLYGON', 'RIPPLE', 'SOLANA', 'TRON', 'unknown_default_open_api']):
            raise ValueError("must be one of enum values ('BASE', 'BINANCE', 'BITCOIN', 'BITCOIN_CASH', 'DOGECOIN', 'ETHEREUM', 'LITECOIN', 'POLYGON', 'RIPPLE', 'SOLANA', 'TRON', 'unknown_default_open_api')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Balance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if available (nullable) is None
        # and model_fields_set contains the field
        if self.available is None and "available" in self.model_fields_set:
            _dict['available'] = None

        # set to None if reserved (nullable) is None
        # and model_fields_set contains the field
        if self.reserved is None and "reserved" in self.model_fields_set:
            _dict['reserved'] = None

        # set to None if blockchain (nullable) is None
        # and model_fields_set contains the field
        if self.blockchain is None and "blockchain" in self.model_fields_set:
            _dict['blockchain'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Balance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "network": obj.get("network"),
            "asset": obj.get("asset"),
            "available": obj.get("available"),
            "reserved": obj.get("reserved"),
            "blockchain": obj.get("blockchain")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


