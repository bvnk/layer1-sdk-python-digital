# CreateAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_pool_id** | **str** | asset pool id | [optional] 
**network** | **str** | crypto network | [optional] 
**asset** | **str** | crypto currency for which address(es) should be created. if network is not given will create addreses in all networks supporting given asset | [optional] 
**reference** | **str** | unique identifier for each destination that is receiving funds (whether tag or address). Similar to banking reference it is used to link deposit to a specific invoice | [optional] 
**customer_id** | **str** | custom non-unique identifier supplied for address that is used to link address to external entity like customer, merchant, company, etc. | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.create_address_request import CreateAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressRequest from a JSON string
create_address_request_instance = CreateAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAddressRequest.to_json())

# convert the object into a dict
create_address_request_dict = create_address_request_instance.to_dict()
# create an instance of CreateAddressRequest from a dict
create_address_request_from_dict = CreateAddressRequest.from_dict(create_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


