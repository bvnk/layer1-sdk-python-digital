# PaginatedScreenings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** | total number of items in all pages | [optional] 
**content** | [**List[ScreeningView]**](ScreeningView.md) | list of items | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.paginated_screenings import PaginatedScreenings

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedScreenings from a JSON string
paginated_screenings_instance = PaginatedScreenings.from_json(json)
# print the JSON string representation of the object
print(PaginatedScreenings.to_json())

# convert the object into a dict
paginated_screenings_dict = paginated_screenings_instance.to_dict()
# create an instance of PaginatedScreenings from a dict
paginated_screenings_from_dict = PaginatedScreenings.from_dict(paginated_screenings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


