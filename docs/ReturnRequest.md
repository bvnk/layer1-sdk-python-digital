# ReturnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | ID of the transaction to return | [optional] 
**destination_address** | **str** | address into which funds should be returned | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.return_request import ReturnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRequest from a JSON string
return_request_instance = ReturnRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnRequest.to_json())

# convert the object into a dict
return_request_dict = return_request_instance.to_dict()
# create an instance of ReturnRequest from a dict
return_request_from_dict = ReturnRequest.from_dict(return_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


