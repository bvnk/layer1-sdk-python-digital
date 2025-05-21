# NetworkDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**BlockDetail**](BlockDetail.md) | block detail such as number and timestamp | [optional] 
**fee** | [**AssetValue**](AssetValue.md) | network fee on the blockchain | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.network_detail import NetworkDetail

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetail from a JSON string
network_detail_instance = NetworkDetail.from_json(json)
# print the JSON string representation of the object
print(NetworkDetail.to_json())

# convert the object into a dict
network_detail_dict = network_detail_instance.to_dict()
# create an instance of NetworkDetail from a dict
network_detail_from_dict = NetworkDetail.from_dict(network_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


