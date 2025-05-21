# Network


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | crypto network | [optional] 
**native_asset** | **str** | native network currency | [optional] 
**supported_assets** | [**List[Asset]**](Asset.md) | list of assets supported by network | [optional] 
**tag_supported** | **bool** | whether network supports address tags | [optional] [default to False]

## Example

```python
from openapi_client.com_layer1_clients_digital_model.network import Network

# TODO update the JSON string below
json = "{}"
# create an instance of Network from a JSON string
network_instance = Network.from_json(json)
# print the JSON string representation of the object
print(Network.to_json())

# convert the object into a dict
network_dict = network_instance.to_dict()
# create an instance of Network from a dict
network_from_dict = Network.from_dict(network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


