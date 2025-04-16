__all__ = (
    "PositiveIntMsgSpec",
    "DTAware",
)

from datetime import datetime
from typing import Annotated

import msgspec


PositiveIntMsgSpec = Annotated[int, msgspec.Meta(gt=0)]
DTAware = Annotated[datetime, msgspec.Meta(tz=True)]
