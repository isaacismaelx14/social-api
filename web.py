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


def connectToTwitter(user):
    consumer_key = TWITTER_CONSUMER_KEY
    consumer_secret = TWITTER_CONSUMER_SECRET
    access_token = TWITTER_ACCESS_TOKEN
    access_token_secret = TWITTER_ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    data = api.get_user(user)
    userData = data._json

    return {'followers': userData['followers_count'], 'name': userData['name'], 'pic_url': userData['profile_image_url_https']}


def connectToYoutube(channel_id):
    api_key = YOUTUBE_API_KEY
    linkById = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&part=snippet&id={channel_id}&key={api_key}'
    linkByUserName = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&part=snippet&forUsername={channel_id}&key={api_key}'
    requestId = requests.get(linkById)
    requestUserName = requests.get(linkByUserName)
    youtubeJson = json.loads(requestId.content)
    if(youtubeJson["pageInfo"]["totalResults"] == 0):
        youtubeJson = json.loads(requestUserName.content)

    youtubeSucribers = youtubeJson["items"][0]["statistics"]["subscriberCount"]
    youtubeChannelName = youtubeJson["items"][0]["snippet"]["localized"]["title"]
    youtubeChannelPic = youtubeJson["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
    return {'followers': youtubeSucribers, 'name': youtubeChannelName, 'pic_url': youtubeChannelPic}


def connectToInstagram(user):
    instagram = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(instagram.context, user)
    return {'followers': profile.followers, 'name': profile.full_name, 'pic_url': profile.profile_pic_url}


# For test :)
# print(
#     connectToYoutube('MARCIANOPHONE')
# )
