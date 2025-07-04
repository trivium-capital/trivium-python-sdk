# coding: utf-8

"""
    trivium-cash

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from trivium_python_sdk.models.cash_deposit import CashDeposit
from trivium_python_sdk.models.cash_redemption import CashRedemption
from trivium_python_sdk.models.fixed_deposit_redemption import FixedDepositRedemption
from trivium_python_sdk.models.fixed_deposit_transfer import FixedDepositTransfer
from trivium_python_sdk.models.payment_incoming import PaymentIncoming
from trivium_python_sdk.models.payment_outgoing import PaymentOutgoing
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

USERTRANSACTION_ONE_OF_SCHEMAS = ["CashDeposit", "CashRedemption", "FixedDepositRedemption", "FixedDepositTransfer", "PaymentIncoming", "PaymentOutgoing"]

class UserTransaction(BaseModel):
    """
    UserTransaction
    """
    # data type: CashDeposit
    oneof_schema_1_validator: Optional[CashDeposit] = None
    # data type: CashRedemption
    oneof_schema_2_validator: Optional[CashRedemption] = None
    # data type: FixedDepositRedemption
    oneof_schema_3_validator: Optional[FixedDepositRedemption] = None
    # data type: FixedDepositTransfer
    oneof_schema_4_validator: Optional[FixedDepositTransfer] = None
    # data type: PaymentIncoming
    oneof_schema_5_validator: Optional[PaymentIncoming] = None
    # data type: PaymentOutgoing
    oneof_schema_6_validator: Optional[PaymentOutgoing] = None
    actual_instance: Optional[Union[CashDeposit, CashRedemption, FixedDepositRedemption, FixedDepositTransfer, PaymentIncoming, PaymentOutgoing]] = None
    one_of_schemas: Set[str] = { "CashDeposit", "CashRedemption", "FixedDepositRedemption", "FixedDepositTransfer", "PaymentIncoming", "PaymentOutgoing" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = UserTransaction.model_construct()
        error_messages = []
        match = 0
        # validate data type: CashDeposit
        if not isinstance(v, CashDeposit):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CashDeposit`")
        else:
            match += 1
        # validate data type: CashRedemption
        if not isinstance(v, CashRedemption):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CashRedemption`")
        else:
            match += 1
        # validate data type: FixedDepositRedemption
        if not isinstance(v, FixedDepositRedemption):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FixedDepositRedemption`")
        else:
            match += 1
        # validate data type: FixedDepositTransfer
        if not isinstance(v, FixedDepositTransfer):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FixedDepositTransfer`")
        else:
            match += 1
        # validate data type: PaymentIncoming
        if not isinstance(v, PaymentIncoming):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentIncoming`")
        else:
            match += 1
        # validate data type: PaymentOutgoing
        if not isinstance(v, PaymentOutgoing):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaymentOutgoing`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UserTransaction with oneOf schemas: CashDeposit, CashRedemption, FixedDepositRedemption, FixedDepositTransfer, PaymentIncoming, PaymentOutgoing. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UserTransaction with oneOf schemas: CashDeposit, CashRedemption, FixedDepositRedemption, FixedDepositTransfer, PaymentIncoming, PaymentOutgoing. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into CashDeposit
        try:
            instance.actual_instance = CashDeposit.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CashRedemption
        try:
            instance.actual_instance = CashRedemption.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FixedDepositRedemption
        try:
            instance.actual_instance = FixedDepositRedemption.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FixedDepositTransfer
        try:
            instance.actual_instance = FixedDepositTransfer.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaymentIncoming
        try:
            instance.actual_instance = PaymentIncoming.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PaymentOutgoing
        try:
            instance.actual_instance = PaymentOutgoing.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UserTransaction with oneOf schemas: CashDeposit, CashRedemption, FixedDepositRedemption, FixedDepositTransfer, PaymentIncoming, PaymentOutgoing. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UserTransaction with oneOf schemas: CashDeposit, CashRedemption, FixedDepositRedemption, FixedDepositTransfer, PaymentIncoming, PaymentOutgoing. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CashDeposit, CashRedemption, FixedDepositRedemption, FixedDepositTransfer, PaymentIncoming, PaymentOutgoing]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


