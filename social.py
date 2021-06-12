import time
import requests
import json
import instaloader
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')


def __get_yt_link(get, channel_id):
    return f'https://www.googleapis.com/youtube/v3/channels?part=statistics&part=snippet&{get}={channel_id}&key={YOUTUBE_API_KEY}'


def __get_yt_json(channel_id):
    requestId = requests.get(__get_yt_link('id', channel_id))
    requestUserName = requests.get(__get_yt_link('forUsername', channel_id))
    res_json = json.loads(requestId.content)
    if(res_json["pageInfo"]["totalResults"] == 0):
        res_json = json.loads(requestUserName.content)

    return res_json


def youtube(channel_id):
    try:
        res_json = __get_yt_json(channel_id)
        item = res_json["items"][0]
        subs = item["statistics"]["subscriberCount"]
        name = item["snippet"]["localized"]["title"]
        pic_url = item["snippet"]["thumbnails"]["medium"]["url"]
        return {'followers': subs, 'name': name, 'pic_url': pic_url}
    except:
        return False


def twitter(user):
    try:
        auth = tweepy.OAuthHandler(
            TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN,
                              TWITTER_ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)

        data = api.get_user(user)
        userData = data._json

        return {'followers': userData['followers_count'], 'name': userData['name'], 'pic_url': userData['profile_image_url_https']}
    except:
        return False


def instagram(user):
    try:
        instagram = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(instagram.context, user)
        return {'followers': profile.followers, 'name': profile.full_name, 'pic_url': profile.profile_pic_url}
    except:
        return False


# For test :)
# print(
#     youtube('MARCIANOPHONE')
# )
