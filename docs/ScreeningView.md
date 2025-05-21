# ScreeningView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique identifier of the transaction | [optional] 
**transaction_hash** | **str** | Blockchain transaction hash | [optional] 
**transaction_status** | **str** | Current status of the transaction | [optional] 
**network** | **str** | Network code used for the transaction | [optional] 
**transaction_metadata** | [**TransactionMetadata**](TransactionMetadata.md) | Transaction metadata in JSON format | [optional] 
**transaction_created_at** | **datetime** | Timestamp when the transaction was created | [optional] 
**transaction_updated_at** | **datetime** | Timestamp when the transaction was last updated | [optional] 
**screening_state** | **str** | Screening state of the transaction | [optional] 
**screening_reason** | **str** | Reason for the screening result | [optional] 
**screening_reason_code** | **str** | Reason code for the screening result | [optional] 
**screening_created_at** | **datetime** | Timestamp when the screening was created | [optional] 
**screening_updated_at** | **datetime** | Timestamp when the screening was last updated | [optional] 
**screening_metadata** | [**ScreeningMetadata**](ScreeningMetadata.md) | Screening metadata in JSON format | [optional] 
**participants** | [**List[Participant]**](Participant.md) | List of participants involved in the transaction | [optional] 
**operation** | **str** | Operation type for the screening | [optional] 
**address_id** | **str** | Unique identifier of the address involved in the screening | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.screening_view import ScreeningView

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningView from a JSON string
screening_view_instance = ScreeningView.from_json(json)
# print the JSON string representation of the object
print(ScreeningView.to_json())

# convert the object into a dict
screening_view_dict = screening_view_instance.to_dict()
# create an instance of ScreeningView from a dict
screening_view_from_dict = ScreeningView.from_dict(screening_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


