from typing import Any, List


class InstalledAppFlow:
    @staticmethod
    def from_client_secrets_file(client_secrets_file: str, scopes: List[str]) -> Any:
        ...
