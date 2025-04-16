__all__ = ("UserRepo",)


from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository

from src.app.models import User


class UserRepo(SQLAlchemyAsyncRepository[User]):
    model_type = User
