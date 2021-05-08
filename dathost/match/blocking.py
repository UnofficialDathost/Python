from .base import MatchBase

from ..routes import MATCHES

from ..models.match import MatchModel


class BlockingMatch(MatchBase):
    def get(self) -> MatchModel:
        """Gets details on a match

        Returns
        -------
        MatchModel
            Holds match details.
        """

        data = self._context._get(
            MATCHES.details.format(self.match_id)
        )

        return MatchModel(data)
