from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import Awaiting, Blocking


class MatchBase:
    def __init__(self, context: Union["Awaiting", "Blocking"],
                 match_id: str) -> None:
        self._context = context
        self.match_id = match_id


class SeriesBase:
    def __init__(self, context: Union["Awaiting", "Blocking"],
                 series_id: str) -> None:
        self._context = context
        self.series_id = series_id
