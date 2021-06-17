from typing import cast, TYPE_CHECKING

from .base import MatchBase
from ..routes import MATCHES
from ..models.match import MatchModel

if TYPE_CHECKING:
    from .. import Blocking


class BlockingMatch(MatchBase):
    _context: "Blocking"

    def get(self) -> MatchModel:
        """Gets details on a match

        Returns
        -------
        MatchModel
            Holds match details.
        """

        data = cast(
            dict,
            self._context._get(
                MATCHES.details.format(self.match_id)
            )
        )

        return MatchModel(data)
