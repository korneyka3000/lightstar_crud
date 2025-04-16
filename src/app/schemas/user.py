__all__ = (
    "UserInStructDTO",
    "UserOutStructDTO",
)


import msgspec

from src.utils import PasswordManager
from src.utils.schemas.types import DTAware, PositiveIntMsgSpec


class UserInStructDTO(msgspec.Struct, forbid_unknown_fields=True):
    name: str
    surname: str
    password: str  # TODO add validation

    def __post_init__(self) -> None:
        self.password = PasswordManager.hash(self.password)


class UserOutStructDTO(UserInStructDTO):
    id: PositiveIntMsgSpec
    updated_at: DTAware
    created_at: DTAware
