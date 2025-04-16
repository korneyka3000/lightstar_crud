__all__ = ("User",)


from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped


class User(BigIntAuditBase):
    __tablename__ = "user"

    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]
