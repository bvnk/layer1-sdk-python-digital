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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.participant import Participant
from typing import Optional, Set
from typing_extensions import Self

class CreateTransactionRequest(BaseModel):
    """
    CreateTransactionRequest
    """ # noqa: E501
    asset_pool_id: Optional[StrictStr] = Field(default=None, description="asset pool id", alias="assetPoolId")
    asset: Optional[StrictStr] = Field(default=None, description="currency")
    network: Optional[StrictStr] = Field(default=None, description="crypto network")
    reference: Optional[StrictStr] = Field(default=None, description="custom identifier supplied for transaction that is used to link transaction to specific customer or use case")
    sources: Optional[List[Participant]] = Field(default=None, description="(Optional) list of addresses and amounts that fund the transaction")
    destinations: Optional[List[Participant]] = Field(default=None, description="list of recipient addresses and amounts that benefit from the transaction")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["assetPoolId", "asset", "network", "reference", "sources", "destinations"]

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
        """Create an instance of CreateTransactionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item_sources in self.sources:
                if _item_sources:
                    _items.append(_item_sources.to_dict())
            _dict['sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in destinations (list)
        _items = []
        if self.destinations:
            for _item_destinations in self.destinations:
                if _item_destinations:
                    _items.append(_item_destinations.to_dict())
            _dict['destinations'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateTransactionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assetPoolId": obj.get("assetPoolId"),
            "asset": obj.get("asset"),
            "network": obj.get("network"),
            "reference": obj.get("reference"),
            "sources": [Participant.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "destinations": [Participant.from_dict(_item) for _item in obj["destinations"]] if obj.get("destinations") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


