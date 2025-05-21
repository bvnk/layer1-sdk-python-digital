# BlockDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | blockchain number | [optional] 
**timestamp** | **datetime** | timestamp of the block | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.block_detail import BlockDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BlockDetail from a JSON string
block_detail_instance = BlockDetail.from_json(json)
# print the JSON string representation of the object
print(BlockDetail.to_json())

# convert the object into a dict
block_detail_dict = block_detail_instance.to_dict()
# create an instance of BlockDetail from a dict
block_detail_from_dict = BlockDetail.from_dict(block_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


