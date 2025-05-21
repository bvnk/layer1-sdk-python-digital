# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | internal id | [optional] 
**address** | **str** | blockchain address | [optional] 
**asset_pool_id** | **str** | asset pool id | [optional] 
**network** | **str** | crypto network | [optional] 
**key_pair_id** | **str** | key pair id | [optional] 
**reference** | **str** | key pair reference | [optional] 
**supported_assets** | **List[str]** | list of assets supported by network | [optional] 
**aliases** | **List[str]** | alternative address (e.g. BTC has segwitt and legacy format) | [optional] 
**tag** | **str** | destination tag that serves as optional payment identifier. Only applicable to select networks like Ripple, Solana etc. | [optional] 
**balances** | [**List[Balance]**](Balance.md) | address balances | [optional] 
**customer_id** | **str** | custom non-unique identifier supplied for address that is used to link address to external entity like customer | [optional] 
**master** | **bool** | flag indicating whether this address is asset pool master address | [optional] 
**supported_networks** | **List[str]** | list of networks supporting given asset. mutually exclusive with network and supportedAssets | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


