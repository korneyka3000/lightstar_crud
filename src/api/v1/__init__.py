__all__ = ("router",)

from litestar import Router

from .user import UserAPI


router = Router(path="/v1", route_handlers=[UserAPI])
