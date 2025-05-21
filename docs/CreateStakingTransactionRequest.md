# CreateStakingTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_pool_id** | **str** | asset pool id | [optional] 
**asset** | **str** | currency | [optional] 
**network** | **str** | crypto network | [optional] 
**type** | **str** |  | [optional] 
**reference** | **str** | custom identifier supplied for transaction that is used to link transaction to specific customer or use case | [optional] 
**address** | **str** | blockchain address | [optional] 
**amount** | **object** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.create_staking_transaction_request import CreateStakingTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStakingTransactionRequest from a JSON string
create_staking_transaction_request_instance = CreateStakingTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateStakingTransactionRequest.to_json())

# convert the object into a dict
create_staking_transaction_request_dict = create_staking_transaction_request_instance.to_dict()
# create an instance of CreateStakingTransactionRequest from a dict
create_staking_transaction_request_from_dict = CreateStakingTransactionRequest.from_dict(create_staking_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


