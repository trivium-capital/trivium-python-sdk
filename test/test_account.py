# coding: utf-8

"""
    trivium-cash

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trivium_python_sdk.models.account import Account

class TestAccount(unittest.TestCase):
    """Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Account:
        """Test Account
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Account`
        """
        model = Account()
        if include_optional:
            return Account(
                account_id = '',
                account_type = 'CASH',
                currency_code = '',
                status = 'ACTIVE',
                provider = trivium_python_sdk.models.provider_details.ProviderDetails(
                    provider = '', 
                    product_name = '', 
                    product_distinction = '', 
                    currency_code = '', 
                    returns = 1.337, ),
                earnings_to_date = trivium_python_sdk.models.earnings_to_date.EarningsToDate(
                    earnings = 1.337, 
                    time_weighted_return_decimal = 1.337, ),
                balance = trivium_python_sdk.models.balance.Balance(
                    total_balance = 1.337, 
                    available_balance = 1.337, ),
                deposit_instructions = trivium_python_sdk.models.deposit_instructions.DepositInstructions(
                    local = [
                        null
                        ], 
                    global = [
                        null
                        ], )
            )
        else:
            return Account(
                account_id = '',
                account_type = 'CASH',
                currency_code = '',
                status = 'ACTIVE',
                provider = trivium_python_sdk.models.provider_details.ProviderDetails(
                    provider = '', 
                    product_name = '', 
                    product_distinction = '', 
                    currency_code = '', 
                    returns = 1.337, ),
                earnings_to_date = trivium_python_sdk.models.earnings_to_date.EarningsToDate(
                    earnings = 1.337, 
                    time_weighted_return_decimal = 1.337, ),
                balance = trivium_python_sdk.models.balance.Balance(
                    total_balance = 1.337, 
                    available_balance = 1.337, ),
                deposit_instructions = trivium_python_sdk.models.deposit_instructions.DepositInstructions(
                    local = [
                        null
                        ], 
                    global = [
                        null
                        ], ),
        )
        """

    def testAccount(self):
        """Test Account"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
