import social
import os
from flask import Flask, jsonify, request, render_template

PORT = os.environ.get('PORT')
app = Flask(__name__)


def __check(data):
    if data:
        return jsonify(data), 201
    else:
        return jsonify({"error": f'user not found'}), 404


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/instagram/<string:user>')
def instagram(user):
    return __check(social.instagram(user))


@app.route('/youtube/<string:user>')
def youtube(user):
    return __check(social.youtube(user))


@app.route('/twitter/<string:user>')
def twitter(user):
    return __check(social.twitter(user))


@app.route('/all')
def all():
    youtube_user = request.args.get('youtube')
    twitter_user = request.args.get('twitter')
    instagram_user = request.args.get('instagram')
    response = {}

    if (youtube_user == None and twitter_user == None and instagram_user == None):
        return jsonify({'error': "You haven't params, verify documentation"})

    if youtube_user != None:
        response['youtube'] = social.youtube(youtube_user)
    if twitter_user != None:
        response['twitter'] = social.twitter(twitter_user)
    if instagram_user != None:
        response['instagram'] = social.instagram(instagram_user)

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=PORT or 4000)
