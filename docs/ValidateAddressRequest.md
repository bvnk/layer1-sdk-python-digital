# ValidateAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | crypto network | [optional] 
**address** | **str** | blockchain address | [optional] 
**tag** | **str** | destination tag that serves as optional payment identifier. Only applicable to select networks like Ripple, Solana etc. | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.validate_address_request import ValidateAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAddressRequest from a JSON string
validate_address_request_instance = ValidateAddressRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateAddressRequest.to_json())

# convert the object into a dict
validate_address_request_dict = validate_address_request_instance.to_dict()
# create an instance of ValidateAddressRequest from a dict
validate_address_request_from_dict = ValidateAddressRequest.from_dict(validate_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


