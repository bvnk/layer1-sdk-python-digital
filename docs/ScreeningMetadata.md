# ScreeningMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** | URLs to external screening providers relevant to the deposit | [optional] 
**ids** | **List[str]** | Deposit screening identifiers within external screening providers | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.screening_metadata import ScreeningMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningMetadata from a JSON string
screening_metadata_instance = ScreeningMetadata.from_json(json)
# print the JSON string representation of the object
print(ScreeningMetadata.to_json())

# convert the object into a dict
screening_metadata_dict = screening_metadata_instance.to_dict()
# create an instance of ScreeningMetadata from a dict
screening_metadata_from_dict = ScreeningMetadata.from_dict(screening_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


