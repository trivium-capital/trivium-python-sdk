# coding: utf-8

"""
    trivium-cash

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trivium_python_sdk.models.subscribe_callback_response_public_key import SubscribeCallbackResponsePublicKey

class TestSubscribeCallbackResponsePublicKey(unittest.TestCase):
    """SubscribeCallbackResponsePublicKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscribeCallbackResponsePublicKey:
        """Test SubscribeCallbackResponsePublicKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscribeCallbackResponsePublicKey`
        """
        model = SubscribeCallbackResponsePublicKey()
        if include_optional:
            return SubscribeCallbackResponsePublicKey(
                public_key = '',
                type = 'SubscribeCallbackResponsePublicKey'
            )
        else:
            return SubscribeCallbackResponsePublicKey(
                public_key = '',
                type = 'SubscribeCallbackResponsePublicKey',
        )
        """

    def testSubscribeCallbackResponsePublicKey(self):
        """Test SubscribeCallbackResponsePublicKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
