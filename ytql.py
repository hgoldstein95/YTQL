# -*- coding: utf-8 -*-

import os
from typing import Any

import googleapiclient.discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    CLIENT_SECRETS_FILE = "client-secret.json"
    TOKEN_FILE = "token.json"
    SCOPES = ["https://www.googleapis.com/auth/youtube"]

    creds: Any = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow: Any = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    youtube: Any = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=creds)

    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "YTQL: Better Subscriptions",
                "description": "An automatically generated playlist that's better than the normal subscription feed.",
                "tags": [
                    "auto-generated"
                ],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
