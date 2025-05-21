# TransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | transaction request id | [optional] 
**asset** | **str** | currency | [optional] 
**asset_pool_id** | **str** | asset pool id | [optional] 
**network** | **str** | crypto network | [optional] 
**reference** | **str** | custom identifier supplied for transaction that is used to link transaction to specific customer or use case | [optional] 
**status** | **str** | transaction request status | [optional] 
**sources** | [**List[Participant]**](Participant.md) | requested list of addresses and amounts that fund the transaction | [optional] 
**destinations** | [**List[Participant]**](Participant.md) | requested list of recipient addresses and amounts that benefit from the transaction | [optional] 
**type** | **str** | transaction request type | [optional] 
**created_at** | **datetime** | timestamp when transaction request was created | [optional] 
**updated_at** | **datetime** | timestamp when transaction request was updated | [optional] 
**failure** | [**Failure**](Failure.md) | failure details | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.transaction_request import TransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequest from a JSON string
transaction_request_instance = TransactionRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionRequest.to_json())

# convert the object into a dict
transaction_request_dict = transaction_request_instance.to_dict()
# create an instance of TransactionRequest from a dict
transaction_request_from_dict = TransactionRequest.from_dict(transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


