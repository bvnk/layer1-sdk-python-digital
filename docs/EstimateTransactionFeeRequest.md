# EstimateTransactionFeeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | currency | [optional] 
**network** | **str** | crypto network | [optional] 
**sources** | [**List[Participant]**](Participant.md) | (Optional) list of addresses and amounts that fund the transaction | [optional] 
**destinations** | [**List[Participant]**](Participant.md) | (Optional) list of recipient addresses and amounts that benefit from the transaction | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.estimate_transaction_fee_request import EstimateTransactionFeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateTransactionFeeRequest from a JSON string
estimate_transaction_fee_request_instance = EstimateTransactionFeeRequest.from_json(json)
# print the JSON string representation of the object
print(EstimateTransactionFeeRequest.to_json())

# convert the object into a dict
estimate_transaction_fee_request_dict = estimate_transaction_fee_request_instance.to_dict()
# create an instance of EstimateTransactionFeeRequest from a dict
estimate_transaction_fee_request_from_dict = EstimateTransactionFeeRequest.from_dict(estimate_transaction_fee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


