# Participant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | blockchain address | [optional] 
**amount** | **object** |  | [optional] 
**asset** | **str** | Optional currency if different than in parent object | [optional] 
**tag** | **str** | destination tag that serves as optional payment identifier. Only applicable to select networks like Ripple, Solana etc. | [optional] 

## Example

```python
from openapi_client.com_layer1_clients_digital_model.participant import Participant

# TODO update the JSON string below
json = "{}"
# create an instance of Participant from a JSON string
participant_instance = Participant.from_json(json)
# print the JSON string representation of the object
print(Participant.to_json())

# convert the object into a dict
participant_dict = participant_instance.to_dict()
# create an instance of Participant from a dict
participant_from_dict = Participant.from_dict(participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


