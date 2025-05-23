# coding: utf-8

"""
    Digital Asset

    Layer1 API making management of crypto assets simple and easy

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.com_layer1_clients_digital_model.screening_view import ScreeningView

class TestScreeningView(unittest.TestCase):
    """ScreeningView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScreeningView:
        """Test ScreeningView
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScreeningView`
        """
        model = ScreeningView()
        if include_optional:
            return ScreeningView(
                transaction_id = 'e7b67a42-ebb7-4f35-913b-29d89068e74c',
                transaction_hash = '0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
                transaction_status = 'SCREENING_PASSED',
                network = 'ETHEREUM',
                transaction_metadata = openapi_client.models.transaction_metadata.TransactionMetadata(
                    failure = openapi_client.models.failure.Failure(
                        reason = 'INSUFFICIENT_FUNDS', 
                        message = 'insufficient funds on address 0x1234567890abcdef1234567890abcdef12345678', ), ),
                transaction_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                transaction_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                screening_state = 'PENDING_SCREENING',
                screening_reason = 'Manual review required',
                screening_reason_code = 'DUST_AMOUNT',
                screening_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                screening_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                screening_metadata = openapi_client.models.screening_metadata.ScreeningMetadata(
                    urls = [
                        ''
                        ], 
                    ids = [
                        ''
                        ], ),
                participants = [
                    openapi_client.models.participant.Participant(
                        address = '0x1234567890abcdef1234567890abcdef12345678', 
                        amount = null, 
                        asset = 'ETH', 
                        tag = '123456789', )
                    ],
                operation = 'WITHDRAWAL',
                address_id = 'fefc3e7b-743b-489f-9311-0921f4930dc7'
            )
        else:
            return ScreeningView(
        )
        """

    def testScreeningView(self):
        """Test ScreeningView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
