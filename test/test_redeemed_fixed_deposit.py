# coding: utf-8

"""
    trivium-cash

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trivium_python_sdk.models.redeemed_fixed_deposit import RedeemedFixedDeposit

class TestRedeemedFixedDeposit(unittest.TestCase):
    """RedeemedFixedDeposit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RedeemedFixedDeposit:
        """Test RedeemedFixedDeposit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RedeemedFixedDeposit`
        """
        model = RedeemedFixedDeposit()
        if include_optional:
            return RedeemedFixedDeposit(
                placement_id = '',
                invested_quantity = 1.337,
                redeemed_value = 1.337,
                currency_code = '',
                provider_details = trivium_python_sdk.models.provider_details.ProviderDetails(
                    provider = '', 
                    product_name = '', 
                    product_distinction = '', 
                    currency_code = '', 
                    returns = 1.337, ),
                term = '',
                redemption_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                return_at_maturity = 1.337,
                locked_rate = 1.337,
                type = 'RedeemedFixedDeposit'
            )
        else:
            return RedeemedFixedDeposit(
                placement_id = '',
                invested_quantity = 1.337,
                redeemed_value = 1.337,
                currency_code = '',
                provider_details = trivium_python_sdk.models.provider_details.ProviderDetails(
                    provider = '', 
                    product_name = '', 
                    product_distinction = '', 
                    currency_code = '', 
                    returns = 1.337, ),
                term = '',
                redemption_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                return_at_maturity = 1.337,
                locked_rate = 1.337,
                type = 'RedeemedFixedDeposit',
        )
        """

    def testRedeemedFixedDeposit(self):
        """Test RedeemedFixedDeposit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
