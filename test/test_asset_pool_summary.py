# coding: utf-8

"""
    Digital Asset

    Layer1 API making management of crypto assets simple and easy

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.com_layer1_clients_digital_model.asset_pool_summary import AssetPoolSummary

class TestAssetPoolSummary(unittest.TestCase):
    """AssetPoolSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetPoolSummary:
        """Test AssetPoolSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssetPoolSummary`
        """
        model = AssetPoolSummary()
        if include_optional:
            return AssetPoolSummary(
                balances = [
                    openapi_client.models.balance.Balance(
                        network = 'BITCOIN', 
                        asset = 'BTC', 
                        available = null, 
                        reserved = null, 
                        blockchain = null, )
                    ]
            )
        else:
            return AssetPoolSummary(
        )
        """

    def testAssetPoolSummary(self):
        """Test AssetPoolSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
