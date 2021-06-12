# Social Media API (Python)

This API Rest you could get any user data from: `Instgram, Twitter and youtube`  (_more coming soon_). \
_created for [Social Dashobard](https://github.com/isaacismaelx14/dashboard-react)_

## First steps 🦶
**Install packages:** \
`pip install -r requirements.txt` \

**Start app:** \
`py .\app.py` or `python .\app.py`

__*You need to create an API key from
[Twitter API](https://developer.twitter.com/en) & [Youtube API](https://console.cloud.google.com/) and after create the `.env` file with the keys.*__ 


**Variables:**

```
YOUTUBE_API_KEY=""
TWITTER_CONSUMER_KEY=""
TWITTER_CONSUMER_SECRET=""
TWITTER_ACCESS_TOKEN=""
TWITTER_ACCESS_TOKEN_SECRET=""
```

## Instagram: 📸
`localhost/instagram/{USER}`

------

## Twitter: 📖
`localhost/twitter/{USER}`

------

## Youtube: 📽
`localhost/youtube/{USER or CHANNEL_ID}` \
_**NOTE:** You cannot use the channel's name_

------

## All Social Networks:📱
`localhost/all?{params...}`
### Params: 
`instagram={USER}` \
`twitter={USER}` \
`youtube={CHANNEL}`

___

# TO DO 📃
## Implement also for:  
 - `Facebook`
 - `Gitghub` 

 > created with 💖 by: [isaacismaelx14](https://github.com/isaacismaelx14)
