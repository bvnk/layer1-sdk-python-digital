# ValidateAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | whether the address is valid | [optional] 
**errors** | **List[str]** | list of error messages if the address is invalid | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.validate_address_response import ValidateAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAddressResponse from a JSON string
validate_address_response_instance = ValidateAddressResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateAddressResponse.to_json())

# convert the object into a dict
validate_address_response_dict = validate_address_response_instance.to_dict()
# create an instance of ValidateAddressResponse from a dict
validate_address_response_from_dict = ValidateAddressResponse.from_dict(validate_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


