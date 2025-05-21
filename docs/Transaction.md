# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | transaction id | [optional] 
**address** | [**Address**](Address.md) | address involved in the transaction | [optional] 
**reference** | **str** | custom identifier supplied for transaction that is used to link transaction to specific customer or use case | [optional] 
**status** | **str** | transaction status | [optional] 
**sources** | [**List[Participant]**](Participant.md) | list of addresses and amounts that fund the transaction | [optional] 
**destinations** | [**List[Participant]**](Participant.md) | list of recipient addresses and amounts that benefit from the transaction | [optional] 
**type** | **str** | transaction type | [optional] 
**asset** | **str** | currency | [optional] 
**amount** | **object** |  | [optional] 
**hash** | **str** | blockchain transaction hash | [optional] 
**network_detail** | [**NetworkDetail**](NetworkDetail.md) | network details of the transaction | [optional] 
**metadata** | [**TransactionMetadata**](TransactionMetadata.md) | metadata about the transaction | [optional] 
**created_at** | **datetime** | timestamp when transaction was created | [optional] 
**updated_at** | **datetime** | timestamp when transaction was updated | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


