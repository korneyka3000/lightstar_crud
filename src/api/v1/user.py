__all__ = ("UserAPI",)


from typing import Annotated, cast

from advanced_alchemy.service import OffsetPagination
from litestar import Controller, delete, get, post, put
from litestar.di import Provide
from litestar.dto import DTOConfig
from litestar.dto.msgspec_dto import MsgspecDTO
from litestar.repository.filters import LimitOffset
from pydantic import PositiveInt

from src.app.schemas.user import UserInStructDTO, UserOutStructDTO
from src.services import UserService, provide_user_service


class UserAPI(Controller):
    path = "/users"
    dependencies = {"service": Provide(provide_user_service)}
    tags = ["User"]
    dto = MsgspecDTO[UserInStructDTO]
    return_dto = MsgspecDTO[
        Annotated[UserOutStructDTO, DTOConfig(exclude={"password"})]
    ]

    @post()
    async def create_user(
        self,
        data: UserInStructDTO,
        service: UserService,
    ) -> UserOutStructDTO:
        return cast(UserOutStructDTO, await service.create(data=data))

    @get()
    async def get_users(
        self,
        service: UserService,
        limit_offset: LimitOffset,
    ) -> OffsetPagination[UserOutStructDTO]:
        results, total = await service.list_and_count(limit_offset)
        return service.to_schema(
            data=results,
            total=total,
            filters=[limit_offset],
            schema_type=UserOutStructDTO,
        )

    @get("/{user_id:int}")
    async def get_user(
        self,
        user_id: PositiveInt,
        service: UserService,
    ) -> UserOutStructDTO:
        return cast(UserOutStructDTO, await service.get(user_id))

    @put("/{user_id:int}")
    async def update_user(
        self,
        user_id: PositiveInt,
        data: UserInStructDTO,
        service: UserService,
    ) -> UserOutStructDTO:
        return cast(UserOutStructDTO, await service.update(data, user_id))

    @delete("/{user_id:int}")
    async def delete_user(
        self,
        user_id: PositiveInt,
        service: UserService,
    ) -> None:
        await service.delete(user_id)
