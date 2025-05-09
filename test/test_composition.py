# coding: utf-8

"""
    trivium-cash

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trivium_python_sdk.models.composition import Composition

class TestComposition(unittest.TestCase):
    """Composition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Composition:
        """Test Composition
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Composition`
        """
        model = Composition()
        if include_optional:
            return Composition(
                classes = [
                    trivium_python_sdk.models.asset_class_proportion.AssetClassProportion(
                        asset_class = 'BONDS', 
                        proportion = 1.337, )
                    ],
                funds = [
                    trivium_python_sdk.models.fund.Fund(
                        name = '', 
                        fund_id = '', 
                        description = '', 
                        proportion = 1.337, 
                        asset_class = 'BONDS', )
                    ],
                countries = [
                    trivium_python_sdk.models.country_proportion.CountryProportion(
                        country = '', 
                        proportion = 1.337, )
                    ]
            )
        else:
            return Composition(
        )
        """

    def testComposition(self):
        """Test Composition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
