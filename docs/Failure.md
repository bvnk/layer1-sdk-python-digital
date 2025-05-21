# Failure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | reason for failure | [optional] 
**message** | **str** | error message | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.failure import Failure

# TODO update the JSON string below
json = "{}"
# create an instance of Failure from a JSON string
failure_instance = Failure.from_json(json)
# print the JSON string representation of the object
print(Failure.to_json())

# convert the object into a dict
failure_dict = failure_instance.to_dict()
# create an instance of Failure from a dict
failure_from_dict = Failure.from_dict(failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


