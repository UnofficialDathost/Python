from .base import MatchBase

from ..routes import MATCHES

from ..models.match import MatchModel


class AwaitingMatch(MatchBase):
    async def get(self) -> MatchModel:
        """Gets details on a match

        Returns
        -------
        MatchModel
            Holds match details.
        """

        data = await self._context._get(
            MATCHES.details.format(self.match_id)
        )

        return MatchModel(data)
