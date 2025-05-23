# coding: utf-8

"""
    Digital Asset

    Layer1 API making management of crypto assets simple and easy

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.com_layer1_clients_digital_model.estimate_transaction_fee_request import EstimateTransactionFeeRequest

class TestEstimateTransactionFeeRequest(unittest.TestCase):
    """EstimateTransactionFeeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimateTransactionFeeRequest:
        """Test EstimateTransactionFeeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimateTransactionFeeRequest`
        """
        model = EstimateTransactionFeeRequest()
        if include_optional:
            return EstimateTransactionFeeRequest(
                asset = 'USDT',
                network = 'ETHEREUM',
                sources = [
                    openapi_client.models.participant.Participant(
                        address = '0x1234567890abcdef1234567890abcdef12345678', 
                        amount = null, 
                        asset = 'ETH', 
                        tag = '123456789', )
                    ],
                destinations = [
                    openapi_client.models.participant.Participant(
                        address = '0x1234567890abcdef1234567890abcdef12345678', 
                        amount = null, 
                        asset = 'ETH', 
                        tag = '123456789', )
                    ]
            )
        else:
            return EstimateTransactionFeeRequest(
        )
        """

    def testEstimateTransactionFeeRequest(self):
        """Test EstimateTransactionFeeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
