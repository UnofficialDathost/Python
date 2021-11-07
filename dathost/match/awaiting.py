from typing import TYPE_CHECKING, cast

from .base import MatchBase, SeriesBase
from ..routes import MATCHES, MATCH_SERIES
from ..models.match import MatchModel, MatchSeriesModel

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


class AwaitingSeries(SeriesBase):
    _context: "Awaiting"

    async def get(self) -> MatchSeriesModel:
        """Gets details on a match

        Returns
        -------
        MatchSeriesModel
            Holds series details.
        """

        data = cast(
            dict,
            await self._context._get(
                MATCH_SERIES.details.format(self.series_id)
            )
        )

        return MatchSeriesModel(data)
