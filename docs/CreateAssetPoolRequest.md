# CreateAssetPoolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of asset pool | [optional] 
**reference** | **str** | custom supplied identifier for asset pool. Also used to initialise master key pair | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.create_asset_pool_request import CreateAssetPoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetPoolRequest from a JSON string
create_asset_pool_request_instance = CreateAssetPoolRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAssetPoolRequest.to_json())

# convert the object into a dict
create_asset_pool_request_dict = create_asset_pool_request_instance.to_dict()
# create an instance of CreateAssetPoolRequest from a dict
create_asset_pool_request_from_dict = CreateAssetPoolRequest.from_dict(create_asset_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


