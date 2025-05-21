# PaginatedResultTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** | total number of items in all pages | [optional] 
**content** | [**List[Transaction]**](Transaction.md) | list of items | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.paginated_result_transaction import PaginatedResultTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultTransaction from a JSON string
paginated_result_transaction_instance = PaginatedResultTransaction.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultTransaction.to_json())

# convert the object into a dict
paginated_result_transaction_dict = paginated_result_transaction_instance.to_dict()
# create an instance of PaginatedResultTransaction from a dict
paginated_result_transaction_from_dict = PaginatedResultTransaction.from_dict(paginated_result_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


