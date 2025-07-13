import datetime

from sqlalchemy.orm import Mapped, mapped_column
from advanced_alchemy.base import UUIDBase, UUIDAuditBase
from advanced_alchemy.types import DateTimeUTC


class resources(UUIDAuditBase):
    __tablename__ = "resources"

    delete_at: Mapped[datetime.datetime] = mapped_column(
        DateTimeUTC(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
    )

    # create_by: Mapped[] = mapped_column()
