# Balance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | network | [optional] 
**asset** | **str** | asset | [optional] 
**available** | **object** |  | [optional] 
**reserved** | **object** |  | [optional] 
**blockchain** | **object** |  | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.balance import Balance

# TODO update the JSON string below
json = "{}"
# create an instance of Balance from a JSON string
balance_instance = Balance.from_json(json)
# print the JSON string representation of the object
print(Balance.to_json())

# convert the object into a dict
balance_dict = balance_instance.to_dict()
# create an instance of Balance from a dict
balance_from_dict = Balance.from_dict(balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


