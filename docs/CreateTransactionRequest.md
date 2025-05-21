# CreateTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_pool_id** | **str** | asset pool id | [optional] 
**asset** | **str** | currency | [optional] 
**network** | **str** | crypto network | [optional] 
**reference** | **str** | custom identifier supplied for transaction that is used to link transaction to specific customer or use case | [optional] 
**sources** | [**List[Participant]**](Participant.md) | (Optional) list of addresses and amounts that fund the transaction | [optional] 
**destinations** | [**List[Participant]**](Participant.md) | list of recipient addresses and amounts that benefit from the transaction | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.create_transaction_request import CreateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransactionRequest from a JSON string
create_transaction_request_instance = CreateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTransactionRequest.to_json())

# convert the object into a dict
create_transaction_request_dict = create_transaction_request_instance.to_dict()
# create an instance of CreateTransactionRequest from a dict
create_transaction_request_from_dict = CreateTransactionRequest.from_dict(create_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


