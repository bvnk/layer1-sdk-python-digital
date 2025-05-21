# TransactionClaimRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | blockchain transaction hash | [optional] 
**network** | **str** | crypto network | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.transaction_claim_request import TransactionClaimRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionClaimRequest from a JSON string
transaction_claim_request_instance = TransactionClaimRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionClaimRequest.to_json())

# convert the object into a dict
transaction_claim_request_dict = transaction_claim_request_instance.to_dict()
# create an instance of TransactionClaimRequest from a dict
transaction_claim_request_from_dict = TransactionClaimRequest.from_dict(transaction_claim_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


