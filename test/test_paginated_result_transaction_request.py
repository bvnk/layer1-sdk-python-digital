# coding: utf-8

"""
    Digital Asset

    Layer1 API making management of crypto assets simple and easy

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.com_layer1_clients_digital_model.paginated_result_transaction_request import PaginatedResultTransactionRequest

class TestPaginatedResultTransactionRequest(unittest.TestCase):
    """PaginatedResultTransactionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedResultTransactionRequest:
        """Test PaginatedResultTransactionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedResultTransactionRequest`
        """
        model = PaginatedResultTransactionRequest()
        if include_optional:
            return PaginatedResultTransactionRequest(
                total_elements = 56,
                content = [
                    openapi_client.models.transaction_request.TransactionRequest(
                        request_id = '', 
                        asset = 'USDT', 
                        asset_pool_id = '', 
                        network = 'ETHEREUM', 
                        reference = 'myUniqueRef333', 
                        status = 'BLOCKED', 
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
                            ], 
                        type = 'DEPOSIT', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        failure = openapi_client.models.failure.Failure(
                            reason = 'INSUFFICIENT_FUNDS', 
                            message = 'insufficient funds on address 0x1234567890abcdef1234567890abcdef12345678', ), )
                    ],
                pageable = openapi_client.models.pageable.Pageable(
                    page_number = 56, 
                    page_size = 56, )
            )
        else:
            return PaginatedResultTransactionRequest(
        )
        """

    def testPaginatedResultTransactionRequest(self):
        """Test PaginatedResultTransactionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
