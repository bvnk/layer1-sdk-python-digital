# PaginatedExports


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** | total number of items in all pages | [optional] 
**content** | [**List[Export]**](Export.md) | list of items | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.paginated_exports import PaginatedExports

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExports from a JSON string
paginated_exports_instance = PaginatedExports.from_json(json)
# print the JSON string representation of the object
print(PaginatedExports.to_json())

# convert the object into a dict
paginated_exports_dict = paginated_exports_instance.to_dict()
# create an instance of PaginatedExports from a dict
paginated_exports_from_dict = PaginatedExports.from_dict(paginated_exports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


