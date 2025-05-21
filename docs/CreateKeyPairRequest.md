# CreateKeyPairRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_pool_id** | **str** | asset pool id | [optional] 
**reference** | **str** | custom identifier supplied for key pair that is used to link key pair to specific customer or use case | [optional] 
**master** | **bool** | whether this is a master key for the asset pool | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.create_key_pair_request import CreateKeyPairRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyPairRequest from a JSON string
create_key_pair_request_instance = CreateKeyPairRequest.from_json(json)
# print the JSON string representation of the object
print(CreateKeyPairRequest.to_json())

# convert the object into a dict
create_key_pair_request_dict = create_key_pair_request_instance.to_dict()
# create an instance of CreateKeyPairRequest from a dict
create_key_pair_request_from_dict = CreateKeyPairRequest.from_dict(create_key_pair_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


