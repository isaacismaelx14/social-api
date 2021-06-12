import web
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/instagram/<string:user>')
def instagram(user):
    return jsonify(web.connectToInstagram(user))


@app.route('/youtube')
def youtube():
    return jsonify(web.connectToYoutube('MARCIANOPHONE'))


@app.route('/twitter')
def twitter():
    return jsonify(web.connectToTwitter('elonmusk'))


@app.route('/all')
def all():
    youtube_user = request.args.get('youtube')
    twitter_user = request.args.get('twitter')
    instagram_user = request.args.get('instagram')
    return jsonify({
        'youtube': web.connectToYoutube(youtube_user),
        'twitter': web.connectToTwitter(twitter_user),
        'instagram': web.connectToInstagram(instagram_user)
    })


if __name__ == '__main__':
    app.run(debug=True, port=4000)
