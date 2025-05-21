# AssetPoolSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[Balance]**](Balance.md) | balances summary | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.asset_pool_summary import AssetPoolSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPoolSummary from a JSON string
asset_pool_summary_instance = AssetPoolSummary.from_json(json)
# print the JSON string representation of the object
print(AssetPoolSummary.to_json())

# convert the object into a dict
asset_pool_summary_dict = asset_pool_summary_instance.to_dict()
# create an instance of AssetPoolSummary from a dict
asset_pool_summary_from_dict = AssetPoolSummary.from_dict(asset_pool_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


