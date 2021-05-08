class MatchBase:
    def __init__(self, context: object, match_id: str) -> None:
        self._context = context
        self.match_id = match_id
