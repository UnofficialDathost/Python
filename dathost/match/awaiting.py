from typing import TYPE_CHECKING, cast

from .base import MatchBase
from ..routes import MATCHES
from ..models.match import MatchModel

if TYPE_CHECKING:
    from .. import Awaiting


class AwaitingMatch(MatchBase):
    _context: "Awaiting"

    async def get(self) -> MatchModel:
        """Gets details on a match

        Returns
        -------
        MatchModel
            Holds match details.
        """

        data = cast(
            dict,
            await self._context._get(
                MATCHES.details.format(self.match_id)
            )
        )

        return MatchModel(data)
