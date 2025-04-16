from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from advanced_alchemy.filters import FilterTypes, LimitOffset
from litestar import Litestar
from litestar.di import Provide
from litestar.params import Parameter
from litestar_granian import GranianPlugin

from src.api import router
from src.app.adapters.database_pg import sqlalchemy_config


async def provide_limit_offset_pagination(
    offset: int = Parameter(ge=1, query="offset", default=1, required=False),
    limit: int = Parameter(
        query="limit",
        ge=1,
        default=10,
        required=False,
    ),
) -> FilterTypes:
    return LimitOffset(limit, limit * (offset - 1))


alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)
app = Litestar(
    route_handlers=[router],
    plugins=[alchemy, GranianPlugin()],
    dependencies={"limit_offset": Provide(provide_limit_offset_pagination)},
)
