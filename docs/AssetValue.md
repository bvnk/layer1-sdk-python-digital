# AssetValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **object** |  | [optional] 
**asset** | **str** | currency | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.asset_value import AssetValue

# TODO update the JSON string below
json = "{}"
# create an instance of AssetValue from a JSON string
asset_value_instance = AssetValue.from_json(json)
# print the JSON string representation of the object
print(AssetValue.to_json())

# convert the object into a dict
asset_value_dict = asset_value_instance.to_dict()
# create an instance of AssetValue from a dict
asset_value_from_dict = AssetValue.from_dict(asset_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


