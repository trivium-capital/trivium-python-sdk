# coding: utf-8

"""
    trivium-cash

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trivium_python_sdk.models.performance_snapshot import PerformanceSnapshot

class TestPerformanceSnapshot(unittest.TestCase):
    """PerformanceSnapshot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PerformanceSnapshot:
        """Test PerformanceSnapshot
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PerformanceSnapshot`
        """
        model = PerformanceSnapshot()
        if include_optional:
            return PerformanceSnapshot(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                nav = 1.337,
                twr = 1.337
            )
        else:
            return PerformanceSnapshot(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                nav = 1.337,
                twr = 1.337,
        )
        """

    def testPerformanceSnapshot(self):
        """Test PerformanceSnapshot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
