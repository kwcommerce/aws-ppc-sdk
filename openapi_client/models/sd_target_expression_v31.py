# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.sd_targeting_predicate_nested_v31 import SDTargetingPredicateNestedV31
from openapi_client.models.sd_targeting_predicate_v31 import SDTargetingPredicateV31
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SDTARGETEXPRESSIONV31_ONE_OF_SCHEMAS = ["SDTargetingPredicateNestedV31", "SDTargetingPredicateV31"]

class SDTargetExpressionV31(BaseModel):
    """
    SDTargetExpressionV31
    """
    # data type: SDTargetingPredicateV31
    oneof_schema_1_validator: Optional[SDTargetingPredicateV31] = None
    # data type: SDTargetingPredicateNestedV31
    oneof_schema_2_validator: Optional[SDTargetingPredicateNestedV31] = None
    actual_instance: Optional[Union[SDTargetingPredicateNestedV31, SDTargetingPredicateV31]] = None
    one_of_schemas: Set[str] = { "SDTargetingPredicateNestedV31", "SDTargetingPredicateV31" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


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
        instance = SDTargetExpressionV31.model_construct()
        error_messages = []
        match = 0
        # validate data type: SDTargetingPredicateV31
        if not isinstance(v, SDTargetingPredicateV31):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SDTargetingPredicateV31`")
        else:
            match += 1
        # validate data type: SDTargetingPredicateNestedV31
        if not isinstance(v, SDTargetingPredicateNestedV31):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SDTargetingPredicateNestedV31`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SDTargetExpressionV31 with oneOf schemas: SDTargetingPredicateNestedV31, SDTargetingPredicateV31. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SDTargetExpressionV31 with oneOf schemas: SDTargetingPredicateNestedV31, SDTargetingPredicateV31. Details: " + ", ".join(error_messages))
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

        # deserialize data into SDTargetingPredicateV31
        try:
            instance.actual_instance = SDTargetingPredicateV31.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SDTargetingPredicateNestedV31
        try:
            instance.actual_instance = SDTargetingPredicateNestedV31.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SDTargetExpressionV31 with oneOf schemas: SDTargetingPredicateNestedV31, SDTargetingPredicateV31. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SDTargetExpressionV31 with oneOf schemas: SDTargetingPredicateNestedV31, SDTargetingPredicateV31. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], SDTargetingPredicateNestedV31, SDTargetingPredicateV31]]:
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


