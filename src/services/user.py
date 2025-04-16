__all__ = (
    "UserService",
    "provide_user_service",
)

from collections.abc import AsyncGenerator

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.models import User
from src.repository import UserRepo


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    """User service."""

    repository_type = UserRepo

    # async def get_user(self, user_id: int) -> User:
    #     user = await self.repository.get_one_or_none(User.id == user_id)
    #     if user is None:
    #         raise HTTPException(
    #             detail=f"User with id {user_id} not found",
    #             status_code=HTTP_404_NOT_FOUND,
    #         )
    #     return user


async def provide_user_service(db_session: AsyncSession) -> AsyncGenerator[UserService]:
    """This provides the default Authors repository."""
    async with UserService.new(session=db_session) as service:
        yield service
