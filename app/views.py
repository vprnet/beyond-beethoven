from index import app
from flask import render_template, request
from config import BASE_URL


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = 'Beyond Beethoven'

    social = {
        'title': "Beyond Beethoven",
        'subtitle': "A production of VPR Classical and the Burlington Ensemble",
        'img': "",
        'description': "",
        'twitter_text': "",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        social=social,
        page_url=page_url)
