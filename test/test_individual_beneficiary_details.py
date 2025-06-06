# coding: utf-8

"""
    trivium-cash

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.8.dev0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trivium_python_sdk.models.individual_beneficiary_details import IndividualBeneficiaryDetails

class TestIndividualBeneficiaryDetails(unittest.TestCase):
    """IndividualBeneficiaryDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IndividualBeneficiaryDetails:
        """Test IndividualBeneficiaryDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IndividualBeneficiaryDetails`
        """
        model = IndividualBeneficiaryDetails()
        if include_optional:
            return IndividualBeneficiaryDetails(
                first_name = '',
                last_name = '',
                address = '',
                city = '',
                state = '',
                country = '',
                postal_code = '',
                type = 'IndividualBeneficiaryDetails'
            )
        else:
            return IndividualBeneficiaryDetails(
                first_name = '',
                last_name = '',
                address = '',
                city = '',
                country = '',
                type = 'IndividualBeneficiaryDetails',
        )
        """

    def testIndividualBeneficiaryDetails(self):
        """Test IndividualBeneficiaryDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
