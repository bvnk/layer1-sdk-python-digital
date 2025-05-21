# CreateBalanceExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | network | [optional] 
**asset** | **str** | asset | [optional] 
**networks** | **List[str]** | networks | [optional] 
**assets** | **List[str]** | assets | [optional] 
**asset_pool_id** | **str** | The ID of the asset pool for which the report will be generated. | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.create_balance_export_request import CreateBalanceExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBalanceExportRequest from a JSON string
create_balance_export_request_instance = CreateBalanceExportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBalanceExportRequest.to_json())

# convert the object into a dict
create_balance_export_request_dict = create_balance_export_request_instance.to_dict()
# create an instance of CreateBalanceExportRequest from a dict
create_balance_export_request_from_dict = CreateBalanceExportRequest.from_dict(create_balance_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


