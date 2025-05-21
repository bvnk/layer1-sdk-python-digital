# TransactionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure** | [**Failure**](Failure.md) | information about why the transaction failed | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.transaction_metadata import TransactionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMetadata from a JSON string
transaction_metadata_instance = TransactionMetadata.from_json(json)
# print the JSON string representation of the object
print(TransactionMetadata.to_json())

# convert the object into a dict
transaction_metadata_dict = transaction_metadata_instance.to_dict()
# create an instance of TransactionMetadata from a dict
transaction_metadata_from_dict = TransactionMetadata.from_dict(transaction_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


