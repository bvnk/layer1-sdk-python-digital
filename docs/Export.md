# Export


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the export | [optional] 
**status** | **str** | Current status of the export job | [optional] 
**type** | **str** | Export type name | [optional] 
**input_parameters** | **Dict[str, str]** | JSON string containing input parameters for the job | [optional] 
**filename** | **str** | Filename of the resulting export | [optional] 
**url** | **str** | URL for file download | [optional] 
**created_at** | **datetime** | Timestamp when the export was created | [optional] 
**updated_at** | **datetime** | Timestamp when the export was last updated | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.export import Export

# TODO update the JSON string below
json = "{}"
# create an instance of Export from a JSON string
export_instance = Export.from_json(json)
# print the JSON string representation of the object
print(Export.to_json())

# convert the object into a dict
export_dict = export_instance.to_dict()
# create an instance of Export from a dict
export_from_dict = Export.from_dict(export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


