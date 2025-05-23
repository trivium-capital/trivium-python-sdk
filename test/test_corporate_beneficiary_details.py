# coding: utf-8

"""
    trivium-cash

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.8.dev0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trivium_python_sdk.models.corporate_beneficiary_details import CorporateBeneficiaryDetails

class TestCorporateBeneficiaryDetails(unittest.TestCase):
    """CorporateBeneficiaryDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CorporateBeneficiaryDetails:
        """Test CorporateBeneficiaryDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CorporateBeneficiaryDetails`
        """
        model = CorporateBeneficiaryDetails()
        if include_optional:
            return CorporateBeneficiaryDetails(
                company_name = '',
                address = '',
                city = '',
                country = '',
                state = '',
                postal_code = '',
                type = 'CorporateBeneficiaryDetails'
            )
        else:
            return CorporateBeneficiaryDetails(
                company_name = '',
                address = '',
                city = '',
                country = '',
                type = 'CorporateBeneficiaryDetails',
        )
        """

    def testCorporateBeneficiaryDetails(self):
        """Test CorporateBeneficiaryDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
