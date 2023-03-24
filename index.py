# -*- coding: utf-8 -*-
import os
import json
import requests


def get_playlists(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(
        "https://api.spotify.com/v1/me/playlists", headers=headers)
    if response.status_code == 200:
        return response.json()["items"]
    else:
        return None


def get_liked_songs(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(
        "https://api.spotify.com/v1/me/top/artists", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def print_answer(msg):
    #   parse the JSON object
    token = json.loads(os.environ["spotify_auth"])

    playlists = get_liked_songs(token["access_token"])

    return playlists


def run(msg):
    return print_answer(msg)


def setup(config):
    os.environ["spotify_auth"] = config["spotify_auth"]
