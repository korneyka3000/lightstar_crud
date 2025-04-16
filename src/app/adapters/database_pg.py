__all__ = (
    "session_config",
    "sqlalchemy_config",
)


from litestar.plugins.sqlalchemy import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
)

from src.config import settings


session_config = AsyncSessionConfig(expire_on_commit=False)

sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.DB_URL.unicode_string(),
    before_send_handler="autocommit",
    session_config=session_config,
)
