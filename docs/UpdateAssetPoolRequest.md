# UpdateAssetPoolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | name of asset pool property | [optional] 
**value** | **str** | value for the property | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.update_asset_pool_request import UpdateAssetPoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetPoolRequest from a JSON string
update_asset_pool_request_instance = UpdateAssetPoolRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetPoolRequest.to_json())

# convert the object into a dict
update_asset_pool_request_dict = update_asset_pool_request_instance.to_dict()
# create an instance of UpdateAssetPoolRequest from a dict
update_asset_pool_request_from_dict = UpdateAssetPoolRequest.from_dict(update_asset_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


