import requests
import os

from dotenv import load_dotenv
load_dotenv()

def exchangeCode(code: str) -> [dict, dict]:
    data: [str, str] = {
        "client_id": os.environ.get("CLIENT_ID"),
        "client_secret": os.environ.get("CLIENT_SECRET"),
        "grant_type": os.environ.get("GRANT_TYPE"),
        "code": code,
        "redirect_uri": os.environ.get("REDIRECT_URI"),
        "scope": os.environ.get("SCOPE"),
    }
    headers: [str, str] = {"Content-Type": "application/x-www-form-urlencoded"}
    response: any = requests.post(
        "https://discord.com/api/oauth2/token", data=data, headers=headers
    )
    credentials: dict = response.json()
    access_token: str = credentials["access_token"]
    user_response: any = requests.get(
        "https://discord.com/api/users/@me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    guilds_response: any = requests.get(
        "https://discord.com/api/users/@me/guilds",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user: dict = user_response.json()
    guilds: dict = guilds_response.json()
    return [user, guilds]