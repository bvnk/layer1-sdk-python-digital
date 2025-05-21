# ManualActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Screening action to execute on the transfer | 
**operation** | **str** | Transaction type | 
**reason** | **str** | Reason for approving or rejecting the suspended transfer | 
**transfer_id** | **str** | Transfer identifier for which screening is performed | 
**address_id** | **str** | Specific destination address identifier for which screening is performed. Required only for deposits. | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.manual_action_request import ManualActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManualActionRequest from a JSON string
manual_action_request_instance = ManualActionRequest.from_json(json)
# print the JSON string representation of the object
print(ManualActionRequest.to_json())

# convert the object into a dict
manual_action_request_dict = manual_action_request_instance.to_dict()
# create an instance of ManualActionRequest from a dict
manual_action_request_from_dict = ManualActionRequest.from_dict(manual_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


