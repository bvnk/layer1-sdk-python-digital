# PaginatedResultAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** | total number of items in all pages | [optional] 
**content** | [**List[Address]**](Address.md) | list of items | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.paginated_result_address import PaginatedResultAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultAddress from a JSON string
paginated_result_address_instance = PaginatedResultAddress.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultAddress.to_json())

# convert the object into a dict
paginated_result_address_dict = paginated_result_address_instance.to_dict()
# create an instance of PaginatedResultAddress from a dict
paginated_result_address_from_dict = PaginatedResultAddress.from_dict(paginated_result_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


