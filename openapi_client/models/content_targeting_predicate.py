# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ContentTargetingPredicate(BaseModel):
    """
    A predicate to match against in the content targeting expression.
    """ # noqa: E501
    type: Optional[StrictStr] = None
    value: Optional[StrictStr] = Field(default=None, description="The value to be targeted.  The following table shows all possible values of the `contentCategorySameAs` predicate. | Category              | Subcategory                             | Value                    | |-----------------------|-----------------------------------------|--------------------------| | Movies and Television | All Movies and Television               | amzn1.iab-content.SPSHQ5 | | Movies and Television | Action or Adventure                     | amzn1.iab-content.325    | | Movies and Television | Animation or Anime                      | amzn1.iab-content.641    | | Movies and Television | Biographies                             | amzn1.iab-content.44     | | Movies and Television | Comedy                                  | amzn1.iab-content.646    | | Movies and Television | Documentary                             | amzn1.iab-content.332    | | Movies and Television | Drama                                   | amzn1.iab-content.647    | | Movies and Television | Factual                                 | amzn1.iab-content.648    | | Movies and Television | Family                                  | amzn1.iab-content.645    | | Movies and Television | Fantasy                                 | amzn1.iab-content.335    | | Movies and Television | History                                 | amzn1.iab-content.EZWB7V | | Movies and Television | Holiday                                 | amzn1.iab-content.649    | | Movies and Television | Horror                                  | amzn1.iab-content.336    | | Movies and Television | Lifestyle                               | amzn1.iab-content.TIFQA5 | | Movies and Television | Music Video                             | amzn1.iab-content.650    | | Movies and Television | Musicals                                | amzn1.iab-content.156    | | Movies and Television | Mystery                                 | amzn1.iab-content.331    | | Movies and Television | Reality TV                              | amzn1.iab-content.651    | | Movies and Television | Romance                                 | amzn1.iab-content.326    | | Movies and Television | Science Fiction                         | amzn1.iab-content.652    | | Movies and Television | Soap Opera                              | amzn1.iab-content.642    | | Movies and Television | Special Interest (Indie or Art House)   | amzn1.iab-content.643    | | Movies and Television | Sports Radio                            | amzn1.iab-content.370    | | Movies and Television | Talk Show                               | amzn1.iab-content.A0AH3G | | Movies and Television | True Crime                              | amzn1.iab-content.KHPC5A | | Movies and Television | Western                                 | amzn1.iab-content.KHPC6A | | Music and Radio       | All Music and Radio                     | amzn1.iab-content.338    | | Music and Radio       | Blues                                   | amzn1.iab-content.360    | | Music and Radio       | Classical Music                         | amzn1.iab-content.346    | | Music and Radio       | Comedy (Music and Audio)                | amzn1.iab-content.348    | | Music and Radio       | Pop, Contemporary Hits, or Top 40 Music | amzn1.iab-content.349    | | Music and Radio       | Country Music                           | amzn1.iab-content.350    | | Music and Radio       | Dance and Electronic Music              | amzn1.iab-content.351    | | Music and Radio       | Hip Hop Music                           | amzn1.iab-content.355    | | Music and Radio       | Inspirational or New Age Music          | amzn1.iab-content.356    | | Music and Radio       | Jazz                                    | amzn1.iab-content.357    | | Music and Radio       | Oldies or Adult Standards               | amzn1.iab-content.358    | | Music and Radio       | R&B, Soul or Funk Music                 | amzn1.iab-content.362    | | Music and Radio       | Reggae                                  | amzn1.iab-content.359    | | Music and Radio       | Rock Music                              | amzn1.iab-content.363    | | Music and Radio       | Songwriters or Folk                     | amzn1.iab-content.353    | | Music and Radio       | World or International Music            | amzn1.iab-content.352    | | Video Games           | All Video Games                         | amzn1.iab-content.680    | | Video Games           | Action-Adventure Games                  | amzn1.iab-content.691    | | Video Games           | Casual Games                            | amzn1.iab-content.693    | | Video Games           | Puzzle Video Games                      | amzn1.iab-content.698    | | Video Games           | Racing Video Games                      | amzn1.iab-content.VK7KD0 | | Video Games           | Role-Playing Video Games                | amzn1.iab-content.687    | | Video Games           | Simulation Video Games                  | amzn1.iab-content.688    | | Video Games           | Sports Video Games                      | amzn1.iab-content.689    | | Video Games           | Strategy Video Games                    | amzn1.iab-content.690    | | Video Games           | PC Games                                | amzn1.iab-content.684    | | Video Games           | Mobile Games                            | amzn1.iab-content.683    | | Video Games           | Console Games                           | amzn1.iab-content.681    | | Video Games           | eSports                                 | amzn1.iab-content.682    |")
    __properties: ClassVar[List[str]] = ["type", "value"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['contentCategorySameAs']):
            raise ValueError("must be one of enum values ('contentCategorySameAs')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ContentTargetingPredicate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentTargetingPredicate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "value": obj.get("value")
        })
        return _obj

