import social
import os
import html
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template

PORT = os.environ.get('PORT')

app = Flask(__name__)
CORS(app)
HTMLTEMPLATE = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>API SOCIAL APP</title>
    <style>
      * {
        margin: 0;
        padding: 0;
      }
      .container {
        margin: auto;
        width: 90%;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Welcome to API SOCIAL APP</h1>
      <a href="https://github.com/isaacismaelx14/social-api">VIEW ON GITHUB</a>
      <span>Bye</span>
    </div>
  </body>
</html>
'''


def __check(data):
    if data:
        return jsonify(data), 201
    else:
        return jsonify({"error": f'user not found'}), 404


@app.route('/')
def index():
    return HTMLTEMPLATE


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
