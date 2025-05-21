# KeyPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | key pair id | [optional] 
**reference** | **str** | custom identifier supplied for key pair that is used to link key pair to specific customer or use case | [optional] 
**asset_pool_id** | **str** | asset pool id | [optional] 
**master** | **bool** | whether this is a master key for the asset pool | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.key_pair import KeyPair

# TODO update the JSON string below
json = "{}"
# create an instance of KeyPair from a JSON string
key_pair_instance = KeyPair.from_json(json)
# print the JSON string representation of the object
print(KeyPair.to_json())

# convert the object into a dict
key_pair_dict = key_pair_instance.to_dict()
# create an instance of KeyPair from a dict
key_pair_from_dict = KeyPair.from_dict(key_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


