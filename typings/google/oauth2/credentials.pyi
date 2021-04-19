from typing import Any, List


class Credentials:
    @staticmethod
    def from_authorized_user_file(token_file: str, scopes: List[str]) -> Any:
        ...
